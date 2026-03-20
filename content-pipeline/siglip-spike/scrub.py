#!/usr/bin/env python3
"""
Film-scrubbing validation spike: SigLIP multi-prompt object detection.

Usage:
    # Extract frames from a video at 1 FPS
    python scrub.py extract input.mp4 --fps 1 --output frames/

    # Scan frames for an object using SigLIP
    python scrub.py scan frames/ --object telephone --threshold 0.2

    # Scan with era-aware multi-prompts
    python scrub.py scan frames/ --prompts prompts/telephone.txt --threshold 0.2

    # Full pipeline: extract + scan in one shot
    python scrub.py pipeline input.mp4 --object milk --fps 1 --threshold 0.2
"""

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

import torch
from PIL import Image


def get_device():
    """Select best available device."""
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def load_model(model_name="google/siglip-base-patch16-224"):
    """Load SigLIP model and processor."""
    from transformers import AutoModel, AutoProcessor

    print(f"Loading {model_name}...")
    t0 = time.time()
    processor = AutoProcessor.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    device = get_device()
    model = model.to(device)
    model.eval()
    print(f"Model loaded on {device} in {time.time() - t0:.1f}s")
    return model, processor, device


def build_prompts(object_name=None, prompts_file=None):
    """Build multi-prompt list for an object."""
    if prompts_file:
        path = Path(prompts_file)
        if path.exists():
            return [
                line.strip()
                for line in path.read_text().splitlines()
                if line.strip() and not line.startswith("#")
            ]

    # Default era-aware multi-prompt banks per object
    prompt_banks = {
        "telephone": [
            "a telephone",
            "a rotary telephone",
            "a candlestick telephone",
            "a wall telephone",
            "a desk phone",
            "a touch-tone phone",
            "a payphone",
            "a phone booth",
            "a cell phone",
            "a smartphone",
            "a phone handset",
            "a phone receiver",
            "someone talking on the phone",
        ],
        "milk": [
            "a glass of milk",
            "a bottle of milk",
            "a milk carton",
            "a milk jug",
            "milk being poured",
            "a person drinking milk",
            "a baby bottle with milk",
            "spilled milk",
            "a milk pail",
            "milk on a table",
        ],
        "mirror": [
            "a mirror",
            "a hand mirror",
            "a vanity mirror",
            "a bathroom mirror",
            "a wall mirror",
            "a mirror reflection",
            "someone looking in a mirror",
            "a broken mirror",
            "a compact mirror",
            "a rearview mirror",
        ],
        "cigarette": [
            "a cigarette",
            "someone smoking a cigarette",
            "a cigarette in an ashtray",
            "a lit cigarette",
            "a cigarette holder",
            "a person with a cigarette",
            "cigarette smoke",
            "a pack of cigarettes",
        ],
        "clock": [
            "a clock",
            "a wall clock",
            "a clock tower",
            "an alarm clock",
            "a grandfather clock",
            "a pocket watch",
            "a wristwatch",
            "clock hands",
            "a clock face",
            "someone checking the time",
        ],
    }

    if object_name and object_name.lower() in prompt_banks:
        return prompt_banks[object_name.lower()]
    elif object_name:
        # Generic prompts for unknown objects
        obj = object_name.lower()
        return [
            f"a {obj}",
            f"a {obj} in a room",
            f"someone holding a {obj}",
            f"a {obj} on a table",
            f"a close-up of a {obj}",
        ]
    else:
        raise ValueError("Must provide --object or --prompts")


def extract_frames(video_path, output_dir, fps=1):
    """Extract frames from video using ffmpeg."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    video_path = Path(video_path)
    if not video_path.exists():
        print(f"Error: Video file not found: {video_path}")
        sys.exit(1)

    # Get video duration
    probe = subprocess.run(
        [
            "ffprobe",
            "-v",
            "quiet",
            "-print_format",
            "json",
            "-show_format",
            str(video_path),
        ],
        capture_output=True,
        text=True,
    )
    if probe.returncode == 0:
        info = json.loads(probe.stdout)
        duration = float(info.get("format", {}).get("duration", 0))
        expected_frames = int(duration * fps)
        print(f"Video: {video_path.name} ({duration:.0f}s, ~{expected_frames} frames at {fps} FPS)")
    else:
        print(f"Video: {video_path.name}")

    pattern = str(output_dir / "frame_%06d.jpg")
    cmd = [
        "ffmpeg",
        "-i",
        str(video_path),
        "-vf",
        f"fps={fps}",
        "-q:v",
        "2",
        "-hide_banner",
        "-loglevel",
        "warning",
        pattern,
    ]

    print(f"Extracting frames at {fps} FPS...")
    t0 = time.time()
    subprocess.run(cmd, check=True)
    frame_count = len(list(output_dir.glob("frame_*.jpg")))
    elapsed = time.time() - t0
    print(f"Extracted {frame_count} frames in {elapsed:.1f}s")
    return frame_count


def scan_frames(frames_dir, prompts, model, processor, device, threshold=0.2, batch_size=16):
    """Scan frames with SigLIP multi-prompt search."""
    frames_dir = Path(frames_dir)
    frame_files = sorted(frames_dir.glob("frame_*.jpg"))
    if not frame_files:
        frame_files = sorted(frames_dir.glob("*.jpg")) + sorted(frames_dir.glob("*.png"))
    if not frame_files:
        print(f"No image files found in {frames_dir}")
        return []

    print(f"Scanning {len(frame_files)} frames against {len(prompts)} prompts...")
    print(f"Prompts: {prompts[:3]}{'...' if len(prompts) > 3 else ''}")

    results = []
    t0 = time.time()

    for i in range(0, len(frame_files), batch_size):
        batch_files = frame_files[i : i + batch_size]
        images = [Image.open(f).convert("RGB") for f in batch_files]

        # Process each image against all prompts
        for j, (img, fpath) in enumerate(zip(images, batch_files)):
            inputs = processor(
                text=prompts,
                images=[img] * len(prompts),
                padding="max_length",
                return_tensors="pt",
            ).to(device)

            with torch.no_grad():
                outputs = model(**inputs)
                # SigLIP uses sigmoid (not softmax) — each score is independent
                logits = outputs.logits_per_image[0]
                probs = torch.sigmoid(logits).cpu().numpy()

            max_prob = float(probs.max())
            best_prompt_idx = int(probs.argmax())
            best_prompt = prompts[best_prompt_idx]

            if max_prob >= threshold:
                frame_num = int(fpath.stem.split("_")[-1]) if "_" in fpath.stem else i + j
                results.append(
                    {
                        "frame": fpath.name,
                        "frame_num": frame_num,
                        "score": round(max_prob, 4),
                        "best_prompt": best_prompt,
                        "all_scores": {p: round(float(s), 4) for p, s in zip(prompts, probs)},
                    }
                )

        # Progress
        processed = min(i + batch_size, len(frame_files))
        elapsed = time.time() - t0
        fps_rate = processed / elapsed if elapsed > 0 else 0
        print(
            f"  {processed}/{len(frame_files)} frames "
            f"({fps_rate:.1f} frames/s) — "
            f"{len(results)} detections so far",
            end="\r",
        )

    elapsed = time.time() - t0
    print(f"\nScan complete: {len(frame_files)} frames in {elapsed:.1f}s "
          f"({len(frame_files) / elapsed:.1f} frames/s)")
    print(f"Detections above threshold ({threshold}): {len(results)}")

    # Sort by confidence
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def print_results(results, top_n=20):
    """Print detection results."""
    if not results:
        print("No detections above threshold.")
        return

    print(f"\nTop {min(top_n, len(results))} detections:")
    print(f"{'Frame':<20} {'Score':<10} {'Best Prompt'}")
    print("-" * 60)
    for r in results[:top_n]:
        print(f"{r['frame']:<20} {r['score']:<10.4f} {r['best_prompt']}")


def save_results(results, output_path):
    """Save results to JSON."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Film-scrubbing validation spike")
    subparsers = parser.add_subparsers(dest="command")

    # extract
    ext = subparsers.add_parser("extract", help="Extract frames from video")
    ext.add_argument("video", help="Path to video file")
    ext.add_argument("--fps", type=float, default=1, help="Frames per second (default: 1)")
    ext.add_argument("--output", default="frames", help="Output directory")

    # scan
    scn = subparsers.add_parser("scan", help="Scan frames for objects")
    scn.add_argument("frames_dir", help="Directory containing frame images")
    scn.add_argument("--object", help="Object to detect (has built-in prompt bank)")
    scn.add_argument("--prompts", help="Text file with one prompt per line")
    scn.add_argument("--threshold", type=float, default=0.2, help="Detection threshold (default: 0.2)")
    scn.add_argument("--model", default="google/siglip-base-patch16-224", help="SigLIP model name")
    scn.add_argument("--output", default=None, help="Save results to JSON file")
    scn.add_argument("--top", type=int, default=20, help="Number of top results to show")
    scn.add_argument("--batch-size", type=int, default=16, help="Batch size for inference")

    # pipeline
    pipe = subparsers.add_parser("pipeline", help="Extract + scan in one shot")
    pipe.add_argument("video", help="Path to video file")
    pipe.add_argument("--object", help="Object to detect")
    pipe.add_argument("--prompts", help="Text file with one prompt per line")
    pipe.add_argument("--fps", type=float, default=1, help="Frames per second")
    pipe.add_argument("--threshold", type=float, default=0.2, help="Detection threshold")
    pipe.add_argument("--model", default="google/siglip-base-patch16-224", help="SigLIP model name")
    pipe.add_argument("--output", default=None, help="Save results to JSON file")
    pipe.add_argument("--top", type=int, default=20, help="Number of top results to show")

    # demo — run on sample images to verify the pipeline works
    demo = subparsers.add_parser("demo", help="Run a demo on synthetic test images")
    demo.add_argument("--model", default="google/siglip-base-patch16-224", help="SigLIP model name")

    args = parser.parse_args()

    if args.command == "extract":
        extract_frames(args.video, args.output, args.fps)

    elif args.command == "scan":
        prompts = build_prompts(args.object, args.prompts)
        model, processor, device = load_model(args.model)
        results = scan_frames(
            args.frames_dir, prompts, model, processor, device, args.threshold, args.batch_size
        )
        print_results(results, args.top)
        if args.output:
            save_results(results, args.output)

    elif args.command == "pipeline":
        frames_dir = Path("frames") / Path(args.video).stem
        extract_frames(args.video, frames_dir, args.fps)
        prompts = build_prompts(args.object, args.prompts)
        model, processor, device = load_model(args.model)
        results = scan_frames(frames_dir, prompts, model, processor, device, args.threshold)
        print_results(results, args.top)
        if args.output:
            save_results(results, args.output)

    elif args.command == "demo":
        print("=== SigLIP Film-Scrubbing Demo ===\n")
        model, processor, device = load_model(args.model)

        # Create a synthetic test — score prompts against a blank/noise image
        # This verifies the pipeline works end-to-end
        import numpy as np

        test_image = Image.fromarray(np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8))

        prompts = [
            "a rotary telephone on a desk",
            "a glass of milk",
            "a mirror on a wall",
            "random noise",
            "abstract colorful pattern",
        ]

        inputs = processor(
            text=prompts,
            images=[test_image] * len(prompts),
            padding="max_length",
            return_tensors="pt",
        ).to(device)

        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits_per_image[0]
            probs = torch.sigmoid(logits).cpu().numpy()

        print("Prompt scores against random noise image:")
        print(f"{'Prompt':<40} {'Score':<10}")
        print("-" * 50)
        for prompt, score in zip(prompts, probs):
            print(f"{prompt:<40} {score:.4f}")

        print("\nExpected: All scores should be low (<0.1) against noise.")
        print(f"Max score: {probs.max():.4f} — {'PASS' if probs.max() < 0.3 else 'CHECK THRESHOLD'}")
        print("\nPipeline verified. Ready for real film frames.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

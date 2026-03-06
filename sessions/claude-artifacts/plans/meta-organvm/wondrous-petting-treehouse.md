# Synthesis: The Director, the Habitat, and the Knowledge Agents

## The Thread (What Was Said, In Order)

This session began with a concrete audit and progressively surfaced a deeper architectural insight about how this entire system operates — not just at the code level but at the level of *who thinks what*.

### 1. "Where does all this infrastructure live?"

The audit produced tests, reports, governance docs, GitHub issues. The first question was purely spatial: which directories, which repos, which level of the ORGANVM hierarchy? Answer: tests co-locate with source, planning docs live in `docs/planning/`, quality gates in `scripts/validation/`, organ-level policies in `commerce--meta/governance/`, system-level truth in `meta-organvm/organvm-corpvs-testamentvm/`. We mapped the full four-level propagation chain (repo → organ → system → orchestration).

### 2. "Explain the whole system to me conversationally"

A request to step back from the map and tell the story. What emerged: ORGANVM is an eight-organ creative-institutional system run by one person using AI to generate volume. Styx is a behavioral market that weaponizes loss aversion. The Fury auditors are a decentralized jury. The linguistic cloaker hides regulated vocabulary. The governance flows upward through a registry. All of it operates under an "AI-conductor model" — human directs, AI generates, human reviews.

### 3. "Where was the SOP written and stored?"

It wasn't. The audit produced artifacts, but no one wrote the reusable playbook for *how to equip any repo with this governance structure at each stage of its life*. This revealed a gap: the system had the artifacts but not the meta-knowledge of when and why each artifact becomes necessary.

### 4. The philosophical reframe

> "Once an idea moves from abstract to concrete, the constructed-universe suddenly takes shape to form the perfect habitats to not only root, but experiment, pivot, take new shape, grow endlessly like a beautiful chaotic element of nature."

This reframed the entire SOP question. The ORGANVM isn't a filing cabinet. It's a living topology. Ideas don't get assigned to organs — they germinate, find affinity, and root themselves. Governance artifacts aren't bureaucratic overhead — they're soil conditions. A seedling doesn't need a SECURITY.md. A tree bearing fruit that strangers pay for does. The promotion ladder (LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED) encodes this organic growth logic.

This became document 12 in the system standards: `12-habitat-governance-lifecycle.md`.

### 5. The director and the archetypal specialists

> "A great innovator/director doesn't know about legal docs, or child labor laws, or lens specifications — that data is trusted to someone with that specified knowledge. What I'm creating then is a position for an abstract thinker whose thinking is specified in that level, and he's orchestrating *to* [an algorithmic process]."

The original transcription heard "two knowledge-based AI experts." The actual meaning: **orchestrating *toward*** an algorithmic process — a repeatable, self-contained specialist that deliberates an efficient method to produce the artifact its archetypal role was designed to produce.

Each specialist is not a general assistant. It is a **historically complete corpus contextual expert** of exactly one thing — and quite literally nothing else. It is the AI equivalent of a person who was hired to do one job, who has read every book written about that job, who has done that job ten thousand times, and who would look at you blankly if you asked about anything outside their domain.

In a traditional business, you'd hire:
- A security specialist who writes SECURITY.md because she's written a thousand of them
- A legal counsel who drafts compliance policy because that's all he does
- A behavioral economist who validates the loss-aversion constants
- A DevOps engineer who wires CI gates

The director doesn't know how to do any of these jobs. The director knows **that** they need to be done, and **when**, and **why** — because the director holds the vision of what the organism is becoming. The specialists produce the artifacts. The director composes the specialists into a coherent system.

**The ORGANVM is the infrastructure that makes this possible for one person.** The original problem: a creative person with ideas wants to bring them to audiences at the same level and quality as the head of a business that someone accidentally stumbled into (inherited resources, institutional support, existing teams). Traditionally, you think small because resources are scarce. But that constraint has *inverted*. AI specialists can be spun up as needed, each one a de facto know-it-all about their specific assignment. The infrastructure should not shrink the idea — it should grow to contain it.

This means:
- The skill library (`a-i--skills/`, 70+ skills) is the **bench of available specialists**
- Each skill is an archetypal role definition: what it knows, what it produces, what it ignores
- The director doesn't choose skills by name — the director expresses intent, and the system matches intent to the right specialist
- The specialist runs its process, produces its artifact, and exits. It doesn't linger. It doesn't opine on things outside its scope.

---

## Open Questions for Investigation

### Q1: What is the director's actual interface?

Right now the director communicates through natural language in Claude Code sessions. Is that sufficient, or does the director need a more structured interface?

- The `seed.yaml` is a kind of declaration: "this is what I am, this is my stage." Does the director interact primarily through seed.yaml updates, or through session conversations, or through something else entirely?
- ORGAN-IV (Taxis) has `orchestration-start-here/` as a session entry point. Is that the director's console? What does it actually do today?
- The `conductor patch --json` command runs at session start. Is *that* the director's dashboard? What does it show, and is it sufficient for directorial-level awareness?

### Q2: How does intent map to specialist?

The skill library has 70+ skills. Each is an archetypal specialist. But the director doesn't think in skill names — the director thinks in intent ("this project needs protection," "this code smells wrong," "this pitch isn't landing").

- What is the matching mechanism? Today it's the director (or a general-purpose AI session) manually invoking `/evaluation-to-growth` or `/security-threat-modeler`. Is that sufficient, or does the system need an intent-routing layer?
- Should there be a "casting director" process that takes directorial intent and selects the right specialist(s)?
- How does the system handle cases where the right specialist doesn't exist yet? Is that when the `skill-creator` skill gets invoked — the meta-specialist that creates new specialists?
- The skills are currently static files in `a-i--skills/`. Should they accumulate institutional memory (e.g., "the last time I wrote a SECURITY.md for a financial product, here's what worked")? Or does that violate the "know everything about your role, nothing else" principle?

### Q3: Where does the abstract-to-concrete boundary actually sit?

You described a spectrum: abstract thought → research/AI-chats/idea storms → concrete implementation. The ORGANVM is the habitat for the concrete side. But where does the transition happen?

- Is Theoria (Organ I) the abstract side, and everything else is concrete?
- Or is the abstract/concrete boundary *within* each organ — every project has a brainstorm phase (abstract) and an implementation phase (concrete)?
- The `intake/` directory at the workspace root is described as "unsorted inbound material." Is that the anteroom where abstract ideas wait to find their organ?
- When you have an insight like "governance artifacts are soil conditions," that's abstract. When it becomes `12-habitat-governance-lifecycle.md`, it's concrete. Who decided *where* that document should root? You or the AI? (In this session, the AI chose `docs/standards/` based on proximity to docs 10 and 11. Was that right? Did it feel right to you, or did you have to trust the AI's knowledge of the directory structure?)

### Q4: The Pre-Codified Space — What Is It?

> "This begs the need for a space pre-codified, a space where ideas challenge one another, devour the other, multiply, but not affect the codified structured canon work."

This is a structural requirement that doesn't currently exist in the ORGANVM. The system has:

- **Intake** (`~/Workspace/intake/`) — unsorted inbound material, but this is a dumping ground, not an arena
- **Brainstorm directories** (`docs/brainstorm/` in various repos) — but these are already *inside* a codified project
- **Theoria** (Organ I) — foundational theory, but it has structure, seed.yaml contracts, promotion states
- **Claude session transcripts** — where a lot of the wild thinking actually happens, but they're ephemeral and un-navigable

What's missing is a **liminal space** — a place where:
- Ideas exist in draft form, arguing with each other
- Nothing is canonical yet — contradictions are allowed, even encouraged
- The director can think out loud without triggering governance machinery
- Ideas can be killed without ceremony (unlike ARCHIVED, which is a formal state)
- An idea that survives this space has *earned* its right to root in an organ

This is the dream-state counterpart to the wake-state organs. The organs are codified, structured, governed. This space is pre-codified, wild, ungoverned.

**Questions:**
- Is this a directory? A repo? A separate tool? A mode of interaction?
- Does it have *any* structure, or is structure itself the thing being resisted?
- Who curates it? The director? Nobody? Does it self-prune?
- What triggers graduation from the pre-codified space into an organ? Is it the director's judgment alone, or does something measurable happen?
- Does this space already exist implicitly (in Claude sessions, in voice memos, in the director's head) and just needs to be *named*? Or does naming it and giving it a location fundamentally change its character?
- Relationship to `intake/`: Is intake the pre-codified space, poorly named? Or is intake for *external* material coming in, while the pre-codified space is for *internal* ideation going out?

### Q5: Does the dream/wakefulness metaphor have structural implications beyond the pre-codified space?

> "We are often a dream looking at real-wakefulness, so I want to operate with a solid foot in the light and the dark, in order and chaos."

The pre-codified space addresses the dream side. But the metaphor implies the system needs to *continuously operate in both modes simultaneously* — not sequence them (dream first, then wake). The director holds both. The question is whether the infrastructure does.

Current state: the ORGANVM architecture biases heavily toward wake-state. Validation gates, promotion checklists, the registry, CI pipelines, seed.yaml contracts — these are all order. The chaos side happens in conversations and in the director's head, and leaves no trace in the system.

- Should the pre-codified space be a permanent organ (Organ 0? Organ IX?)? Or does making it an organ immediately codify it, defeating the purpose?
- Is the answer that the pre-codified space is *outside* the ORGANVM — it's the director's private territory, and the ORGANVM begins only when something crosses the threshold into structure?
- Or is the answer that *every* organ has a dream-state layer (the brainstorm directories) and a wake-state layer (the src directories), and the pre-codified space is the system-wide dream layer that feeds all of them?

### Q5: What already exists in ORGAN-IV that serves this model?

Before designing anything new, we need to understand what's already built:

- `agent--claude-smith/` — AI agent definitions. What agents are defined? Do they map to the "two knowledge experts" model?
- `a-i--skills/` — 70+ skills. These are specialized knowledge packages. Are they the "knowledge" that the experts draw from? Is the skill library the experts' training data?
- `orchestration-start-here/` — Session entry point. Is this the director's launch pad?
- `domus-semper-palingenesis/` — Environmental controller. Is this the infrastructure that ensures the director and the experts share the same context?

### Q6: Does document 12 need revision?

Document 12 (`12-habitat-governance-lifecycle.md`) was written *before* the specialist model was clarified. It describes what each promotion stage needs but frames the work as "things to do" — checklists. It doesn't say *who thinks what*.

Should it be revised to encode the director/specialist model at each stage?

- At LOCAL: the director senses a seed worth planting. No specialist involvement.
- At CANDIDATE: the director names it. A specialist (repo-standards archetype) produces seed.yaml, CLAUDE.md.
- At PUBLIC_PROCESS: the director says "this is ready for the world." Specialists produce SECURITY.md (security archetype), CONTRIBUTING.md (community-health archetype), ADRs (architecture-documenter archetype). Each knows everything about their artifact and nothing about the others.
- At GRADUATED: the director says "this is mature." Specialists ensure SLA docs (operations archetype), incident runbooks (incident-response archetype), external audit coverage (security-audit archetype).

Or is this over-engineering — does the checklist format work fine, and the director/specialist dynamic is implicit in *how* the checklists get executed rather than *what* they say?

### Q7: This session as a case study

What happened in this session maps the model precisely:

1. **Director**: "Where does this live?" — spatial intuition, not technical question
2. **Specialist response**: Mapped the four-level topology — structural knowledge
3. **Director**: "Explain it to me like a human" — directorial need for synthesis without jargon
4. **Specialist response**: Translated architecture into narrative — domain knowledge applied to communication
5. **Director**: "Where's the SOP?" — awareness of a gap the specialist missed
6. **Specialist response**: "It doesn't exist" — structural knowledge confirming the gap
7. **Director**: "Ideas find their habitat like nature" — philosophical reframe that restructures the entire problem
8. **Specialist response**: Wrote doc 12 — governance-specialist archetype producing its artifact
9. **Director**: "The director orchestrates *to* specialists" — meta-insight about the operating model itself
10. **Director**: "This needs a pre-codified space" — identifying a structural absence that no specialist would notice, because specialists only know their domain

Step 10 is the critical one. No specialist would have surfaced the need for a pre-codified space, because that need lives at the *system design* level — the director's level. The specialist knows how to write a SECURITY.md. Only the director knows that the system is missing a place where ideas fight before they become SECURITY.md-shaped.

This suggests: **the director's unique contribution is not executing any task but perceiving the shape of the system as a whole** — including the shapes that are missing.

### Q8: The resource inversion

> "Why must we think small? Because resources. But that problem has inverted."

This is the founding thesis of the ORGANVM, stated plainly. Traditionally, a solo creator is limited by what they can personally execute. AI has inverted this: execution capacity is now effectively unlimited (measured in tokens, not hours). The constraint has shifted from "can I do this work?" to "can I direct this work coherently?"

This inversion has implications for the system design:
- **The bottleneck is directorial bandwidth, not execution capacity.** The system should minimize the director's cognitive load, not maximize the number of tasks running.
- **Specialist depth matters more than specialist breadth.** A specialist that knows *everything* about SECURITY.md and produces a perfect one in seconds is more valuable than a generalist that produces a mediocre one after a conversation.
- **The pre-codified space is where the director's bandwidth is most scarce and most valuable.** Dream-state thinking — sensing what's missing, reframing problems, connecting distant ideas — is the one thing the specialists cannot do. The system should protect this space, not automate it.

**Questions:**
- Does the current system protect directorial bandwidth, or does it consume it? (How much time is spent on governance ceremony vs. creative direction?)
- Are the 70+ skills deep enough to be true archetypal specialists, or are they shallow prompts that still require the director to hold domain knowledge?
- What would it look like if a specialist were *so* complete that the director could say "this project needs protection" and the right artifacts would appear without further input?

---

## What's Resolved

1. **~~"Two" experts~~** — Resolved. Mis-transcription. "Orchestrating *to*" an algorithmic process. The model is: the director orchestrates toward archetypal specialists, each a historically complete corpus expert in exactly one domain.

2. **Scope** — Resolved. Universal but flexible. The director/specialist model is the operating model for all work. The specific specialists change by context, but the director role is constant.

3. **Relationship to the AI-conductor model** — Clarified. The workspace CLAUDE.md says "Human directs, AI generates volume, human reviews." The specialist model is a *deepening* of this: the AI generation isn't monolithic — it's composed of archetypal specialists, each producing the exact artifact their role was designed to produce. The director's job is sensing what's needed, not specifying how to produce it.

## What's Resolved (Session Conclusions)

### The Pre-Codified Space → Materia Collider

**Resolved.** The pre-codified space is a **repo** in `meta-organvm/` called `materia-collider`.

Why meta-organvm: Meta sits both above and below the organ system. It governs AND it's the substrate. The collider is meta-infrastructure — it serves all organs without belonging to any.

Why a repo (not just a directory): Because the collider isn't passive storage. It's an active laboratory. It has methods and systems for experimentation — ways to collide ideas, invert them, stress-test them, observe what new particles emerge. Those methods need to be designed, versioned, and iterated on.

Why "collider": A particle collider takes raw material, accelerates it, smashes it together at high energy, and observes what emerges. The materia-collider does the same with early-stage ideas. The hope is to get something genuinely *new* out of raw material — not just to sort ideas into boxes, but to create inversions, unexpected combinations, novel structures.

**Properties preserved from the workshop bench requirements:**
- Persistent (it's a repo)
- Unstructured (internally — the collider's own structure serves experimentation, not classification)
- Visible (top-level in meta-organvm, alongside the corpus and engine)
- Collision-friendly (its *purpose* is collision)
- Disposable (experimental results that don't produce new particles are discarded without ceremony)
- Traceable (git history traces how ideas evolved; graduation into an organ is linkable)

**Graduation model — all three simultaneously:**
1. Director moves it manually (intentional, ceremonial — for major insights)
2. Director signals, specialist executes (director says "this is ready," archetype specialist produces the organ-appropriate artifact)
3. Organic (during work sessions, collider material naturally becomes code or docs in an organ — no formal graduation, just absorption)

The graduation mode depends on the idea. A philosophical framework might graduate ceremonially. A code pattern might just get absorbed during implementation. A failed experiment gets swept off the bench.

**This document itself is the collider's first experiment.** It belongs in `materia-collider/` as a founding artifact — a synthesis-in-progress that emerged from concrete work (audit artifacts) and produced system-level insights (the director/specialist model, the collider itself).

## What's Still Open

1. **Collider internal design** — What methods and systems for experimentation does it contain? What does a "collision protocol" look like? What does an "inversion" of an idea mean in practice? This is the design work for the repo itself.

2. **Skill depth** — Are the 70+ skills deep enough to be true archetypal specialists? Or are they shallow prompts that still require the director to carry domain knowledge? This determines whether the vision is already realized or still aspirational.

3. **Intent routing** — The director doesn't think in skill names. How does directorial intent ("this project needs protection") get matched to the right specialist(s)? Is there an intermediary, or does the director learn to speak the system's language?

4. **Relationship between collider and intake** — `~/Workspace/intake/` is "unsorted inbound material." The collider is for active experimentation. Are they the same thing (rename intake to collider)? Complementary (intake is raw material *input*, collider is the *process*)? Or should intake feed into the collider as fuel?

---

---

## Deep Dive: The Collider's Methods

### Prior Art: The Expansive Inquiry System

An earlier attempt at this concept already exists: `meta-organvm/intake/OS-me/iAMGenRec/expand-ai-inquiry.txt`. It's a React app (V4) that runs any topic through 6 specialized AI roles in sequence:

| Role | Name | What It Does |
|------|------|-------------|
| Scope AI | Scope Clarification | Refines the core inquiry into a precise question |
| Logic AI | Logical Branching | 5 orthodox lines of inquiry, each drilled 3 levels deep |
| Mythos AI | Intuitive Branching | 5 metaphorical/mythopoetic framings + archetypal stories |
| Bridge AI | Lateral Exploration | 5 unrelated domains bridged to the topic via analogy |
| Meta AI | Recursive Design | Designs feedback loops that refine the inquiry itself |
| Pattern AI | Pattern Recognition | Scans all outputs for emergent meta-patterns |

Each stage passes its results to the next as context. The output is downloadable Markdown with YAML frontmatter. The critique notes (also in the file) envision adding:
- **Contradiction Detection** ("Dialectic AI") — surfaces productive friction between stages
- **Temporal Re-Inquiry** — re-run the same topic after a delay, compare past and present
- **Epistemic Signature** — visualize the cognitive shape of an inquiry (radar chart)
- **Ontology Builder** — extract terms and build a living concept map

**This is the materia-collider in embryonic form.** The 6-stage pipeline IS a collision protocol. But it's trapped in a React app that depends on `window.claude.complete`. The materia-collider needs to absorb and generalize this into something that works with any idea-generation process, not just a web UI.

### What a Collision Protocol Looks Like

Drawing from the Expansive Inquiry System and the particle collider metaphor:

**A particle collider has:**
1. **Beam preparation** — raw material is cleaned, focused, accelerated
2. **Collision event** — two beams meet at high energy
3. **Detector array** — instruments observe what flies out
4. **Data analysis** — physicists study the debris for new particles

**The materia-collider analogue:**

1. **Material preparation** — an idea enters the collider. It could be:
   - A sentence from a conversation
   - A half-formed hypothesis
   - A competitor observation
   - A philosophical reframe (like "governance is soil conditions")
   - Raw intake material (`intake/` feeds the collider)

   Preparation means giving it *just enough* form to collide with something else. Not structure — form. A name, a one-paragraph articulation, a provocation.

2. **Collision event** — two (or more) prepared ideas are smashed together. Methods:
   - **Dialectic collision**: Ideas that contradict each other are forced into the same frame. What survives?
   - **Analogical collision**: An idea from one domain is mapped onto a completely different domain. What transfers?
   - **Inversion collision**: An idea is negated. "What if the opposite were true?" What emerges?
   - **Scale collision**: An idea designed for one scale (personal, project, organ, system) is applied at a different scale. Does it hold?
   - **Temporal collision**: An idea from the past meets a current problem. Does it still apply? Has it mutated?
   - **Archetypal collision** (from the Expansive Inquiry System): An idea is run through multiple cognitive lenses — logic, myth, bridge, recursion, pattern

3. **Observation** — what flies out of the collision? New questions? New connections? Contradictions that reveal hidden assumptions? The collider doesn't judge results — it observes them. Some collisions produce nothing. Some produce a single insight. Some produce a new particle (an idea ready to root in an organ).

4. **Analysis** — over time, patterns emerge across collisions. Certain types of collisions consistently produce new particles. Certain ideas keep appearing in debris. The collider's own methods evolve based on what works.

### Inversion as a Primary Method

You specifically mentioned "inversions of ideas." This is the most interesting collision type because it's counterintuitive:

- **Resource inversion**: "We think small because resources are scarce" → "Resources are abundant; the constraint is direction." (This inversion founded the ORGANVM.)
- **Governance inversion**: "Governance constrains growth" → "Governance IS the soil that enables growth." (This session's key insight.)
- **Specialist inversion**: "One person can't know everything" → "One person doesn't need to; each specialist knows everything about one thing." (The archetypal specialist model.)
- **Structure inversion**: "Unstructured ideas need structure" → "A structured system needs an unstructured space." (The collider itself.)

Each of these inversions produced something fundamentally new. The collider should have an explicit "inversion protocol" — take any assumption and ask "what if the opposite?"

---

## Deep Dive: The Specialist Model

### Current Skill Depth Assessment

**Evaluated**: `evaluation-to-growth`, `security-implementation-guide`, `skill-creator`

| Skill | SKILL.md Size | References | Scripts | Assets | Depth Assessment |
|-------|--------------|------------|---------|--------|-----------------|
| evaluation-to-growth | ~200 lines | 3 templates (checklist, inline, report) | None | None | **Medium-deep.** Has a real 4-phase framework (Critique → Reinforcement → Risk → Growth) with structured prompts per phase. But lacks domain-specific knowledge — it's a generic evaluation framework, not a "historically complete corpus expert" in any domain. |
| security-implementation-guide | ~80+ lines | 2 refs (OWASP top 10, security checklist) | None | None | **Shallow.** Code snippets for common patterns (XSS, bcrypt, rate limiting). This is a cheat sheet, not an expert. A real security specialist would have deep knowledge of threat modeling, compliance frameworks, incident response, audit procedures, pen-testing methodology. |
| skill-creator | ~80+ lines | Yes | Yes (scripts/) | None | **Meta-deep.** Knows how to create skills — the anatomy, the progressive disclosure pattern, the bundled resource types. But it's a meta-skill, not a domain specialist. |

**Gap between current state and vision:**

Current skills are **prompt wrappers with reference material**. They tell Claude *how to approach* a task, not *everything there is to know* about a domain. The evaluation-to-growth skill says "assess logical consistency" but doesn't contain the entire corpus of rhetorical analysis. The security skill says "use bcrypt" but doesn't contain the NIST password guidelines, the OWASP testing guide, or the complete threat modeling literature.

To become the "historically complete corpus expert" the director envisions, skills would need:

1. **Much deeper references/** — not 2 files, but 10-20, covering the full domain. A security specialist skill would have: OWASP top 10 (already there), NIST 800-63 (password guidelines), STRIDE methodology, CWE top 25, PCI-DSS checklist for payment apps, GDPR data protection impact assessment template, incident response playbook template, etc.

2. **Institutional memory** — records of past executions. "The last time I wrote a SECURITY.md for a financial product (Styx), I included these sections and referenced these file paths." Currently skills are stateless — each invocation starts fresh.

3. **Narrower scope with deeper walls** — a skill that knows "everything about writing SECURITY.md files and literally nothing else" would be more useful than a general "security implementation guide." The specialist model demands role-narrowing, not role-broadening.

### The AI-Conductor Methodology Essay (Essay 09)

The existing essay `09-ai-conductor-methodology.md` describes a 4-phase workflow:
1. **Context Assembly** (human-led) — the director gathers context
2. **Generation** (AI-led) — AI produces first draft
3. **Review** (human-led) — director reviews for accuracy, voice, positioning
4. **Validation** (automated + human) — quality gates check the output

**Key quote from the essay**: "Context assembly is the most important phase because it determines the ceiling of the output quality. An AI given thin context produces thin documentation."

**How this maps to the specialist model:**

The essay describes the director doing context assembly manually — 15-30 minutes per repo, reading code, reading registry entries, formulating positioning. In the specialist model, this context assembly is what makes a specialist *specialist*. The context is pre-assembled in the skill's `references/` directory. The director doesn't need to gather it — the specialist already has it.

**The evolution**: Essay 09 describes the current model (director assembles context → AI generates). The specialist model is the *next* evolution: the context is baked into the specialist itself, so the director only needs to express intent ("this project needs protection") and the specialist already knows what SECURITY.md should contain, what file paths to reference, what sections are standard for a financial product.

### Genesis Documents

The genesis documents confirm the specialist concept already existed in embryo:

- `universal-orchestrator-architecture.md` (Dec 2025) describes a multi-agent system: **Architect, Implementer, Reviewer, Tester, Maintainer** — five named roles that discover projects via seed.yaml and route work to the appropriate agent. This is the archetypal specialist model, just with different role names.
- The orchestrator was originally called `omni-dromenon-machina` and sat in ORGAN-II. It evolved into ORGAN-IV (Taxis) as the orchestration organ.

**The collider is what's missing from the genesis architecture.** The genesis docs describe agents that *execute* on well-defined projects. They don't describe a space where ill-defined ideas become well-defined enough for agents to act on.

### The intake/ Directory

`meta-organvm/intake/` is currently a wild directory containing:
- Gemini session exports
- React prototypes (including the Expansive Inquiry System)
- Tractatus summaries, Dante cosmos guides
- Personal strategy docs ("Chris-Adaptation-Strategy.md")
- System design feedback
- Curriculum analysis
- AI shell experiments
- Auto-UID scripts
- Combined mythology/ingest engines

This IS the pre-codified space, in its most chaotic form. It's the workshop bench covered in sawdust. The materia-collider doesn't replace it — it gives it a name, a purpose, and experimental methods. The raw material in `intake/` is the **fuel**. The collider's protocols are the **accelerator**. What comes out the other end — if anything — roots in an organ.

---

## Synthesis: What the Materia Collider Is

A repo in `meta-organvm/` that serves three functions:

### 1. The Pre-Codified Space
Where ideas exist before they're structured enough for an organ. Unlike `intake/` (which is a dump), the collider is intentional. Ideas enter it with awareness that they're being experimented on.

### 2. The Experimental Apparatus
Methods for colliding ideas: dialectic, analogical, inversion, scale, temporal, archetypal. Each method is documented as a protocol. The Expansive Inquiry System's 6-stage pipeline is absorbed as one protocol ("archetypal collision") among several.

### 3. The Specialist Forge
Where new specialist archetypes are identified. When a collision produces a novel insight about *how to think* about a domain (not just *what to think*), that insight becomes the seed for a new skill in the skill library. The collider doesn't just produce ideas that root in organs — it produces specialists that join the bench.

### Relationship Map

```
intake/ (raw fuel)
    ↓ material preparation
materia-collider/ (experimental apparatus)
    ↓ collision → observation → analysis
    ↓
    ├─→ New idea roots in an organ (graduation)
    ├─→ New specialist archetype → skill library (forge)
    ├─→ Nothing useful → swept off the bench (disposal)
    └─→ Methodology refinement → collider improves itself (recursion)
```

---

## Deep Dive: The Inversion Protocol

### Evidence: Inversions in This Session

Every major insight that emerged was an inversion — an assumption flipped to reveal what was invisible from the original frame.

| # | Original Assumption (Hidden) | Inversion | What Became Visible |
|---|------------------------------|-----------|---------------------|
| 1 | "We think small because resources are scarce." | Resources are abundant (AI tokens). The constraint is *direction*. | The ORGANVM founding thesis. One person can operate at enterprise scale. |
| 2 | "Governance is overhead that slows a project down." | Governance is the *soil* that enables growth at each stage. | Doc 12: habitat governance lifecycle. The promotion ladder as organic growth. |
| 3 | "One person can't know everything needed to run a business." | One person doesn't need to. Each specialist knows *everything about one thing and nothing else*. | The archetypal specialist model. Skills as complete corpus experts. |
| 4 | "Unstructured ideas need to be organized into structure." | A structured system needs an *unstructured space* to stay alive. | The materia-collider. The pre-codified space. |
| 5 | "Ideas should be assigned to the right category." | Ideas *find their own habitat* through affinity, not assignment. | The organic topology metaphor. Ideas as seeds, organs as ecosystems. |
| 6 | "The SOP should tell you what to do." | The SOP should tell you *when each thing becomes necessary* — growth stages, not checklists. | Reframing doc 12 from compliance to care. |
| 7 | "A filing system stores ideas." | A collider *transforms* ideas. The point isn't storage — it's collision. | The materia-collider as laboratory, not library. |
| 8 | "The director needs to know how to do the work." | The director needs to know *that* the work needs doing, and *when*. The how belongs to the specialist. | Clean separation of directorial perception from specialist execution. |

### Why Inversion Works

Inversion is not just "consider the opposite." It's a specific cognitive operation:

**Step 1: Surface the hidden assumption.** The most powerful inversions flip assumptions that are so deeply held they're invisible. "Resources are scarce" isn't something you consciously think — it's the water you swim in. The first job is to *name* the assumption.

**Step 2: Flip it.** Not randomly — structurally. The inversion must produce a statement that is *grammatically coherent and logically possible*, even if it seems absurd. "Resources are abundant" is coherent. "Governance is soil" is coherent. "Cats are triangles" is not — it's a category error, not an inversion.

**Step 3: Ask "in what world is this true?"** This is the critical step. Don't ask "is this true?" (it probably isn't, in the current world). Ask "what would have to be true for this to work?" The answer constructs a new possibility space.

**Step 4: Import the insight back.** If the inverted world has properties that partially apply to the current situation, you've found something new. The insight is always at the *boundary* between the two worlds — not fully in either.

### What Makes Inversion Different from Other Collision Types

| Collision Type | What It Does | What It Produces |
|---------------|-------------|-----------------|
| **Dialectic** | Two ideas that contradict each other are forced into the same frame | Synthesis (a third position that resolves the contradiction) |
| **Analogical** | An idea from domain A is mapped onto domain B | Transfer (a pattern that works in both domains) |
| **Inversion** | An assumption is flipped to its structural opposite | *Visibility* (something that was invisible becomes seeable) |
| **Scale** | An idea is applied at a different magnitude | Fracture or fractal (what holds, what breaks, what repeats) |
| **Temporal** | An idea from the past meets the present | Evolution (what mutated, what persisted, what died) |
| **Archetypal** | An idea is run through multiple cognitive lenses | Depth (the same idea seen from logic, myth, bridge, pattern) |

Inversion is unique because it doesn't produce a *new* idea — it makes an *existing but invisible* idea visible. The other collision types generate; inversion *reveals*. This is why every session insight came from inversion: the ideas were already there, hidden behind their own assumptions.

### The Inversion Protocol (Formal)

```
INVERSION PROTOCOL v0.1
Materia Collider — Primary Experimental Method

INPUT: Any statement, assumption, belief, constraint, or design decision.

PHASE 1: EXCAVATION
  Goal: Surface the hidden assumptions behind the input.
  Method: Ask "what must be true for this to make sense?"
  Output: 3-5 assumptions, ranked by how invisible they are
          (most invisible = most powerful to invert).

PHASE 2: SELECTION
  Goal: Choose the assumption to invert.
  Criteria:
    - Invisibility: how deeply held? (deeper = more powerful)
    - Structural load: how much of the system rests on this assumption?
      (more load = more disruptive inversion)
    - Coherence: does flipping it produce a grammatically/logically
      coherent alternative? (incoherent inversions are category errors,
      not insights)

PHASE 3: INVERSION
  Goal: Flip the selected assumption.
  Method: Negate the core verb or reverse the core relationship.
    "X constrains Y" → "X enables Y"
    "We need X" → "X is what we need to eliminate"
    "X is scarce" → "X is abundant"
    "X comes before Y" → "Y comes before X"
    "X serves Y" → "Y serves X"
  Output: The inverted statement, stated plainly.

PHASE 4: WORLD-BUILDING
  Goal: Construct the world in which the inversion is true.
  Method: Ask "what would have to be true for this to work?"
  Output: 3-5 conditions that would make the inverted world function.

  Critical: This is NOT about whether the inverted world is realistic.
  It's about what it *reveals*. Even a fantastical inverted world has
  properties that illuminate the original.

PHASE 5: IMPORT
  Goal: Bring insights from the inverted world back into the original.
  Method: For each condition identified in Phase 4, ask:
    - Does this partially apply to our current situation?
    - What would change if we acted as though it were true?
    - What becomes visible from this angle that was invisible before?
  Output: 0-3 actionable insights. (Zero is valid — not every
  inversion produces usable material. The collider doesn't guarantee
  results; it guarantees the experiment was run.)

PHASE 6: OBSERVATION (optional, for recursive improvement)
  Goal: Record what the inversion produced.
  Method: Log:
    - The original assumption
    - The inversion
    - What became visible
    - Whether it produced an actionable insight
    - Whether it changed the system's understanding of itself
  Over time, patterns emerge: which types of assumptions produce the
  most powerful inversions? Which domains are most inversion-rich?
```

### Running the Protocol: A Worked Example

**Input**: "Skills need to be broad to be useful across many contexts."

**Phase 1 (Excavation)**:
- Assumption: Breadth equals utility
- Assumption: The same skill will be used in many different contexts
- Assumption: A narrow skill would be useless outside its specific domain
- Assumption: The director needs flexible tools, not rigid ones

**Phase 2 (Selection)**: "Breadth equals utility" — deeply held, high structural load (it shaped how all 70+ skills were designed), and the inversion is coherent.

**Phase 3 (Inversion)**: "Depth equals utility. A skill that knows *everything* about one narrow domain is more useful than a skill that knows *a little* about many domains."

**Phase 4 (World-building)**: What would have to be true?
- The director would need to be able to summon the *exact right* narrow specialist for any situation (intent-routing solved)
- There would need to be *many* narrow specialists, not a few broad ones (large skill library, >200?)
- Each specialist would need to include its complete domain corpus (deep references/)
- A specialist that doesn't match any current need would cost nothing to maintain (unlike a hired employee)

**Phase 5 (Import)**:
- The resource inversion makes condition 4 true: idle specialists cost nothing (unlike human employees who draw salary)
- Condition 1 is the "intent-routing" problem — not yet solved, but solvable
- Condition 3 is the skill-depth gap identified in the assessment — skills need 10-20x deeper references
- **Actionable insight**: The skill library should evolve toward *many narrow specialists* rather than *few broad guides*. This is the opposite of the current trajectory. Current skills try to cover broad domains (security-implementation-guide covers all of security). The specialist model says: split that into `security-policy-writer`, `threat-model-analyst`, `penetration-test-planner`, `incident-response-drafter` — each one a complete corpus expert in exactly one artifact type.

**Phase 6 (Observation)**: This inversion produced a concrete architectural direction for the skill library. The original assumption ("broad is useful") was invisible because it mirrors how human generalists work. The inversion reveals that AI specialists have different economics — depth is free, breadth is a context-window tax.

### Types of Inversion (Taxonomy)

Not all inversions flip the same structure. Naming the types makes the protocol more precise:

| Type | What Gets Flipped | Example |
|------|-------------------|---------|
| **Constraint inversion** | A limitation becomes an advantage | "Scarce resources" → "Abundant resources" |
| **Direction inversion** | The flow reverses | "Ideas are assigned to categories" → "Ideas find their own habitat" |
| **Role inversion** | Who does what swaps | "Director assembles context" → "Specialist arrives pre-loaded with context" |
| **Value inversion** | What's valued is devalued, and vice versa | "Breadth is useful" → "Depth is useful" |
| **Absence inversion** | What's missing is the most important thing | "We need more structure" → "We need an unstructured space" |
| **Temporal inversion** | The sequence reverses | "Build the tool, then define the SOP" → "Define when each tool becomes necessary, then build on demand" |
| **Relationship inversion** | The relationship between two things flips | "Governance constrains growth" → "Governance enables growth" |

### Open Questions About the Protocol

1. **Can it be automated?** Phase 1 (excavation) seems like something an AI could assist with — "surface the hidden assumptions behind this statement." But Phase 2 (selection) requires the director's judgment about which assumption is most invisible. And Phase 5 (import) requires the director's knowledge of the current system to know what "partially applies." The protocol may be inherently hybrid: AI-assisted excavation, director-led selection and import.

2. **Does the protocol need an adversary?** In dialectic collision, you have two opposing ideas. In inversion, you have an idea and its negation. But who advocates for the negation? Does the protocol need a "Devil's Advocate" role — a specialist whose job is to argue for the inverted world's validity?

3. **How do you prevent trivial inversions?** "The sky is blue" → "The sky is not blue" produces nothing useful. The Phase 2 criteria (invisibility, structural load, coherence) are meant to filter these out, but they may need refinement. What makes an assumption *worth* inverting?

4. **Recursive inversions**: Can you invert an inversion? "Governance constrains" → "Governance enables" → "Governance enables constraints" (governance provides the right limitations at the right time). Triple inversions may produce increasingly subtle insights, or they may produce noise. Needs experimentation.

5. **Inversion exhaustion**: Does a system eventually run out of invertible assumptions? Or does each inversion reveal new assumptions that weren't visible before, creating an infinite well?

---

## The Missing Piece: Agentic Titan as Materia Manipulator

**This changes everything.**

`organvm-iv-taxis/agentic-titan` is a **polymorphic, model-agnostic multi-agent orchestration framework** with:

- **22 agent archetypes** (researcher, reviewer, coder, security_analyst, product_manager, data_engineer, devops, cfo, orchestrator, jury, dao, bureaucracy, government, cell, eusocial, swarm_intelligence, actor_network, assemblage, paper2code...)
- **9 topology patterns** (swarm, hierarchy, pipeline, mesh, ring, star, rhizomatic, fission-fusion, stigmergic)
- **Runtime topology switching** — the system can change coordination patterns mid-task based on task analysis
- **Model-agnostic adapter layer** — routes to Ollama, Anthropic, OpenAI, Groq based on strategy (cost, quality, speed, cognitive-task-aware)
- **Hive Mind layer** — Redis state + ChromaDB vectors for shared memory
- **Safety & governance** — human-in-the-loop approval gates, RBAC, budget enforcement, audit logging
- **1,312 tests passing**, production-hardened
- **Criticality detection** based on statistical physics (monitors the "edge of chaos" in agent networks)
- An `absorb-alchemize/` directory that already contains the Expansive Inquiry System (`expand_AI_inquiry.jsx` and `.txt`)

**The 22 archetypes ARE the specialists.** The jury archetype. The researcher archetype. The security_analyst archetype. The reviewer archetype. These are exactly what the director/specialist model describes — archetypal roles that know their domain.

**The 9 topologies ARE the collision methods.** A swarm topology = parallel brainstorming. A pipeline = sequential staged inquiry (like the Expansive Inquiry System's 6 stages). A ring = consensus/voting. Fission-fusion = ideas splitting into independent clusters and reconverging. Stigmergic = ideas leaving traces that other ideas follow. Rhizomatic = lateral, non-hierarchical connections.

**`absorb-alchemize/` IS the proto-collider.** It already contains the Expansive Inquiry System alongside research prompts, architectural synthesis docs, and pattern documents. The name itself — "absorb-alchemize" — describes exactly what the collider does: absorb raw material, alchemize it into something new.

### The Architecture Becomes Clear

```
DIRECTOR (you)
    ↓ intent
MATERIA-COLLIDER (meta-organvm/)
    │ pre-codified space — ideas in their raw form
    │ collision protocols (inversion, dialectic, analogical...)
    ↓ fuel (ideas ready for manipulation)
AGENTIC TITAN (organvm-iv-taxis/)
    │ the manipulators — 22 archetypes × 9 topologies
    │ model-agnostic execution across providers
    │ runtime topology switching based on task analysis
    ↓ artifacts
ORGANS (I through VII + META)
    │ the habitats — ideas rooted in their natural ecosystem
    │ governed by promotion ladder, seed.yaml, CI gates
    ↓ products, art, theory, community, distribution
THE WORLD
```

The materia-collider is **upstream** of Agentic Titan. The collider holds raw ideas and experimental protocols. Titan's archetypes and topologies are the mechanisms that *process* those ideas into structured artifacts. The organs receive the results.

### What This Means for the Collider

The collider doesn't need to implement its own specialist archetypes or coordination patterns — **those already exist in Titan**. The collider needs to:

1. **Hold raw material** (the pre-codified space function)
2. **Define collision protocols** (inversion, dialectic, etc.) as high-level experimental designs
3. **Express protocols as Titan workflow specifications** — a collision protocol translates into a Titan DAG: which archetypes participate, which topology to use, what the success criteria are
4. **Receive and store experimental results** — the output of Titan executions, before they graduate to organs

The inversion protocol, for instance, would map to Titan like this:

```
INVERSION PROTOCOL → TITAN WORKFLOW
Phase 1 (Excavation) → researcher archetype, swarm topology
                        (multiple researchers surface hidden assumptions)
Phase 2 (Selection) → DIRECTOR (human-in-the-loop gate)
                        (director chooses which assumption to invert)
Phase 3 (Inversion) → researcher archetype, pipeline topology
                        (sequential: negate, articulate, validate coherence)
Phase 4 (World-building) → researcher + product_manager, fission-fusion
                        (explore independently, reconverge with conditions)
Phase 5 (Import) → DIRECTOR (human-in-the-loop gate)
                        (director imports insights back to current system)
Phase 6 (Observation) → data_engineer archetype
                        (log results, detect patterns across inversions)
```

### The Expansive Inquiry System → Titan Workflow

The 6-stage pipeline from the Expansive Inquiry System maps directly:

```
Scope AI     → researcher archetype, pipeline stage 1
Logic AI     → researcher archetype (analytic variant), pipeline stage 2
Mythos AI    → researcher archetype (mythic variant), pipeline stage 3
Bridge AI    → researcher archetype (lateral variant), pipeline stage 4
Meta AI      → orchestrator archetype, pipeline stage 5
Pattern AI   → data_engineer archetype, pipeline stage 6
```

But Titan enables what the Expansive Inquiry System couldn't: **topology switching mid-inquiry**. Logic and Mythos could run in parallel (swarm), then converge via ring (consensus on contradictions), then Meta runs stigmergically (leaving traces for Pattern to follow).

### Resolved Questions

**1. What is the materia-collider's relationship to `absorb-alchemize/`?**

`absorb-alchemize/` is the collider's **theoretical library** — not the collider itself. It contains the *science* of assembly: morphodynamics of organizational bodies (from cosmic accretion to cancer as cellular rebellion), modular synthesis as an architectural metaphor, the Expansive Inquiry System prototype. This is reference material that informs HOW the collider works.

The collider itself sits upstream in `meta-organvm/` because it serves ALL organs, not just Titan. `absorb-alchemize/` stays where it is — it's Titan's own research corpus. The collider *references* it but doesn't absorb it. The relationship:

```
absorb-alchemize/ (Titan's theoretical library — HOW agents assemble)
    ↑ informs
materia-collider/ (the experimental space — WHERE ideas collide)
    ↓ feeds
agentic-titan/ (the execution engine — WHAT manipulates the ideas)
```

**2. How does the director interface with Titan?**

Two modes, not one:

- **Safety HITL** (existing): binary approve/reject gates for high-risk agent actions. This stays as-is.
- **Creative HITL** (needed): open-ended directorial input at decision points. Not "approve this action" but "choose which assumption to invert" or "this idea is ready to root — where?" This is the director's creative contribution, which no agent can replace.

The Creative HITL is the key interface between the director and the specialist engine. It's where the dream-state meets the wake-state. Titan already has the infrastructure for pause-and-wait-for-human-input; it just needs a mode that expects creative direction rather than yes/no.

**3. Do collision protocols need to be formal Titan workflow specs?**

**Both.** This is the spectrum:

- **Lightweight collisions** (bench-level): The director jots a one-paragraph inversion on the bench. No Titan involvement. Just a note in the collider, maybe cross-referenced to another note. This is the unstructured, dream-state work.
- **Medium collisions** (directed exploration): The director picks 2-3 ideas from the bench and says "collide these." A single Titan archetype (researcher, likely) runs a focused exploration. Results go back to the bench.
- **Heavy collisions** (full protocol): The director triggers a formal inversion or archetypal collision. Titan spins up multiple archetypes across topologies, runs the full protocol, returns structured results. This is the wake-state machinery at full power.

The collider must support all three weights. Its value is in the RANGE — from napkin sketch to orchestrated experiment. If it only works at full Titan scale, it's too heavy for dream-state thinking. If it only works at napkin scale, it can't leverage the 22 archetypes.

**4. The skill library vs. Titan archetypes — convergence?**

They serve different execution contexts and should remain separate but **mutually informed**:

| Aspect | Skills (`a-i--skills/`) | Archetypes (Titan `agents/archetypes/`) |
|--------|------------------------|-----------------------------------------|
| Runtime | Claude Code sessions (human-interactive) | Titan orchestrator (multi-agent automated) |
| Language | Markdown prompts + references | Python classes (BaseAgent subclasses) |
| Interface | Director invokes `/skill-name` | Titan workflow DAG assigns archetypes |
| Depth | Currently shallow (prompt wrappers) | Currently general-purpose (4-step research pattern) |
| State | Stateless (each invocation starts fresh) | Stateful (hive mind, shared memory) |

**Neither is deep enough yet** to be the "historically complete corpus expert." The path to depth:

- **Skills** should grow deeper references/ (10-20 per skill, not 2-3) and narrower scope (one skill per artifact type)
- **Archetypes** should grow domain-specific variants (not just "researcher" but "financial-compliance-researcher", "behavioral-science-researcher")
- **Cross-pollination**: when a skill accumulates deep references/, that corpus should be available to the corresponding Titan archetype. When a Titan archetype develops institutional memory through hive mind interactions, that knowledge should feed back into the skill's references/

They don't converge into one thing. They're the same specialist wearing different clothes for different contexts — a prompt-mode outfit for Claude Code sessions, a Python-class outfit for Titan orchestrations. The knowledge corpus should be shared.

**5. Doc 12 update**

Yes. `12-habitat-governance-lifecycle.md` should be updated to reference:

- **Pre-LOCAL**: the materia-collider. Ideas live here before they even become LOCAL repos. The collider is the anteroom to the promotion ladder.
- **Processing**: Agentic Titan as the machinery that transforms collider output into organ-ready artifacts.
- **The director's role at each stage**: not executing, but sensing, selecting, and directing.

---

## Implementation Plan: Create the Materia Collider

### Step 1: Create the repo directory and founding artifact

**Location**: `/Users/4jp/Workspace/meta-organvm/materia-collider/`

**Directory structure**:
```
materia-collider/
├── README.md                    # What this is, the architecture map, how to use it
├── CLAUDE.md                    # AI agent context for the collider
├── seed.yaml                    # ORGANVM contract (meta-organvm, standard, LOCAL)
├── genesis/                     # Founding documents
│   └── 2026-03-06-synthesis--director-habitat-specialist-collider.md
│                                  ↑ THIS DOCUMENT (the plan file content)
├── protocols/                   # Collision methods
│   └── inversion-v0.1.md        # The inversion protocol (from this document)
├── bench/                       # The workshop bench — raw ideas, no structure enforced
│   └── .gitkeep
├── experiments/                 # Dated collision results
│   └── .gitkeep
└── observations/                # Pattern analysis across experiments
    └── .gitkeep
```

**Anti-governance**: The `bench/` directory has NO naming conventions, no structure requirements, no promotion criteria. Files can be anything — a sentence, a paragraph, a diagram, a link. The only rule: if something graduates from the bench to an organ, leave a breadcrumb (a line in the file noting where it went and when).

### Step 2: Write the README

Content:
- What the materia-collider is (pre-codified space + experimental apparatus + specialist forge)
- The architecture map (collider → Titan → organs)
- The three collision weights (lightweight/medium/heavy)
- How to use the bench (just put things there)
- How to run a protocol (read the protocol doc, follow the phases)
- Relationship to `intake/` (intake is fuel, collider is the accelerator)
- Relationship to `absorb-alchemize/` (Titan's theoretical library informs the collider's methods)

### Step 3: Write the seed.yaml

```yaml
schema_version: "1.0"
organ: META
organ_name: Meta
repo: materia-collider
org: meta-organvm
metadata:
  implementation_status: ACTIVE
  tier: standard
  promotion_status: LOCAL
  last_validated: "2026-03-06"
  language: markdown
  tags: [experimental, pre-codified, collision-protocols, idea-generation]
produces:
  - type: experimental_output
    description: "Raw ideas, collision results, and specialist archetype seeds"
    consumers: [all-organs]
consumes:
  - type: raw_material
    source: intake/
    description: "Unstructured ideas and external material as collision fuel"
  - type: theoretical_library
    source: organvm-iv-taxis/agentic-titan/absorb-alchemize/
    description: "Assembly theory and morphodynamics informing collision methods"
```

### Step 4: Extract the inversion protocol into its own file

Take the formal protocol from this document (Phases 1-6 + taxonomy of inversion types + worked example) and place it in `protocols/inversion-v0.1.md`.

### Step 5: Write CLAUDE.md

Brief context for AI agents working in the collider:
- This is a pre-codified space — structure is minimal by design
- The bench/ directory is intentionally unstructured
- Protocols in protocols/ are experimental methods, not governance
- Results go in experiments/ with date prefixes
- Nothing here is canonical until it graduates to an organ

### Step 6: Update doc 12

Edit `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/standards/12-habitat-governance-lifecycle.md` to add:
- A "Pre-LOCAL: The Materia Collider" section before the LOCAL stage
- Reference to Titan as the processing engine between collider and organs
- The director's role at each stage

### Step 7: Copy founding synthesis to genesis/

Copy the content of this plan file into `genesis/2026-03-06-synthesis--director-habitat-specialist-collider.md` as the collider's founding document — the full thinking arc that produced it.

### Files to create/modify

| # | File | Action |
|---|------|--------|
| 1 | `meta-organvm/materia-collider/README.md` | Create |
| 2 | `meta-organvm/materia-collider/CLAUDE.md` | Create |
| 3 | `meta-organvm/materia-collider/seed.yaml` | Create |
| 4 | `meta-organvm/materia-collider/genesis/2026-03-06-synthesis--director-habitat-specialist-collider.md` | Create (from plan file) |
| 5 | `meta-organvm/materia-collider/protocols/inversion-v0.1.md` | Create (extracted from synthesis) |
| 6 | `meta-organvm/materia-collider/bench/.gitkeep` | Create |
| 7 | `meta-organvm/materia-collider/experiments/.gitkeep` | Create |
| 8 | `meta-organvm/materia-collider/observations/.gitkeep` | Create |
| 9 | `meta-organvm/organvm-corpvs-testamentvm/docs/standards/12-habitat-governance-lifecycle.md` | Update (add pre-LOCAL section) |

### Verification

1. `cd meta-organvm/materia-collider && git init` — repo initializes cleanly
2. All markdown files have valid headings and no broken internal links
3. seed.yaml is valid YAML with correct schema
4. Doc 12 still reads coherently with the new pre-LOCAL section
5. The bench/ directory is genuinely empty (only .gitkeep) — proving the anti-governance principle

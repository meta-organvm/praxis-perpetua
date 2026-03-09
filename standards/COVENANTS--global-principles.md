# COVENANTS: Global Principles of the ORGANVM System

These covenants represent the internalized wisdom of the ORGANVM fleet. They are immutable operational standards that govern all sessions across all 8 organs.

## 1. Ship Speed Over Ship Perfection (`biz.ship_speed`)
**Domain:** Business
**Principle:** A shipped imperfect product beats an unshipped perfect one.
**Application:** Deliver functional increments early and often. Avoid stalling in the PROVE phase for minor aesthetic or non-functional polish if the core logic is verified.

## 2. Design for Idempotency (`practice.idempotency`)
**Domain:** Engineering
**Principle:** Operations should be safe to retry without side effects.
**Application:** All scripts, automation, and data transformations must be designed so that multiple executions produce the same result as a single execution.

## 3. Avoid Big Bang Integration (`antipattern.big_bang`)
**Domain:** Engineering
**Principle:** Integrate incrementally, not all at once.
**Application:** Break down large features into smaller, testable modules. Merge frequently into the `main` branch of sub-repos.

## 4. Feature Flags for Safe Rollout (`practice.feature_flags`)
**Domain:** Engineering
**Principle:** Decouple deployment from release using feature flags.
**Application:** Use conditional logic to guard new features, allowing them to be deployed to production but activated only when ready.

## 5. Navigate Between Scylla and Charybdis (`phil.scylla_charybdis`)
**Domain:** Philosophical
**Principle:** Steer between the twin perils — recklessness and paralysis.
**Application:** Maintain high velocity without sacrificing technical integrity. Use the FRAME and SHAPE phases to identify risks before they become blockers.

## 6. Logical Consistency (`logical_consistency`)
**Domain:** Engineering
**Principle:** The tools must verify themselves against their environment.
**Application:** Every automated process should include a pre-flight check to ensure environmental variables, dependencies, and filesystem paths are consistent with expectations.

## 7. Quality Over Quantity (`quality_over_quantity`)
**Domain:** Philosophical
**Principle:** Prioritize the integrity of the system over the volume of artifacts.
**Application:** It is better to have 10 fully graduated, high-quality repositories than 100 repositories stuck in an unverified CANDIDATE state.

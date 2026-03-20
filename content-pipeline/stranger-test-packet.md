# ORGANVM Stranger Test — Participant Packet

> **You received this because someone asked you to help test whether their software system makes sense to an outsider. This takes about 30-45 minutes. You do not need to install anything or write any code.**

---

## Who sent you this

A solo developer/artist building a large-scale creative-institutional system called ORGANVM. It spans over 100 GitHub repositories organized into 8 functional groups ("organs") covering theory, art, commerce, orchestration, discourse, community, distribution, and meta-governance. The whole thing is built and maintained by one person using AI-assisted automation.

They need to know: **can someone who has never seen this before figure out what it is and navigate it?**

Your honest answers -- including confusion, frustration, and dead ends -- are the most valuable data. There are no wrong answers. Getting stuck is not failure; it tells them exactly where the documentation needs work.

## What you need

- A web browser (Chrome, Firefox, Safari -- anything)
- About 30-45 minutes of uninterrupted time
- This document open for reference

You will NOT need: a terminal, git, any programming tools, or any accounts.

## How this works

You will complete 5 short tasks, each with a time limit. For each task, write your answer in the space provided (or in a separate doc, email, whatever is easiest). After the tasks, there is a brief feedback section.

**Rules:**
- Use only what you can find through public web pages: GitHub repos, READMEs, linked websites
- Do not Google "ORGANVM" or search for external explanations -- the test is whether the system explains itself
- If you are stuck on a task after the time limit, write what you tried and move on
- Getting stuck is data, not failure

---

## The Tasks

### Task 1: What is this thing? (10 minutes)

Go to **https://github.com/meta-organvm**

Look around. Click into repos. Read what you find.

**Question:** What is this system and what is it for? Write 2-3 sentences.

```
YOUR ANSWER:




```

---

### Task 2: Find the commerce flagship (8 minutes)

The system has 8 "organs." ORGAN-III is the commerce organ -- it contains commercial products and developer tools. Its GitHub organization is called **labores-profani-crux** (you can find it linked from what you already explored, or go to https://github.com/labores-profani-crux).

**Question:** Find the most important repository in this organ. What is it called, and what does it do? Write 1-2 sentences.

```
YOUR ANSWER:




```

---

### Task 3: Find the rules (10 minutes)

The system has rules about which organs can depend on which other organs. These rules should be findable somewhere in the documentation you have already been exploring.

**Question:** What is the key dependency rule? Explain it in one sentence.

```
YOUR ANSWER:




```

---

### Task 4: Find a specific essay (6 minutes)

The system includes essays published on a blog. The blog is run by ORGAN-V (the discourse organ).

Start from: **https://organvm-v-logos.github.io/public-process/**

**Question:** Find an essay that discusses AI transparency, honesty, or how the system was built. What is its title?

```
YOUR ANSWER:




```

---

### Task 5: Is this system alive? (12 minutes)

Look at whatever you have already seen, or explore further. Consider things like: when was the last commit? Are there CI badges? Does the documentation look maintained or abandoned? Are there deployed websites that actually work?

Here are some additional live URLs you can check:
- Portfolio: https://4444j99.github.io/portfolio/
- Stakeholder portal: https://stakeholder-portal-ten.vercel.app/
- Constitutional corpus: https://stakeholder-portal-ten.vercel.app/constitution

**Question:** Does this system seem healthy and actively maintained, or does it seem abandoned? Give 3 specific pieces of evidence for your assessment.

```
YOUR ANSWER:

1.

2.

3.

```

---

## Feedback

You are done with the tasks. Now tell them what the experience was actually like.

### Rate each from 1 to 5

| Question | Your Rating (1-5) |
|----------|-------------------|
| How clear was the system's purpose? (1 = completely unclear, 5 = immediately obvious) | |
| How easy was it to find things? (1 = lost the whole time, 5 = intuitive navigation) | |
| How well-written were the docs you read? (1 = confusing, 5 = excellent) | |
| Did the system feel like one coordinated thing, or a pile of unrelated repos? (1 = scattered, 5 = clearly coordinated) | |
| Does this seem like a real, maintained project? (1 = seems abandoned or fake, 5 = clearly real and active) | |

### Open-ended (write as much or as little as you want)

**What was the single most confusing thing you encountered?**
```



```

**What would have helped you most in the first 5 minutes?**
```



```

**If you had to explain this system to a colleague in one sentence, what would you say?**
```



```

**Would you star, fork, or bookmark any of the repos you saw? Which ones and why?**
```



```

**Anything else -- frustrations, observations, suggestions?**
```



```

---

## How to return your results

Send this document back (filled in) to whoever gave it to you. Email, DM, shared doc -- whatever works. If you want, you can also just take a photo of handwritten notes. The format does not matter; the content does.

**Thank you.** This kind of honest external feedback is extremely hard to get as a solo builder, and it directly shapes what gets improved next.

---

---

# FACILITATOR SECTION

> **Everything below this line is for the person administering the test. Do not share it with the participant.**

---

## Scoring Rubric

Each task has 3 criteria worth 1 point each. There is also a 1-point time bonus per task completed within the limit. Total possible: 20 points.

### Task 1: What is this thing? (3 points + 1 time bonus)

| Criterion | 1 point if... | 0 points if... |
|-----------|---------------|----------------|
| Multi-repo awareness | Mentions that it spans multiple repos, orgs, or "organs" | Describes it as a single app or library |
| Domain breadth | Mentions at least 2 of: theory, art, commerce, governance, community | Only identifies one domain or none |
| Not a single product | Understands it is a system/framework/infrastructure, not one application | Thinks it is a single tool or product |
| TIME BONUS | Completed within 10 minutes | Exceeded 10 minutes |

**Partial credit guidance:** If they get the general shape ("a system of repos for different purposes") but miss the organ metaphor, give 2/3.

### Task 2: Find the commerce flagship (3 points + 1 time bonus)

| Criterion | 1 point if... | 0 points if... |
|-----------|---------------|----------------|
| Found the org | Navigated to labores-profani-crux (ORGAN-III's GitHub org) | Never found the right organization |
| Identified flagship | Named `public-record-data-scrapper` (or the repo marked as flagship/highest tier) | Named a different repo or could not identify one |
| Described it | Gave a roughly accurate description of what the repo does | Description is wrong or absent |
| TIME BONUS | Completed within 8 minutes | Exceeded 8 minutes |

**Partial credit guidance:** If they find the org but pick a different repo and explain it well, give 2/3. If they find the right repo but cannot explain it, give 2/3.

### Task 3: Find the rules (3 points + 1 time bonus)

| Criterion | 1 point if... | 0 points if... |
|-----------|---------------|----------------|
| Found governance docs | Located governance-rules.json, a README section, or orchestration docs describing dependencies | Could not find any mention of dependency rules |
| Stated the rule | Correctly says something like "data flows I to II to III, not backwards" or "no reverse dependencies" | States a rule that is wrong or unrelated |
| Understood scope | Recognizes that ORGAN-IV+ is not restricted the same way, or that the rule applies to the core creative pipeline | Thinks the rule applies uniformly to all organs |
| TIME BONUS | Completed within 10 minutes | Exceeded 10 minutes |

**Partial credit guidance:** If they find that dependencies exist but get the direction wrong, give 1/3. If they state the rule correctly but did not find the original source document, give 2/3 (the documentation led them to the right answer regardless).

### Task 4: Find a specific essay (3 points + 1 time bonus)

| Criterion | 1 point if... | 0 points if... |
|-----------|---------------|----------------|
| Found the blog | Navigated to the public-process blog or _posts directory | Never found the essays |
| Found a relevant essay | Identified an essay about transparency, honesty, AI usage, or building in public | Found an unrelated essay or none |
| Provided title or URL | Gave the essay title, filename, or URL | Could not specify which essay |
| TIME BONUS | Completed within 6 minutes | Exceeded 6 minutes |

**Partial credit guidance:** If they find the blog but pick an essay that is adjacent (e.g., about methodology rather than transparency), give 2/3 if their reasoning is sound.

### Task 5: Is this system alive? (3 points + 1 time bonus)

| Criterion | 1 point if... | 0 points if... |
|-----------|---------------|----------------|
| 3 observations | Provides at least 3 specific, concrete observations | Fewer than 3 observations, or only vague impressions |
| Evidence-based | Observations cite specific things (dates, badge colors, page content, commit counts) | Observations are general feelings without specifics |
| Accurate | The cited evidence is factually correct (dates are real, statuses are real) | Evidence is misread or fabricated |
| TIME BONUS | Completed within 12 minutes | Exceeded 12 minutes |

**Partial credit guidance:** 2 solid observations with good evidence = 2/3. 3 observations but one is inaccurate = 2/3.

---

## Score Summary Sheet

Fill this in after reviewing the participant's responses.

```
Participant pseudonym: _______________
Date: _______________
Participant profile (role, years experience): _______________

TASK SCORES
                        Criteria    Time Bonus    Total
Task 1 (purpose):       __ / 3      __ / 1       __ / 4
Task 2 (flagship):      __ / 3      __ / 1       __ / 4
Task 3 (rules):         __ / 3      __ / 1       __ / 4
Task 4 (essay):         __ / 3      __ / 1       __ / 4
Task 5 (health):        __ / 3      __ / 1       __ / 4
                                                 --------
TOTAL:                                            __ / 20

THRESHOLD:
  16-20  PASS              --> Omega #2 = MET
  11-15  PASS WITH NOTES   --> Omega #2 = MET (with remediation items)
  6-10   MARGINAL          --> Omega #2 = NOT MET (fix docs, retest)
  0-5    FAIL              --> Omega #2 = NOT MET (major rework needed)

OMEGA #2 RESULT:  [ ] MET   [ ] NOT MET
```

### Omega Criterion #2 Threshold

The omega scorecard requires "Stranger test score >= 80%." On a 20-point scale, 80% = 16 points. A score of 16 or above means criterion #2 is MET. A score of 11-15 (PASS WITH NOTES) also counts as MET for the omega scorecard, since the system is navigable even if specific improvements are needed.

---

## Structured Feedback Summary

```
CLARITY:          __ / 5
NAVIGATION:       __ / 5
DOC QUALITY:      __ / 5
COHERENCE:        __ / 5
CREDIBILITY:      __ / 5
FEEDBACK TOTAL:   __ / 25

Biggest friction point:
_______________________________________________

First-5-minutes gap:
_______________________________________________

One-sentence summary (participant's words):
_______________________________________________

Would bookmark (repos + reasons):
_______________________________________________
```

---

## Post-Test Actions

1. Record the score in `organvm-corpvs-testamentvm/data/omega/` as a dated JSON file
2. If score >= 16: flip omega criterion #2 to MET in `organvm-engine/src/organvm_engine/omega/scorecard.py` (add `2` to `_KNOWN_MET`)
3. If score < 16: create GitHub issues for each recommended documentation improvement, tagged `omega`, `stranger-test`
4. File the completed scoring sheet in `praxis-perpetua/sessions/` with date prefix
5. Update the stranger-test-protocol SOP with any procedural lessons learned

---

## Reference: Live System URLs

These are the publicly accessible entry points as of 2026-03-19:

| System | URL | What it shows |
|--------|-----|---------------|
| Meta org (GitHub) | https://github.com/meta-organvm | Starting point, org profile, repo list |
| ORGAN-III org | https://github.com/labores-profani-crux | Commerce organ repos |
| Essays blog | https://organvm-v-logos.github.io/public-process/ | Published essays (49+) |
| Portfolio site | https://4444j99.github.io/portfolio/ | Curated project showcase, omega scorecard |
| Stakeholder portal | https://stakeholder-portal-ten.vercel.app/ | AI-powered system browser |
| Constitutional corpus | https://stakeholder-portal-ten.vercel.app/constitution | Governance axioms, spec ladder |

---

## Reference: Source Documents

This packet was assembled from:
- `praxis-perpetua/standards/SOP--stranger-test-protocol.md` (canonical SOP)
- `organvm-corpvs-testamentvm/docs/operations/stranger-test-protocol.md` (original protocol)
- `organvm-corpvs-testamentvm/docs/operations/stranger-test-handout.md` (original participant handout)
- `praxis-perpetua/standards/stranger-test-packet.md` (evaluator-oriented packet)
- `organvm-engine/src/organvm_engine/omega/scorecard.py` (criterion #2 definition)

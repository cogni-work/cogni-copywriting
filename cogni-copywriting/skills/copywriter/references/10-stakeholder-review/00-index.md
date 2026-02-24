---
title: Stakeholder Review System
type: index
version: 1.0
---

# Stakeholder Review System

## Overview

Multi-perspective quality assessment framework that evaluates business documents from different stakeholder viewpoints before final validation. Enables automated feedback collection and synthesis to improve document effectiveness.

## Purpose

**Before this system:** Documents validated only against technical criteria (framework compliance, readability metrics, formatting).

**With this system:** Documents evaluated by simulated stakeholders representing key audience perspectives, ensuring content meets diverse quality expectations.

## Five Core Perspectives

### 1. Executive Review
**Focus:** Decision-readiness, clarity, ROI, time efficiency
**Use when:** Document audience includes C-suite, senior leadership, board members
**File:** `executive-review.md`

### 2. Technical Review
**Focus:** Accuracy, precision, logical consistency, completeness
**Use when:** Document contains technical specifications, implementation details, architecture decisions
**File:** `technical-review.md`

### 3. Legal/Compliance Review
**Focus:** Risk language, regulatory alignment, liability mitigation
**Use when:** Document involves contracts, policies, compliance requirements, vendor agreements
**File:** `legal-review.md`

### 4. Marketing Review
**Focus:** Persuasiveness, audience resonance, brand tone, call-to-action
**Use when:** Document aims to influence, persuade, or promote
**File:** `marketing-review.md`

### 5. End-User Review
**Focus:** Accessibility, plain language, actionability, clarity
**Use when:** Document targets general audiences, customers, non-specialists
**File:** `end-user-review.md`

## Default Stakeholder Selection

Selection based on document audience and deliverable type:

| Audience Parameter | Default Stakeholders |
|-------------------|---------------------|
| `executive` | executive, technical, end-user |
| `technical` | technical, executive |
| `general` | end-user, marketing, executive |
| `legal` | legal, executive, technical |
| `sales/marketing` | marketing, executive, end-user |

**Custom selection:** Override with `stakeholders: [executive, legal, technical]` parameter.

## Review Process

### Phase 6: Stakeholder Review

**For each selected stakeholder:**
1. Load perspective-specific review criteria
2. Evaluate document against weighted checklist (5 criteria per perspective)
3. Assign scores: PASS (100), CONCERN (60), FAIL (0)
4. Calculate weighted overall score (0-100 scale)
5. Generate structured feedback:
   - Strengths (what works well)
   - Concerns (areas needing improvement)
   - Recommendations (specific, actionable improvements)

**Review modes:**
- `automated` (default) - Run checklists without user interaction
- `manual` - Pause for user feedback collection via TodoWrite
- `skip` - Bypass review phases entirely

### Phase 7: Synthesis & Refinement

**Aggregation:**
1. Collect all stakeholder feedback
2. Identify common themes across perspectives
3. Prioritize recommendations:
   - **CRITICAL** - Multiple stakeholders, high-impact, blocks validation
   - **HIGH** - Multiple stakeholders OR high-weight criterion
   - **OPTIONAL** - Single stakeholder, nice-to-have

**Refinement:**
1. Create TodoWrite sub-tasks for critical/high improvements
2. Apply improvements to document
3. Re-evaluate changed sections
4. Calculate synthesis metrics (overall score, applied recommendations)

**File:** `synthesis-guidelines.md`

## Integration with Copywriter Workflow

**8-Phase Workflow:**
1. Parse Parameters & Load References
2. Gather Content Requirements
3. Apply Structure & Framework
4. Apply Writing Principles
5. Apply Impact Techniques (optional)
6. **Stakeholder Review** ← NEW
7. **Synthesis & Refinement** ← NEW
8. Validate & Write Document

**Progressive disclosure:** Stakeholder profiles loaded only in Phase 6, only for selected perspectives.

## Scoring Guidelines

**Per-stakeholder scoring:**
- Each criterion: PASS (100), CONCERN (60), FAIL (0)
- Multiply by criterion weight, sum for total (0-100)
- Threshold: ≥70 considered passing

**Overall synthesis score:**
- Average all stakeholder scores
- Weight by audience (e.g., executive audience → executive score 2x)
- Reported in final JSON output

## Graceful Degradation

**Non-blocking failures:**
- Single stakeholder fails → Continue with remaining stakeholders
- All stakeholders fail → Skip to Phase 8 with `fallback_reason: "review_failure"`
- Synthesis fails → Continue to Phase 8 with original document, `fallback_reason: "synthesis_failure"`
- Improvement application fails → Revert to pre-improvement state, mark skipped

**Philosophy:** Review enhances quality but never blocks document delivery.

## Output Format

**Structured JSON feedback:**
```json
{
  "stakeholder_reviews": [
    {
      "perspective": "executive",
      "score": 85,
      "strengths": ["Clear BLUF", "Strong ROI quantification"],
      "concerns": ["Missing decision timeline"],
      "recommendations": ["CRITICAL: Add explicit decision deadline"]
    },
    {
      "perspective": "technical",
      "score": 78,
      "strengths": ["Accurate technical terminology"],
      "concerns": ["Implementation steps vague", "No risk analysis"],
      "recommendations": ["HIGH: Add technical risk section"]
    }
  ],
  "synthesis": {
    "overall_score": 82,
    "critical_improvements": ["Add decision timeline"],
    "high_improvements": ["Add risk analysis"],
    "optional_improvements": ["Include vendor comparison"],
    "recommendations_applied": true
  }
}
```

## Related Resources

- **Framework patterns:** `references/01-frameworks/*.md`
- **Writing principles:** `references/02-principles/*.md`
- **Impact techniques:** `references/03-impact/*.md`
- **Deliverable templates:** `references/04-deliverables/*.md`


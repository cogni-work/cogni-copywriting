---
title: Multi-Stakeholder Feedback Synthesis
type: process-documentation
version: 1.0
---

# Synthesis Guidelines

## Purpose

Aggregate feedback from multiple stakeholder reviews into prioritized, actionable improvements that enhance document quality without creating analysis paralysis.

**Core principle:** Synthesis transforms diverse feedback into coherent action—identify common themes, resolve conflicts, prioritize by impact.

## Synthesis Process

### Step 1: Collect All Feedback

**Input:** Structured JSON feedback from all completed stakeholder reviews.

**Collect for each stakeholder:**
- Perspective name (executive, technical, legal, marketing, end-user)
- Overall score (0-100)
- Criteria scores (individual dimension scores)
- Strengths (what works well)
- Concerns (areas needing improvement)
- Recommendations (specific, actionable improvements with priority labels)

**Example input:**
```json
[
  {
    "perspective": "executive",
    "score": 78,
    "concerns": ["Missing decision timeline", "ROI not quantified"],
    "recommendations": ["CRITICAL: Add decision deadline", "CRITICAL: Add ROI with timeframe"]
  },
  {
    "perspective": "technical",
    "score": 85,
    "concerns": ["Implementation details vague"],
    "recommendations": ["HIGH: Add technical risk section"]
  },
  {
    "perspective": "end-user",
    "score": 90,
    "concerns": ["Paragraph 3 too dense"],
    "recommendations": ["OPTIONAL: Break paragraph 3 into bullets"]
  }
]
```

---

### Step 2: Identify Common Themes

**Goal:** Find recommendations mentioned by multiple stakeholders to identify high-impact improvements.

**Pattern matching rules:**

| Pattern | Priority | Reasoning |
|---------|----------|-----------|
| **3+ stakeholders mention same issue** | CRITICAL | Impacts effectiveness across multiple perspectives |
| **2 stakeholders mention same issue** | HIGH | Significant quality improvement needed |
| **1 stakeholder mentions issue** | OPTIONAL | Nice-to-have, single-perspective concern |
| **Executive + 1+ other on same issue** | CRITICAL | Decision-maker alignment critical |
| **CRITICAL label from any stakeholder** | CRITICAL | Blocks core deliverable requirements |

**Semantic matching:**
- "Add timeline" = "Include deadline" = "Specify decision date" → Same theme
- "Missing quantification" = "No ROI data" = "Lacks numbers" → Same theme

**Example theme identification:**
```json
{
  "theme": "Missing decision timeline",
  "stakeholders": ["executive", "technical"],
  "priority": "CRITICAL",
  "reasoning": "2 stakeholders + executive perspective"
}
```

---

### Step 3: Prioritize by Impact

**Three priority tiers:**

#### CRITICAL Priority (must address)

**Criteria:**
- Mentioned by multiple stakeholders (2+), OR
- Mentioned by executive + at least one other stakeholder, OR
- Labeled CRITICAL by any stakeholder, OR
- Blocks core deliverable requirements (framework compliance, regulatory, etc.)

**Action:** MUST apply improvement before document finalization.

**Examples:**
- "Add decision timeline" (executive + technical concern)
- "Fix regulatory compliance language" (legal CRITICAL)
- "Quantify ROI" (executive CRITICAL)

---

#### HIGH Priority (should address)

**Criteria:**
- Significant quality improvement across high-weight criteria (≥20% weight), OR
- Mentioned by 2 stakeholders but neither is executive, OR
- Labeled HIGH by any stakeholder, OR
- Feasible within skill constraints (no external data required)

**Action:** Apply if feasible within workflow constraints.

**Examples:**
- "Add risk mitigation section" (technical + legal concern)
- "Strengthen call-to-action" (marketing HIGH)
- "Break dense paragraphs" (end-user + technical concern)

---

#### OPTIONAL Priority (nice-to-have)

**Criteria:**
- Single-stakeholder concern on low-weight criterion (<15% weight), OR
- Labeled OPTIONAL by stakeholder, OR
- Requires external data or out-of-scope changes

**Action:** Log for manual review, do NOT apply automatically.

**Examples:**
- "Add vendor comparison table" (requires external research)
- "Include customer testimonial" (out of scope, no testimonials available)
- "Use more sophisticated vocabulary" (stylistic preference, low impact)

---

### Step 4: Resolve Conflicts

**Common conflicts and resolutions:**

| Conflict | Stakeholders | Resolution | Rationale |
|----------|-------------|------------|-----------|
| **Brevity vs. Detail** | Executive wants concise, Technical wants detail | Executive summary + detailed appendix | Serves both audiences without compromise |
| **Emotion vs. Data** | Marketing wants emotional, Executive wants data | Lead with data, use power words for emphasis | Data credibility + persuasive language |
| **Simplicity vs. Precision** | End-user wants simple, Technical wants precise | Plain language with technical glossary or definitions | Accessibility without sacrificing accuracy |
| **Bold vs. Hedged** | Marketing wants guarantees, Legal wants hedging | Strong but hedged: "designed to deliver" | Confident without over-committing |
| **Clarity vs. Disclosure** | End-user wants simple, Legal wants disclaimers | Main message clear + separate brief disclosure section | Legal protection without burying message |

**Tiebreaker hierarchy:**
1. **Primary audience perspective** - If document is for executives, executive perspective wins
2. **Deliverable requirements** - Core requirements (framework, regulatory) override preferences
3. **Impact techniques effectiveness** - Persuasion and clarity generally prioritized
4. **User-specified preference** - Explicit user parameters override defaults

**Example conflict resolution:**
```
Conflict: Executive wants 1-page memo, Technical wants detailed architecture.
Resolution: 1-page executive memo with link to technical appendix (separate file).
Stakeholder alignment: Executive gets concise document, Technical gets comprehensive detail.
```

---

### Step 5: Apply Improvements

**For each CRITICAL improvement:**
1. Create TodoWrite sub-task: "Apply improvement: [description]"
2. Locate relevant document section
3. Apply change (add, edit, or restructure content)
4. Validate change (re-check criterion that flagged the issue)
5. Mark sub-task complete
6. Update document version

**For each HIGH improvement:**
1. Assess feasibility:
   - ✓ Can be done within skill constraints (no external data, no user input needed)
   - ✓ Doesn't conflict with CRITICAL improvements already applied
   - ✓ Improves document quality measurably
2. If feasible: Apply using same process as CRITICAL
3. If not feasible: Log as skipped with reason

**For each OPTIONAL improvement:**
1. Log in synthesis output for user review
2. Do NOT apply automatically
3. Include in final feedback JSON for manual consideration

**Validation after each improvement:**
- Re-evaluate the specific criterion that flagged the issue
- Verify improvement raised criterion score (60 → 100 or 0 → 60+)
- If score unchanged or decreased, revert change and mark as failed

**Rollback pattern:**
```
1. Save document state before improvement
2. Apply improvement
3. Re-evaluate
4. If score < threshold: Restore saved state, log failure reason
5. If score ≥ threshold: Commit change, proceed
```

---

### Step 6: Calculate Synthesis Metrics

**Metrics to report:**

#### Overall Score
- **Calculation:** Average all stakeholder scores
- **Audience weighting:** If primary audience specified, weight that perspective 2x
  - Example: Executive audience → executive score × 2, others × 1, then average
- **Range:** 0-100

#### Improvement Counts
- **Critical applied:** Count of CRITICAL improvements successfully applied
- **High applied:** Count of HIGH improvements successfully applied
- **Optional logged:** Count of OPTIONAL improvements logged for review
- **Failed:** Count of improvements attempted but reverted (with reasons)

#### Recommendation Application Rate
- **Calculation:** (Critical applied + High applied) / (Total CRITICAL + Total HIGH)
- **Target:** ≥80% (most high-priority recommendations addressed)

**Example synthesis output:**
```json
{
  "overall_score": 84,
  "audience_weighted_score": 86,
  "critical_improvements": [
    "Add decision timeline (March 15, 2025)",
    "Quantify ROI ($340K 3-year ROI, 18-month payback)"
  ],
  "high_improvements": [
    "Add risk mitigation section",
    "Strengthen call-to-action"
  ],
  "optional_improvements": [
    "Add vendor comparison table (requires external research)"
  ],
  "failed_improvements": [],
  "recommendations_applied": true,
  "application_rate": 1.0
}
```

---

## Decision Trees

### Should I apply this recommendation?

```
Is it CRITICAL priority?
├─ YES → Apply immediately, mark as critical improvement
└─ NO → Is it HIGH priority?
    ├─ YES → Is it feasible? (no external data, within scope)
    │   ├─ YES → Apply, mark as high improvement
    │   └─ NO → Skip, log reason
    └─ NO → OPTIONAL → Log for manual review, do NOT apply
```

### How do I resolve conflicting recommendations?

```
Do recommendations conflict?
├─ NO → Apply both
└─ YES → Does one align with primary audience?
    ├─ YES → Prioritize primary audience perspective
    └─ NO → Can both be satisfied with structural solution?
        ├─ YES → Apply structural solution (e.g., summary + appendix)
        └─ NO → Follow tiebreaker hierarchy:
            1. Primary audience
            2. Deliverable requirements
            3. Impact techniques
            4. User-specified preference
```

---

## Example Synthesis Workflow

**Scenario:** Executive memo recommending CRM investment

### Input: Stakeholder Reviews
```json
{
  "executive": {
    "score": 78,
    "concerns": ["Missing timeline", "ROI not quantified"],
    "recommendations": ["CRITICAL: Add decision deadline", "CRITICAL: Quantify ROI with timeframe"]
  },
  "technical": {
    "score": 85,
    "concerns": ["Implementation details vague", "No failure handling"],
    "recommendations": ["HIGH: Add technical risk section", "OPTIONAL: Add architecture diagram"]
  },
  "end-user": {
    "score": 90,
    "concerns": ["Paragraph 3 too dense"],
    "recommendations": ["HIGH: Break paragraph 3 into bullets"]
  }
}
```

### Step 1: Collect Feedback
- 3 stakeholders reviewed
- Scores: Executive 78, Technical 85, End-user 90
- Total recommendations: 5 (2 CRITICAL, 2 HIGH, 1 OPTIONAL)

### Step 2: Identify Common Themes
- **Timeline theme:** Executive CRITICAL (decision deadline)
- **Quantification theme:** Executive CRITICAL (ROI)
- **Clarity theme:** End-user HIGH (paragraph structure)
- **Technical detail theme:** Technical HIGH (risk section)

### Step 3: Prioritize
- **CRITICAL (must apply):** Add timeline, Quantify ROI (both executive CRITICAL)
- **HIGH (should apply):** Add risk section, Break paragraph 3 (both feasible)
- **OPTIONAL (log only):** Add architecture diagram (out of scope)

### Step 4: Resolve Conflicts
- No conflicts detected (all recommendations compatible)

### Step 5: Apply Improvements
1. **Add timeline:**
   - Change: "Please approve this proposal" → "Decision needed by March 15, 2025"
   - Validation: Executive "Decision Clarity" criterion: 60 → 100 ✓
   - Status: Applied

2. **Quantify ROI:**
   - Change: "This will provide strong ROI" → "$340K 3-year ROI with 18-month payback (based on current $120K annual support cost)"
   - Validation: Executive "Quantification" criterion: 60 → 100 ✓
   - Status: Applied

3. **Add risk section:**
   - Change: New section "Key Risks: vendor lock-in (mitigated by annual renewal clause), data migration complexity (estimated 40 hours)"
   - Validation: Technical "Completeness" criterion: 60 → 100 ✓
   - Status: Applied

4. **Break paragraph 3:**
   - Change: 8-line paragraph → 3-line intro + bullet list
   - Validation: End-user "Visual Clarity" criterion: 60 → 100 ✓
   - Status: Applied

5. **Architecture diagram:**
   - Status: Skipped (OPTIONAL, out of scope)

### Step 6: Calculate Metrics
- Overall score: (78 + 85 + 90) / 3 = 84
- Audience-weighted (executive): (78×2 + 85 + 90) / 4 = 83
- Critical applied: 2/2 (100%)
- High applied: 2/2 (100%)
- Application rate: 4/4 = 100%

### Output: Synthesis
```json
{
  "overall_score": 84,
  "audience_weighted_score": 83,
  "critical_improvements": [
    "Add decision deadline: March 15, 2025",
    "Quantify ROI: $340K 3-year ROI, 18-month payback"
  ],
  "high_improvements": [
    "Add risk mitigation section",
    "Break paragraph 3 into bullets"
  ],
  "optional_improvements": [
    "Add architecture diagram (out of scope)"
  ],
  "recommendations_applied": true,
  "application_rate": 1.0
}
```

---

## Integration with Copywriter Workflow

**Phase 7 position:** Between Phase 6 (Stakeholder Review) and Phase 8 (Validate & Write Document)

**TodoWrite integration:**
```
Phase 7: Synthesis & Refinement
├─ Sub-task 1: Aggregate stakeholder feedback
├─ Sub-task 2: Identify common themes
├─ Sub-task 3: Prioritize recommendations
├─ Sub-task 4: Apply CRITICAL improvement #1
├─ Sub-task 5: Apply CRITICAL improvement #2
├─ Sub-task 6: Apply HIGH improvement #1
├─ Sub-task 7: Apply HIGH improvement #2
└─ Sub-task 8: Calculate synthesis metrics
```

**Graceful degradation:**
- Individual improvement fails → Revert change, log failure, continue with remaining improvements
- All improvements fail → Continue to Phase 8 with original document, log `fallback_reason: "synthesis_failure"`
- Synthesis calculation fails → Continue to Phase 8 with original document, partial feedback in output

---

## Related Resources

- **Stakeholder Perspectives:** `references/10-stakeholder-review/{perspective}-review.md`
- **Framework Compliance:** `references/01-frameworks/*.md`
- **Writing Principles:** `references/02-principles/*.md`
- **Impact Techniques:** `references/03-impact/*.md`

---

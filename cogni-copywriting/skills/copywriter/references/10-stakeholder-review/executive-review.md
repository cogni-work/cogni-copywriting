---
title: Executive Review
type: stakeholder-review
perspective: executive
version: 1.0
---

# Executive Review Criteria

## Quick Reference

- **Use when:** Document audience includes C-suite, senior leadership, board members
- **Core principle:** Time is the scarcest resource—respect it with clarity and decision-readiness
- **Evaluation focus:** Lead with ask, quantification, time efficiency, decision clarity, credibility

## Perspective Philosophy

Executives operate under extreme time constraints and decision pressure. They need:
- **Bottom line first** - What are you asking for, and why should I care?
- **Quantified impact** - Show me the numbers, not feelings
- **Time boundaries** - When do I need to decide?
- **Clear choices** - What are my options with trade-offs?
- **Trust signals** - Why should I believe you?

**Anti-patterns to flag:**
- Burying the ask in paragraph 3
- Qualitative claims without data ("significant improvement")
- Open-ended timelines
- Single option without alternatives
- Unsupported assertions

## Evaluation Checklist

### 1. Lead with Ask (Weight: 25%)

**Question:** Does the first paragraph clearly state what is being requested and why it matters?

- ✅ **PASS:** Ask explicitly stated in first 1-2 sentences with business justification
  - Example: "Approve $500K CRM investment to reduce customer churn 15% by Q3"
  - Includes: specific action + quantified benefit + timeframe
- ⚠️ **CONCERN:** Ask stated in first paragraph but lacks clear benefit or is vague
  - Example: "This memo proposes a CRM system to improve customer relationships"
  - Missing: specific ask amount, quantified impact, or timeline
- ❌ **FAIL:** Ask buried after setup/context, or implied rather than explicit
  - Example: Paragraph 1 discusses market trends, paragraph 2 discusses competitors, paragraph 3 hints at needing "better tools"

**Why this matters:** Executives scan documents. If they can't grasp the core ask in 10 seconds, the document fails.

---

### 2. Quantification (Weight: 25%)

**Question:** Are all key claims backed by specific numbers, percentages, or dollar amounts?

- ✅ **PASS:** All major claims quantified with credible data sources
  - Example: "$340K 3-year ROI with 18-month payback (McKinsey benchmark)"
  - Example: "Customer churn reduced from 23% to 8% in pilot (Q1 2025 data)"
- ⚠️ **CONCERN:** Some quantification present but key claims remain qualitative
  - Example: "Significant cost savings expected" (vague)
  - Example: "ROI: $340K" (no timeframe or data source)
- ❌ **FAIL:** Primarily qualitative language without numbers
  - Example: "This will greatly improve efficiency and customer satisfaction"
  - Example: "Costs are reasonable and benefits are substantial"

**Why this matters:** Executives make data-driven decisions. "Significant" and "substantial" are meaningless without numbers.

---

### 3. Time Respect (Weight: 20%)

**Question:** Is the document optimized for fast reading with clear visual hierarchy?

- ✅ **PASS:** BLUF structure + visual aids (bullets, bold, short paragraphs ≤4 lines)
  - Clear hierarchy: H1 ask → H2 sections → bullets for details
  - Key numbers bolded or in tables
  - Scannable in 60-90 seconds
- ⚠️ **CONCERN:** Some visual structure but dense paragraphs or unclear hierarchy
  - Example: Bullets present but paragraphs exceed 5 lines
  - Example: No bold/emphasis on critical numbers
- ❌ **FAIL:** Wall of text, poor visual hierarchy, requires slow reading
  - Example: 8+ line paragraphs with embedded data
  - Example: No bullets, headers, or visual emphasis

**Why this matters:** Executives have 7 minutes per document. Dense text wastes their time.

---

### 4. Decision Clarity (Weight: 20%)

**Question:** Are decision requirements crystal clear (what, when, options, risks)?

- ✅ **PASS:** Explicit decision statement with deadline, clear options, and trade-offs
  - Example: "Decision needed: Approve vendor A ($500K, 6-month deploy) vs. vendor B ($650K, 3-month deploy) by March 15"
  - Includes: specific choices + trade-offs + deadline
  - Risk acknowledgment: "Key risk: vendor lock-in, mitigated by annual renewal clause"
- ⚠️ **CONCERN:** Decision request clear but missing timeline, options, or risk discussion
  - Example: "Choose between vendor A or B" (no trade-offs or deadline)
  - Example: "Decide by end of month" (no specific date)
- ❌ **FAIL:** Unclear what decision is being requested or by when
  - Example: "Your thoughts on this proposal would be appreciated"
  - Example: No timeline mentioned

**Why this matters:** Executives need to know exactly what they're deciding and when. Vague requests stall decisions.

---

### 5. Credibility (Weight: 10%)

**Question:** Does the document establish trust through attribution, precedent, or expertise?

- ✅ **PASS:** Claims attributed to credible sources or internal data
  - Example: "Gartner forecasts 40% growth in CRM market by 2026"
  - Example: "Our Q4 pilot reduced response time 35% (verified by operations team)"
  - Example: "Recommended by our CFO and IT director"
- ⚠️ **CONCERN:** Some attribution but key claims lack sources
  - Example: "Industry research shows..." (no source named)
  - Example: "Experts agree..." (which experts?)
- ❌ **FAIL:** Unsupported assertions without attribution
  - Example: "This is the best solution available"
  - Example: "Everyone knows this approach works"

**Why this matters:** Executives won't approve based on unsubstantiated claims. Trust requires evidence.

---

## Scoring Guidelines

**Calculation:**
1. Evaluate each criterion: PASS (100), CONCERN (60), FAIL (0)
2. Multiply by criterion weight:
   - Lead with Ask: score × 0.25
   - Quantification: score × 0.25
   - Time Respect: score × 0.20
   - Decision Clarity: score × 0.20
   - Credibility: score × 0.10
3. Sum weighted scores for total (0-100)

**Thresholds:**
- 85-100: Excellent, executive-ready
- 70-84: Good, minor improvements needed
- 50-69: Concerns, significant revisions required
- 0-49: Failing, major structural changes needed

**Example calculation:**
- Lead with Ask: PASS (100 × 0.25 = 25)
- Quantification: CONCERN (60 × 0.25 = 15)
- Time Respect: PASS (100 × 0.20 = 20)
- Decision Clarity: CONCERN (60 × 0.20 = 12)
- Credibility: PASS (100 × 0.10 = 10)
- **Total: 82** (Good)

---

## Feedback Template

**Structured JSON output:**
```json
{
  "perspective": "executive",
  "score": 82,
  "criteria_scores": {
    "lead_with_ask": 100,
    "quantification": 60,
    "time_respect": 100,
    "decision_clarity": 60,
    "credibility": 100
  },
  "strengths": [
    "Clear BLUF structure with ask in first sentence",
    "Strong visual hierarchy with bullets and bold numbers",
    "Credible sourcing (Gartner, internal pilot data)"
  ],
  "concerns": [
    "ROI claim lacks timeframe (3-year? 5-year?)",
    "Decision timeline vague ('end of Q1' not specific date)",
    "No vendor comparison or alternatives presented"
  ],
  "recommendations": [
    "CRITICAL: Add specific ROI timeframe and payback period",
    "CRITICAL: Replace 'end of Q1' with specific date (e.g., 'by March 31, 2025')",
    "HIGH: Add 2-3 vendor options with trade-off comparison",
    "OPTIONAL: Include risk mitigation strategy"
  ]
}
```

---

## Common Improvement Patterns

### Pattern 1: Strengthen the Ask
**Before:** "This memo discusses the potential benefits of a new CRM system."
**After:** "Approve $500K CRM investment to reduce customer churn 15% by Q3 2025."

### Pattern 2: Quantify Claims
**Before:** "This will significantly improve customer satisfaction."
**After:** "This will increase NPS from 42 to 58 (industry benchmark: 55, Forrester 2024)."

### Pattern 3: Add Decision Clarity
**Before:** "Please review and approve."
**After:** "Decision needed by March 15: Approve Option A (6-month deploy, $500K) or Option B (3-month deploy, $650K, higher vendor risk)."

### Pattern 4: Improve Scannability
**Before:** (8-line paragraph with embedded data)
**After:**
```
Key benefits:
- **15% churn reduction** (23% → 8%, Q1 pilot data)
- **$340K 3-year ROI** (18-month payback)
- **35% faster response time** (operations verified)
```

---

## Related Resources

- **BLUF Framework:** `references/01-frameworks/bluf.md`
- **Pyramid Principle:** `references/01-frameworks/pyramid-principle.md`
- **Number Plays:** `references/03-impact/number-plays.md`
- **Executive Memo Template:** `references/04-deliverables/memo.md`

## Conflict Resolution

When executive perspective conflicts with other stakeholders:

| Conflict | Resolution |
|----------|------------|
| **Technical wants detail, Executive wants brevity** | Executive summary + detailed appendix |
| **Marketing wants emotion, Executive wants data** | Lead with data, use power words for emphasis (validated, proven) |
| **Legal wants hedging, Executive wants clarity** | Clear recommendation + brief risk disclosure |
| **End-user wants simple, Executive wants sophisticated** | Simplify core message, add technical appendix |

**Tiebreaker:** If deliverable type is executive memo/brief, executive perspective takes priority.

---

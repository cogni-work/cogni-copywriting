---
title: Legal/Compliance Review
type: stakeholder-review
perspective: legal
version: 1.0
---

# Legal/Compliance Review Criteria

## Quick Reference

- **Use when:** Document involves contracts, policies, compliance requirements, vendor agreements, public statements
- **Core principle:** Minimize organizational risk through precise language and appropriate hedging
- **Evaluation focus:** Risk language, regulatory alignment, liability mitigation, evidence standards, disclosure completeness

## Perspective Philosophy

Legal/compliance stakeholders prioritize risk management and regulatory adherence. They need:
- **Risk-appropriate language** - Claims hedged appropriately, not overpromised
- **Regulatory compliance** - Alignment with relevant laws and standards
- **Liability protection** - Disclaimers, limitations, and proper attribution
- **Evidence standards** - Claims must be defensible
- **Complete disclosure** - All material risks surfaced

**Anti-patterns to flag:**
- Absolute guarantees ("will", "guarantee", "always")
- Unfounded claims without evidence
- Missing required disclosures or disclaimers
- Commitments beyond organizational control
- Non-compliant language for regulated industries

## Evaluation Checklist

### 1. Risk Language (Weight: 30%)

**Question:** Are claims appropriately hedged to avoid over-commitment or false guarantees?

- ✅ **PASS:** Claims use appropriate hedging language and avoid absolute guarantees
  - Example: "Based on pilot data, we expect to reduce churn by approximately 15% within 6 months"
  - Example: "The system is designed to achieve 99.9% uptime, subject to external dependencies"
  - Includes: conditional language (expect, anticipate, designed to), qualifiers (approximately), limitations
- ⚠️ **CONCERN:** Some hedging present but occasional absolute claims
  - Example: "This will reduce churn by 15%" (too definitive)
  - Example: "We guarantee 99.9% uptime" (guarantee without qualifiers)
- ❌ **FAIL:** Frequent absolute guarantees or over-commitments
  - Example: "This solution will always work perfectly"
  - Example: "We will eliminate all security vulnerabilities"
  - Example: "Guaranteed ROI within 6 months"

**Why this matters:** Absolute claims create contractual obligations and legal liability.

**Approved hedging terms:** anticipate, believe, designed to, estimate, expect, intend, may, plan, project, seek, should, target

---

### 2. Regulatory Alignment (Weight: 25%)

**Question:** Does the document comply with relevant regulatory requirements and industry standards?

- ✅ **PASS:** Document acknowledges and complies with applicable regulations
  - Example: "Data handling complies with GDPR Article 6(1)(b) and CCPA Section 1798.100"
  - Example: "Financial projections prepared in accordance with GAAP standards"
  - Includes: specific regulation citations, compliance statements
- ⚠️ **CONCERN:** General compliance language but missing specific regulatory references
  - Example: "We comply with data protection laws" (which laws?)
  - Example: "Financials follow standard accounting practices" (which standards?)
- ❌ **FAIL:** No compliance discussion or language that conflicts with regulations
  - Example: No mention of data protection in document handling PII
  - Example: Health claims without FDA disclaimer (if applicable)

**Why this matters:** Non-compliance exposes organization to regulatory penalties and lawsuits.

**Common regulatory domains:**
- Data protection: GDPR, CCPA, HIPAA
- Financial: GAAP, SOX, SEC regulations
- Industry-specific: FDA (healthcare), FINRA (finance), FCC (telecom)

---

### 3. Liability Mitigation (Weight: 20%)

**Question:** Are appropriate disclaimers, limitations, and liability protections present?

- ✅ **PASS:** Document includes necessary disclaimers and limitation of liability language
  - Example: "Recommendations based on information available as of Jan 2025. Not financial advice. Consult qualified advisors."
  - Example: "System availability subject to third-party service dependencies (AWS, Stripe)"
  - Includes: temporal limitations, scope limitations, dependency disclosures
- ⚠️ **CONCERN:** Some disclaimers present but incomplete
  - Example: "Not financial advice" (missing temporal limitation, advisor reference)
  - Example: Mentions dependencies but no liability limitation
- ❌ **FAIL:** Missing critical disclaimers or liability protections
  - Example: Giving specific investment advice without disclaimer
  - Example: Making commitments dependent on third parties without disclosure

**Why this matters:** Insufficient disclaimers create liability exposure and professional responsibility violations.

**Required disclaimers by context:**
- Financial: "Not financial/investment advice. Consult qualified advisors."
- Legal: "Not legal advice. Consult qualified counsel."
- Medical: "Not medical advice. Consult qualified healthcare providers."
- Forward-looking: "Based on current information. Actual results may vary."

---

### 4. Evidence Standards (Weight: 15%)

**Question:** Are all claims supported by adequate evidence and properly attributed?

- ✅ **PASS:** All material claims backed by verifiable evidence with proper attribution
  - Example: "According to Gartner (2024 report), CRM adoption increased 40%"
  - Example: "Internal pilot (Q4 2024, n=500 customers) showed 15% churn reduction"
  - Includes: source identification, date, sample size/methodology where relevant
- ⚠️ **CONCERN:** Most claims supported but some attributions missing or vague
  - Example: "Industry research shows..." (which research?)
  - Example: "Experts agree..." (which experts? What credentials?)
- ❌ **FAIL:** Material claims without evidence or attribution
  - Example: "This is the best solution on the market" (unsupported)
  - Example: "ROI guaranteed" (no evidence)

**Why this matters:** Unsubstantiated claims expose organization to false advertising and misrepresentation liability.

**Evidence hierarchy (strongest to weakest):**
1. Primary data (internal measurements, controlled studies)
2. Peer-reviewed research
3. Reputable industry research (Gartner, Forrester)
4. Expert opinion (qualified professionals)
5. Anecdotal evidence (testimonials)

---

### 5. Disclosure Completeness (Weight: 10%)

**Question:** Are all material risks, limitations, and conflicts of interest disclosed?

- ✅ **PASS:** Document discloses all material risks and limitations
  - Example: "Key risks: vendor lock-in (mitigated by annual renewal), data migration complexity (estimated 40 hours), dependency on vendor roadmap"
  - Example: "Limitations: Projections assume stable economic conditions and no major competitor disruption"
  - Includes: operational risks, financial risks, assumptions, conflicts of interest
- ⚠️ **CONCERN:** Some risks disclosed but missing material risks
  - Example: Mentions technical risks but omits financial risks
  - Example: Discloses dependency on vendor but not migration cost/complexity
- ❌ **FAIL:** Material risks not disclosed or minimized
  - Example: Vendor proposal omits vendor lock-in risk
  - Example: Financial projections omit key assumptions

**Why this matters:** Material omissions can constitute fraud or misrepresentation.

**Material risk categories:**
- Financial: cost overruns, ROI uncertainty
- Operational: resource requirements, timeline risks
- Technical: dependencies, compatibility, scalability limits
- Legal: regulatory changes, contractual obligations
- Strategic: market shifts, competitive response

---

## Scoring Guidelines

**Calculation:**
1. Evaluate each criterion: PASS (100), CONCERN (60), FAIL (0)
2. Multiply by criterion weight:
   - Risk Language: score × 0.30
   - Regulatory Alignment: score × 0.25
   - Liability Mitigation: score × 0.20
   - Evidence Standards: score × 0.15
   - Disclosure Completeness: score × 0.10
3. Sum weighted scores for total (0-100)

**Thresholds:**
- 85-100: Excellent, legally sound
- 70-84: Good, minor risk issues
- 50-69: Concerns, significant risk exposure
- 0-49: Failing, major legal/compliance issues

**Example calculation:**
- Risk Language: CONCERN (60 × 0.30 = 18)
- Regulatory Alignment: PASS (100 × 0.25 = 25)
- Liability Mitigation: PASS (100 × 0.20 = 20)
- Evidence Standards: CONCERN (60 × 0.15 = 9)
- Disclosure Completeness: PASS (100 × 0.10 = 10)
- **Total: 82** (Good)

---

## Feedback Template

**Structured JSON output:**
```json
{
  "perspective": "legal",
  "score": 82,
  "criteria_scores": {
    "risk_language": 60,
    "regulatory_alignment": 100,
    "liability_mitigation": 100,
    "evidence_standards": 60,
    "disclosure_completeness": 100
  },
  "strengths": [
    "Strong GDPR compliance language with specific Article references",
    "Appropriate disclaimers for forward-looking statements",
    "Material risks disclosed (vendor lock-in, migration complexity)"
  ],
  "concerns": [
    "Absolute guarantee language: 'will reduce churn by 15%' (over-commitment)",
    "ROI claim unsupported by verifiable evidence or methodology",
    "Missing temporal limitation on recommendations ('as of [date]')"
  ],
  "recommendations": [
    "CRITICAL: Replace 'will reduce churn by 15%' with 'is expected to reduce churn by approximately 15%, based on pilot data'",
    "HIGH: Add evidence attribution for ROI claim (source, methodology, date)",
    "HIGH: Add temporal disclaimer: 'Recommendations based on information available as of January 2025'",
    "OPTIONAL: Consider adding limitation of liability statement for third-party dependencies"
  ]
}
```

---

## Common Improvement Patterns

### Pattern 1: Add Appropriate Hedging
**Before:** "This solution will eliminate security vulnerabilities."
**After:** "This solution is designed to address known security vulnerabilities identified as of January 2025."

### Pattern 2: Add Regulatory Compliance
**Before:** "We handle customer data securely."
**After:** "Customer data handling complies with GDPR Article 32 (security of processing) and is encrypted in transit (TLS 1.3) and at rest (AES-256)."

### Pattern 3: Add Disclaimers
**Before:** "Expected ROI: $500K over 3 years."
**After:** "Projected ROI: $500K over 3 years, based on current cost structure and market conditions. Actual results may vary. Not financial advice."

### Pattern 4: Improve Evidence Standards
**Before:** "Industry experts agree this is the best approach."
**After:** "Gartner (2024 CRM Magic Quadrant) identifies this approach as a leading practice, adopted by 60% of enterprise clients surveyed."

---

## Related Resources

- **Hedging Language:** `references/02-principles/word-choice.md`
- **Risk Documentation:** `references/04-deliverables/proposal.md`
- **Evidence Standards:** `references/02-principles/clarity-rules.md`

## Conflict Resolution

When legal perspective conflicts with other stakeholders:

| Conflict | Resolution |
|----------|------------|
| **Executive wants bold claims, Legal wants hedging** | Strong but hedged: "We expect to achieve..." vs. "We will achieve..." |
| **Marketing wants guarantees, Legal wants disclaimers** | Aspirational language with appropriate qualifiers: "Designed to deliver..." |
| **Technical wants definitive, Legal wants conditional** | Technical facts remain definitive, projections hedged |
| **End-user wants simplicity, Legal wants disclosure** | Simple language + brief, clear risk disclosure section |

**Tiebreaker:** If document has external legal consequences (contracts, public statements), legal perspective takes priority.

---

---
title: Technical Review
type: stakeholder-review
perspective: technical
version: 1.0
---

# Technical Review Criteria

## Quick Reference

- **Use when:** Document contains technical specifications, implementation details, architecture decisions
- **Core principle:** Precision and accuracy build trust—vague or incorrect technical content destroys credibility
- **Evaluation focus:** Accuracy, logical flow, precision, completeness, terminology

## Perspective Philosophy

Technical stakeholders prioritize correctness and logical rigor. They need:
- **Accurate facts** - No handwaving or approximations
- **Logical consistency** - Claims follow from evidence
- **Precise language** - Right terms used correctly
- **Complete picture** - No critical gaps
- **Technical depth** - Sufficient detail to evaluate feasibility

**Anti-patterns to flag:**
- Technically incorrect statements
- Logical leaps without supporting evidence
- Misused or vague technical terms
- Missing critical technical details (dependencies, constraints, risks)
- Overpromising technical outcomes

## Evaluation Checklist

### 1. Accuracy (Weight: 30%)

**Question:** Are all technical facts, specifications, and claims correct and verifiable?

- ✅ **PASS:** All technical statements accurate and properly attributed
  - Example: "PostgreSQL 14.2 supports native JSON operators (official documentation)"
  - Example: "API response time: 145ms p95 (production metrics, Jan 2025)"
  - Includes: specific versions, actual measurements, data sources
- ⚠️ **CONCERN:** Most facts correct but some statements unverified or imprecise
  - Example: "PostgreSQL supports JSON" (missing version, native vs. extension?)
  - Example: "Fast API response time" (no specific measurement)
- ❌ **FAIL:** Incorrect technical facts or unsupported technical claims
  - Example: "PostgreSQL is a NoSQL database" (incorrect category)
  - Example: "This will scale to millions of users" (no evidence)

**Why this matters:** A single technical error undermines credibility with technical audiences.

---

### 2. Logical Flow (Weight: 25%)

**Question:** Do conclusions follow logically from evidence with clear cause-effect relationships?

- ✅ **PASS:** Clear logical chain from problem → analysis → solution → outcome
  - Example: "Current API timeout (5s) exceeds p95 response time (145ms) → implement 1s timeout → reduce failed requests 40%"
  - Claims explicitly linked to supporting evidence
  - No logical leaps
- ⚠️ **CONCERN:** General logical structure present but some leaps or missing links
  - Example: "API has issues → implement new architecture → better performance" (missing: what issues? Why this architecture? How much better?)
- ❌ **FAIL:** Conclusions not supported by evidence or logical inconsistencies
  - Example: "Traffic increased 20% → reduce server capacity 30%" (inverted logic)
  - Example: "System is slow → use microservices" (no analysis of root cause)

**Why this matters:** Technical decisions must be defensible through rigorous reasoning.

---

### 3. Precision (Weight: 20%)

**Question:** Are technical terms used correctly and consistently with appropriate specificity?

- ✅ **PASS:** Technical terms used correctly, consistently, and with proper specificity
  - Example: "Implement eventual consistency via event sourcing with CQRS pattern"
  - Example: "Deploy to Kubernetes 1.28 cluster with 3 replicas, HPA min/max 3/10"
  - Specific: versions, quantities, patterns named correctly
- ⚠️ **CONCERN:** Technical terms mostly correct but some vagueness or inconsistency
  - Example: "Use cloud infrastructure" (which cloud? IaaS/PaaS?)
  - Example: "Implement caching" (what layer? technology? TTL?)
- ❌ **FAIL:** Technical terms misused, vague, or inconsistent
  - Example: "Use AI to optimize the algorithm" (AI is not a technology)
  - Example: Switching between "microservices" and "distributed architecture" inconsistently

**Why this matters:** Imprecise language signals shallow technical understanding.

---

### 4. Completeness (Weight: 15%)

**Question:** Are all critical technical details present (dependencies, constraints, risks, trade-offs)?

- ✅ **PASS:** Document addresses dependencies, constraints, risks, and trade-offs
  - Example: "Requires Redis 7.0+ (memory: 16GB, network: <5ms latency). Risk: single point of failure, mitigated by Redis Sentinel."
  - Includes: system requirements, constraints, failure modes, mitigation
- ⚠️ **CONCERN:** Some technical context present but missing key details
  - Example: "Requires Redis" (no version, resource requirements, or failure handling)
  - Example: Solution described but no trade-off analysis
- ❌ **FAIL:** Critical technical details omitted
  - Example: Architecture described but no mention of data persistence strategy
  - Example: Performance claims without discussing resource requirements

**Why this matters:** Technical implementations fail due to overlooked dependencies and constraints.

---

### 5. Terminology (Weight: 10%)

**Question:** Are technical terms appropriate for the audience (not too simple, not too complex)?

- ✅ **PASS:** Technical depth matches audience sophistication
  - For technical audience: "Implement LRU cache eviction with TTL override"
  - For mixed audience: "Implement smart caching (keeps frequently-accessed data, expires old data)"
  - Terms defined when necessary
- ⚠️ **CONCERN:** Slight mismatch between terminology and audience
  - For technical audience: "Use a smart system to store data temporarily" (too simple)
  - For mixed audience: "Implement LRU cache eviction" (no definition)
- ❌ **FAIL:** Terminology significantly mismatched to audience
  - For technical audience: Avoiding technical terms entirely
  - For non-technical audience: Unexplained jargon throughout

**Why this matters:** Wrong technical depth alienates the audience—either too condescending or too opaque.

---

## Scoring Guidelines

**Calculation:**
1. Evaluate each criterion: PASS (100), CONCERN (60), FAIL (0)
2. Multiply by criterion weight:
   - Accuracy: score × 0.30
   - Logical Flow: score × 0.25
   - Precision: score × 0.20
   - Completeness: score × 0.15
   - Terminology: score × 0.10
3. Sum weighted scores for total (0-100)

**Thresholds:**
- 85-100: Excellent, technically sound
- 70-84: Good, minor technical gaps
- 50-69: Concerns, significant technical issues
- 0-49: Failing, major technical flaws

**Example calculation:**
- Accuracy: PASS (100 × 0.30 = 30)
- Logical Flow: PASS (100 × 0.25 = 25)
- Precision: CONCERN (60 × 0.20 = 12)
- Completeness: CONCERN (60 × 0.15 = 9)
- Terminology: PASS (100 × 0.10 = 10)
- **Total: 86** (Excellent)

---

## Feedback Template

**Structured JSON output:**
```json
{
  "perspective": "technical",
  "score": 86,
  "criteria_scores": {
    "accuracy": 100,
    "logical_flow": 100,
    "precision": 60,
    "completeness": 60,
    "terminology": 100
  },
  "strengths": [
    "Accurate technical specifications with versions (PostgreSQL 14.2, Redis 7.0)",
    "Clear logical chain from problem to solution",
    "Appropriate technical depth for engineering audience"
  ],
  "concerns": [
    "Caching implementation details vague (layer? technology? TTL?)",
    "Missing failover strategy for Redis dependency",
    "Performance claims lack supporting benchmarks"
  ],
  "recommendations": [
    "HIGH: Specify caching layer (application vs. database), technology (Redis vs. Memcached), and TTL strategy",
    "HIGH: Add Redis failure handling (Sentinel configuration or alternative)",
    "OPTIONAL: Include benchmark data to support performance claims"
  ]
}
```

---

## Common Improvement Patterns

### Pattern 1: Increase Accuracy
**Before:** "The system is fast and scales well."
**After:** "The system achieves 145ms p95 response time and scales linearly to 10K concurrent users (load test Jan 2025)."

### Pattern 2: Strengthen Logical Flow
**Before:** "Users complain about speed, so we need microservices."
**After:** "Users report 5s page loads (p95: 4.8s, analytics Dec 2024). Root cause: monolithic API with blocking calls. Solution: async microservices reduce p95 to 800ms (pilot data)."

### Pattern 3: Improve Precision
**Before:** "Use cloud storage."
**After:** "Use AWS S3 Standard storage class (region: us-east-1) with 30-day lifecycle transition to Glacier."

### Pattern 4: Add Completeness
**Before:** "Deploy to Kubernetes cluster."
**After:** "Deploy to Kubernetes 1.28 cluster (3 nodes, 16GB RAM each). Requires: PostgreSQL 14+, Redis 7+. Failure mode: Redis unavailable → read-only mode. Mitigation: Redis Sentinel (3-node quorum)."

---

## Related Resources

- **Technical Terminology:** `references/02-principles/word-choice.md`
- **Logical Structure:** `references/02-principles/clarity-rules.md`
- **Precision Guidelines:** `references/02-principles/active-voice.md`
- **Technical Brief Template:** `references/04-deliverables/brief.md`

## Conflict Resolution

When technical perspective conflicts with other stakeholders:

| Conflict | Resolution |
|----------|------------|
| **Executive wants brevity, Technical wants detail** | Executive summary + technical appendix with architecture diagrams |
| **Marketing wants simplification, Technical wants precision** | Define terms on first use, maintain technical accuracy |
| **End-user wants plain language, Technical wants jargon** | Plain language with technical glossary |
| **Legal wants hedging, Technical wants definitive statements** | Clear technical facts + separate risk disclosure section |

**Tiebreaker:** If deliverable type is technical specification/architecture doc, technical perspective takes priority.

---

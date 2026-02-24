---
title: Pyramid Principle (McKinsey)
type: messaging-framework
category: communication-framework
tags: [pyramid, mckinsey, consulting, answer-first, structured-analysis]
audience: [all]
best-for: [reports, briefs, proposals, executive-summaries]
origin: mckinsey-consulting
formality: high
related:
  - bluf-framework
  - scqa-framework
version: 1.0
last_updated: 2025-10-29
---

# Pyramid Principle (McKinsey)

## Quick Reference
**Best for:** Reports, briefs, proposals, executive summaries
**Structure:** Answer first → Supporting arguments (3-5) → Evidence
**When to use:** Complex recommendations, consulting context, structured analysis
**Formality:** High (consulting/McKinsey style)
**Key principle:** Start with the answer, support with MECE arguments

## Core Structure

The Pyramid Principle is a communication framework that structures information answer-first, then supporting arguments.

### 4-Layer Hierarchy

1. **Start with the answer** (conclusion/main message)
2. **Group supporting arguments** (3-5 logical clusters, MECE)
3. **Order groups logically** (priority, sequence, or importance)
4. **Provide evidence** within each group

### Visual Representation

```
                    ANSWER/CONCLUSION
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   ARGUMENT 1        ARGUMENT 2        ARGUMENT 3
        │                 │                 │
    ┌───┼───┐         ┌───┼───┐         ┌───┼───┐
   E1  E2  E3        E4  E5  E6        E7  E8  E9
```

E = Evidence/Supporting Details

## Application Pattern

### Basic Template

```markdown
## Answer (Start with Conclusion)
{Clear 2-3 sentence answer to main question}

### Three Core Principles (or Key Findings)
1. **Principle 1**: {Brief statement}
2. **Principle 2**: {Brief statement}
3. **Principle 3**: {Brief statement}

## Supporting Section 1: {Name}
{Detailed evidence and explanation}

## Supporting Section 2: {Name}
{Detailed evidence and explanation}

## Supporting Section 3: {Name}
{Detailed evidence and explanation}
```

### MECE Principle Integration

Arguments must be **Mutually Exclusive, Collectively Exhaustive**:

- **Mutually Exclusive:** No overlap between categories
- **Collectively Exhaustive:** All relevant points covered

✅ **MECE Example:**

- Architecture
- Algorithms
- Process

❌ **NOT MECE:**

- Architecture
- Code (overlaps with Architecture)
- Quality (overlaps with both)

## Real-World Examples

### Example 1: Strategic Recommendation

**Answer:**
Acquire CompanyX for $50M to expand into European market.

**Supporting Arguments (MECE):**
1. **Market Opportunity**: €200M addressable market, 15% growth
2. **Strategic Fit**: Complementary product lines, shared customer base
3. **Financial Viability**: Payback in 3 years, 25% IRR

**Evidence for Argument 1:**
- Market size data from Gartner
- Growth projections from internal analysis
- Competitor market share breakdown

### Example 2: Research Synthesis

**Answer:**
Deep research requires a 12-entity hierarchical architecture organized across 7 phases—from initial questions through verified claims and synthesis.

**Supporting Arguments (MECE):**
1. **Progressive Refinement**: Questions → Dimensions → Queries → Findings
2. **Iterative Validation**: Every claim traced through evidence chains
3. **Hybrid Automation**: 17% fully automated, 83% requires human review

**Evidence:**
- 127 projects analyzed
- Statistical correlations (r=0.74)
- Implementation case studies

## Quality Checks

Before finalizing Pyramid structure:

- ✓ Does first section state the main conclusion?
- ✓ Are arguments grouped into 3-5 logical clusters?
- ✓ Does each group have a clear topic?
- ✓ Is ordering logical and compelling?
- ✓ Are arguments MECE (no overlap, fully exhaustive)?
- ✓ Does evidence support each argument?
- ✓ Could reader understand answer without reading evidence?

## Deliverable-Specific Guidance

### For Reports
- Answer becomes executive summary opening
- Each supporting argument = major section
- Evidence fills section body
- Conclusion reinforces answer

### For Briefs
- Extreme compression of Pyramid
- Answer = first paragraph
- Arguments = bullet list (3-5 items)
- Evidence = 1-2 sentences per argument

### For Proposals
- Answer = recommendation section
- Arguments = benefit categories (MECE)
- Evidence = case studies, data, testimonials
- Natural lead to pricing/next steps

### For Executive Summaries
- Pure Pyramid structure mandatory
- Answer first (always)
- Arguments MECE (always)
- Evidence concise (bullet points)
- 1-2 pages maximum

## When NOT to Use Pyramid

- **Storytelling contexts:** Narrative suspense has value
- **Persuading skeptics:** Build case before conclusion
- **Teaching complex concepts:** Learning requires scaffolding
- **Cultural preferences:** Some cultures prefer context-first

## Transformation Example

### Before (Answer Hidden)

```markdown
## Background

Research methodologies for systematic literature reviews have evolved
significantly over the past decades. Multiple frameworks have been proposed
by various researchers, each contributing different perspectives on optimal
information architecture...

[300+ words before getting to the answer]

## Conclusion

Therefore, we recommend a 12-entity hierarchical architecture.
```

### After (Answer First - Pyramid)

```markdown
## Answer

Deep research requires a 12-entity hierarchical architecture organized across
7 phases—from initial questions through verified claims and synthesis.

### Three Core Principles

1. **Progressive Refinement**: Questions → Dimensions → Queries → Findings
2. **Iterative Validation**: Every claim traced through evidence chains
3. **Hybrid Automation**: 17% fully automated, 83% requires human review

## Supporting Evidence

[Details follow in logical groups]
```

## Integration with Writing Principles

**Clarity:** Pyramid structure enforces clarity by putting answer first
**Conciseness:** Pressure to state conclusion upfront eliminates verbosity
**Active voice:** "We recommend..." not "It is recommended..."
**MECE:** Logical grouping prevents overlap and ensures completeness

## Common Mistakes

### Mistake 1: Fake Pyramid (Answer Still Hidden)
❌ **Bad:** "Background → Analysis → Recommendation" (traditional structure with relabeled sections)
✅ **Good:** "Recommendation → Why it works (3 MECE arguments) → Evidence"

### Mistake 2: Non-MECE Arguments
❌ **Bad:** Technology, Implementation, Technology Stack (overlap)
✅ **Good:** Technology, Process, People (distinct categories)

### Mistake 3: Too Many Arguments
❌ **Bad:** 8 supporting arguments (overwhelming)
✅ **Good:** 3-5 arguments (scannable, memorable)

## See Also
- `bluf-framework.md` (Similar top-down approach, military style)
- `scqa-framework.md` (Alternative with narrative flow)
- `../01-core-principles/clarity-principles.md` (Clear language requirements)

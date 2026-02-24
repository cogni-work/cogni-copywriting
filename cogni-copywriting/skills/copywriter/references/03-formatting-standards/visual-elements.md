---
title: Visual Elements for Scannability
type: formatting-standard
category: formatting
tags: [visual-elements, tables, callouts, lists, emphasis]
audience: [all]
related:
  - heading-hierarchy
  - markdown-basics
version: 1.0
last_updated: 2025-10-29
---

# Visual Elements for Scannability

## Quick Reference
**Purpose:** Break up text, highlight key information, improve readability
**Target ratio:** ~1 visual element per 2 paragraphs
**Key principle:** Purposeful, not decorative

## Visual Element Types

### 1. Callouts for Key Insights

**Use for:** Critical findings, main conclusions, important warnings

**Syntax:**
```markdown
> **Key Insight**: {Important takeaway in 1-2 sentences}
```

**Example:**
> **Key Insight**: Teams using automated code review reduced wait times by 75% while maintaining quality.

**When to use:**
- Highlighting main takeaways
- Warning about critical issues
- Emphasizing recommendations
- Drawing attention to non-obvious insights

**Avoid:** Using for every paragraph or decorative purposes

### 2. Tables for Comparisons

**Use for:** Data comparison, side-by-side analysis, structured information

**Basic Table:**
```markdown
| Aspect | Finding | Confidence |
|--------|---------|------------|
| Speed  | 75% faster | High |
| Cost   | 30% reduction | Medium |
| Quality | Stable at 1.2% | High |
```

**Renders as:**
| Aspect | Finding | Confidence |
|--------|---------|------------|
| Speed  | 75% faster | High |
| Cost   | 30% reduction | Medium |
| Quality | Stable at 1.2% | High |

**Best practices:**
- 3-5 columns maximum for readability
- Keep cell content concise (1-5 words ideal)
- Align numbers right, text left
- Use for >= 3 items being compared

### 3. Bullet Lists for Enumerations

**Use for:** Action items, feature lists, enumerated findings

**Unordered List** (no priority/sequence):
```markdown
- First point
- Second point
- Third point
```

**Ordered List** (priority/sequence matters):
```markdown
1. First step
2. Second step
3. Third step
```

**Nested List** (sub-items):
```markdown
- Main category
  - Sub-item A
  - Sub-item B
- Another category
  - Sub-item C
```

**When to use:**
- Listing 3+ related items
- Action items or steps
- Features or capabilities
- Key findings or principles

**Avoid:**
- Overuse (not for every paragraph)
- Single-item lists
- Lists longer than 7 items (break into categories)

### 4. Bold Emphasis

**Use for:** Technical terms (first use), critical findings, key concepts

**Syntax:**
```markdown
**Critical Term** or **Key Finding**
```

**Example:**
The **MECE principle** (Mutually Exclusive, Collectively Exhaustive) ensures clean categorization.

**Best practices:**
- First use of important terms
- 2-3 bold items per paragraph maximum
- Critical numbers or percentages
- Section topic sentences

**Avoid:**
- Entire sentences in bold
- Overuse (loses impact)
- Bold for emphasis only (use sparingly)

### 5. Section Dividers

**Use for:** Major topic transitions, clear separation between themes

**Syntax:**
```markdown
---
```

**Renders as horizontal rule separating sections**

**When to use:**
- Major topic shifts
- Between independent sections
- Before/after long lists or tables
- Between case studies or examples

**Avoid:** Using between every section (visual clutter)

### 6. Code Blocks

**Use for:** Commands, code examples, structured data, formulas

**Inline code:**
```markdown
Use the `calculate_readability.py` script
```

**Block code:**
````markdown
```bash
python3 scripts/calculate_readability.py document.md
```
````

**When to use:**
- Terminal commands
- File paths
- Code snippets
- Configuration examples
- Formulas or algorithms

### 7. Block Quotes

**Use for:** Testimonials, citations, important external statements

**Syntax:**
```markdown
> "This solution transformed our workflow and saved 20 hours weekly."
> — Sarah Martinez, Engineering Director
```

**When to use:**
- Customer testimonials
- Expert quotes
- Citations from research
- Pull quotes from longer text

## Target Ratios by Deliverable

| Deliverable | Visual Elements Target |
|-------------|------------------------|
| Memo | 2-4 (1 per page typically) |
| Email | 1-2 (keep minimal) |
| Brief | 3-6 (1-3 pages) |
| Report | 10-20+ (varies by length) |
| One-pager | 4-6 (dense but scannable) |
| Executive Summary | 2-4 (concise focus) |

## Visual Element Combinations

Effective patterns combining multiple elements:

### Pattern 1: Key Finding
```markdown
## Finding: Cost Reduction

> **Key Insight**: Implementation reduced costs by 30% ($2M savings).

**Breakdown:**
- Infrastructure: $800K saved
- Operations: $700K saved
- Maintenance: $500K saved
```

### Pattern 2: Comparison Analysis
```markdown
## Approach Comparison

| Approach | Cost | Timeline | Risk |
|----------|------|----------|------|
| Option A | $1M | 6 months | Low |
| Option B | $2M | 3 months | Medium |

**Recommendation**: Option A provides best risk-adjusted ROI.
```

### Pattern 3: Process Steps
```markdown
## Implementation Process

1. **Phase 1: Discovery** (2 weeks)
   - Stakeholder interviews
   - Requirements gathering

2. **Phase 2: Development** (8 weeks)
   - Prototype building
   - Testing cycles

3. **Phase 3: Deployment** (4 weeks)
   - Pilot launch
   - Full rollout
```

## Quality Standards

**Scannability test:** Can reader grasp structure in 30 seconds by scanning visual elements alone?

**Visual balance:** Roughly 1 visual element per 2 paragraphs prevents walls of text

**Purpose test:** Each visual element should serve a clear function (comparison, emphasis, structure)

## Common Mistakes

### Mistake 1: Overuse of Bullets
❌ **Bad:** Converting every paragraph to bullet points
✅ **Good:** Using bullets for actual lists (3+ items)

### Mistake 2: Decorative Tables
❌ **Bad:** Table for single-row data that could be inline
✅ **Good:** Tables for 3+ rows of comparative data

### Mistake 3: Excessive Bold
❌ **Bad:** **Multiple sentences or entire paragraphs** in bold
✅ **Good:** **Key term** or **critical finding** (2-3 words)

### Mistake 4: Random Callouts

❌ **Bad:** Callout for routine information
✅ **Good:** Callout for genuine key insights

## See Also

- `heading-hierarchy.md` (Header structure for scannability)
- `markdown-basics.md` (Full markdown syntax reference)

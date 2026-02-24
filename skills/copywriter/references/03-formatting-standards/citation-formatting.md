---
title: Citation Formatting Standards
type: formatting-standard
category: formatting
tags: [citations, references, markdown, superscript]
audience: [all]
related:
  - markdown-basics
  - visual-elements
version: 1.0
last_updated: 2025-12-06
---

# Citation Formatting Standards

## Quick Reference
**Purpose:** Standardize inline citation placement and formatting for optimal readability
**Compatibility:** Markdown with HTML superscript tags
**Key principle:** Citations at specific claim points, visually separated when consecutive

## Citation Placement Rules

### Rule 1: Citations at Granular Level

Citations should be placed at the most specific level of claim, not at section headers.

❌ **Bad:**
```markdown
**Begruendung:** Industrial SaaS offers compelling economics<sup>[1](path)</sup><sup>[2](path)</sup>.

**Umsetzung:**
1. Higher KGV multiples (2-5x)
2. Reduced cyclical volatility
3. Faster revenue growth
```

✅ **Good:**
```markdown
**Begruendung:** Industrial SaaS offers compelling economics.

**Umsetzung:**
1. Higher KGV multiples (2-5x)<sup>[1](path)</sup>
2. Reduced cyclical volatility<sup>[2](path)</sup>
3. Faster revenue growth<sup>[1](path)</sup>
```

**Rationale:**
- Enables readers to verify specific claims
- Improves academic rigor
- Reduces citation ambiguity
- Better supports fact-checking

### Rule 2: Citations in Recommendation Lists

For structured recommendation sections with "Begruendung" and "Umsetzung" subsections:

**Pattern:**
```markdown
## {Recommendation Title}

**Begruendung:** {Explanation without citations}

**Umsetzung:**
1. {Action item with citation}<sup>[n](path)</sup>
2. {Action item with citation}<sup>[m](path)</sup>
3. {Action item without citation}
```

**When to apply:**
- Documents with TIPS-style insights
- Strategic recommendations with evidence
- Research reports with actionable guidance
- Any "Begruendung → Umsetzung" pattern

## Consecutive Citation Formatting

### Rule 3: Superscript Commas for Visual Separation

When multiple citations appear consecutively, separate them with superscript commas for visual clarity.

❌ **Bad:**
```markdown
Text with multiple sources<sup>[15](path)</sup><sup>[16](path)</sup><sup>[17](path)</sup>.
```

❌ **Also Bad:**
```markdown
Text with multiple sources<sup>[15](path)</sup>, <sup>[16](path)</sup>, <sup>[17](path)</sup>.
```
(Commas at baseline create visual inconsistency)

✅ **Good:**
```markdown
Text with multiple sources<sup>[15](path)</sup><sup>,</sup> <sup>[16](path)</sup><sup>,</sup> <sup>[17](path)</sup>.
```

**Rationale:**
- Improved visual separation between citation numbers
- Maintains consistent superscript baseline
- Easier to parse citation sequences
- Professional academic appearance

### Pattern Recognition

**Regex pattern to detect:**
```regex
</sup><sup>\[
```

**Replacement pattern:**
```regex
</sup><sup>,</sup> <sup>[
```

**Implementation:**
```bash
# Using perl for reliable replacement
perl -pi -e 's/<\/sup><sup>/<\/sup><sup>,<\/sup> <sup>/g' file.md
```

## Validation Checklist

Before finalizing documents with citations:

- [ ] All citations placed at specific claim level (not section headers)
- [ ] Recommendation lists have citations on individual action items
- [ ] No consecutive citations without superscript comma separation
- [ ] Citation format follows `<sup>[n](path)</sup>` pattern
- [ ] No baseline commas between superscript citations

## Edge Cases

### Single Citation
No comma needed:
```markdown
This claim is supported<sup>[42](path)</sup>.
```

### Two Citations
Single comma:
```markdown
This claim has dual support<sup>[15](path)</sup><sup>,</sup> <sup>[16](path)</sup>.
```

### Three or More Citations
Multiple commas:
```markdown
Extensively documented<sup>[1](path)</sup><sup>,</sup> <sup>[2](path)</sup><sup>,</sup> <sup>[3](path)</sup>.
```

### Mid-Sentence Citations
Same rules apply:
```markdown
Research shows<sup>[5](path)</sup><sup>,</sup> <sup>[6](path)</sup> that performance improves.
```

## Related Patterns

### Obsidian Wikilinks
Citations often link to research entities:
```markdown
<sup>[1](11-insights/insight-id.md)</sup>
<sup>[C1](10-claims/claim-id.md)</sup>
```

### Multiple Citation Styles
Support both numeric and labeled citations:
```markdown
Numeric: <sup>[15](path)</sup>
Labeled: <sup>[C1](path)</sup>
Mixed: <sup>[15](path)</sup><sup>,</sup> <sup>[C2](path)</sup>
```

## Automation

### Post-Processing Script (Optional)

For batch citation formatting:

```bash
#!/bin/bash
# citation-formatter.sh
# Applies both citation formatting rules

FILE="$1"

# Rule 3: Add superscript commas between consecutive citations
perl -pi -e 's/<\/sup><sup>/<\/sup><sup>,<\/sup> <sup>/g' "$FILE"

echo "✓ Citation formatting applied to: $FILE"
```

## See Also
- `markdown-basics.md` (Core markdown syntax)
- `visual-elements.md` (Visual hierarchy principles)

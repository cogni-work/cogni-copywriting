---
title: Markdown Basics Reference
type: formatting-standard
category: formatting
tags: [markdown, syntax, formatting]
audience: [all]
related:
  - visual-elements
  - heading-hierarchy
version: 1.0
last_updated: 2025-10-29
---

# Markdown Basics Reference

## Quick Reference
**Purpose:** Standard markdown syntax for business writing
**Compatibility:** CommonMark specification
**Key principle:** Simple, readable, portable

## Essential Syntax

### Headers
```markdown
# H1 - Document Title
## H2 - Major Section
### H3 - Subsection
#### H4 - Detail Level (max)
```

**Rule:** Max 3 levels (H2-H4), use H1 once only

### Emphasis
```markdown
**Bold text** for key terms, critical findings
*Italic text* for titles, subtle emphasis
***Bold and italic*** for extreme emphasis (rare)
```

### Lists

**Unordered:**
```markdown
- First item
- Second item
- Third item
```

**Ordered:**
```markdown
1. First step
2. Second step
3. Third step
```

**Nested:**
```markdown
- Main point
  - Sub-point A
  - Sub-point B
- Another main point
```

### Links
```markdown
[Link text](https://example.com)
[Link with title](https://example.com "Hover title")
```

### Tables
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |
```

**Alignment:**
```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| L1   | C1     | R1    |
```

### Code

**Inline code:**
```markdown
Use the `calculate_readability.py` script
```

**Code blocks:**
````markdown
```python
def example():
    return "Hello"
```
````

### Block Quotes
```markdown
> This is a quote.
> It can span multiple lines.
>
> — Author Name
```

### Horizontal Rules
```markdown
---
```

or
```markdown
***
```

## Less Common Elements

### Footnotes
```markdown
Here's a sentence with a footnote.[^1]

[^1]: This is the footnote content.
```

### Task Lists
```markdown
- [x] Completed task
- [ ] Pending task
- [ ] Another task
```

### Strikethrough (if supported)
```markdown
~~Deleted text~~
```

## Best Practices

### Spacing
- Blank line before/after headers
- Blank line before/after lists
- Blank line before/after code blocks
- Blank line before/after tables
- Blank line between paragraphs

### Consistency
- Use `-` for unordered lists (not `*`)
- Use `**` for bold (not `__`)
- Use `*` for italic (not `_`)
- Consistent table column width for readability

### Readability
- Keep line length reasonable (80-100 chars)
- Don't mix formatting styles
- Use consistent indentation (2 or 4 spaces)

## Common Mistakes

### Mistake 1: Missing Blank Lines
❌ **Bad:**
```markdown
## Header
Text immediately after header
- List item
```

✅ **Good:**
```markdown
## Header

Text with blank line after header.

- List item
```

### Mistake 2: Inconsistent List Markers
❌ **Bad:**
```markdown
* Item 1
- Item 2
+ Item 3
```

✅ **Good:**
```markdown
- Item 1
- Item 2
- Item 3
```

### Mistake 3: Broken Tables
❌ **Bad:**
```markdown
| Col1 | Col2 |
| Data1 | Data2 |
```
(Missing separator row)

✅ **Good:**
```markdown
| Col1 | Col2 |
|------|------|
| Data1 | Data2 |
```

## See Also
- `visual-elements.md` (Using markdown for visual hierarchy)
- `heading-hierarchy.md` (Header structure standards)

---
title: Heading Hierarchy Standards
type: formatting-standard
category: formatting
tags: [headers, hierarchy, structure, scannability]
audience: [all]
related:
  - visual-elements
  - markdown-basics
version: 1.0
last_updated: 2025-10-29
---

# Heading Hierarchy Standards

## Quick Reference
**Max levels:** 3 (H2, H3, H4 maximum)
**Key principle:** Scannable, keyword-rich, parallel structure
**Target:** Front-load keywords, keep concise

## Heading Levels

### H1 - Document Title (One per document)
```markdown
# Document Title
```
- Used once at document top
- Describes overall content
- 3-8 words ideal
- Keywords front-loaded

### H2 - Major Sections
```markdown
## Major Section Name
```
- Primary content divisions
- Answer-first (Pyramid) or topic-based (traditional)
- 2-6 words ideal
- Parallel structure within document

### H3 - Subsections
```markdown
### Subsection Name
```
- Subdivisions of H2 sections
- Supporting details or categories
- 2-5 words ideal
- Parallel structure within H2

### H4 - Detail Level (Use sparingly)
```markdown
#### Detail Topic
```
- Granular subdivisions (rare)
- Only when absolutely necessary
- 2-4 words ideal
- Consider using bold instead

**Rule:** Never go beyond H4 (####). If you need more levels, restructure.

## Parallel Structure Rules

Headers within the same level must follow consistent grammatical patterns.

### Good (Parallel Verb Forms)
```markdown
## Defining Requirements
## Building Prototypes
## Testing Solutions
## Deploying Systems
```

### Bad (Mixed Forms)
```markdown
## Requirements Definition  (noun)
## Building Prototypes      (verb)
## Test the Solution        (verb + article)
## System Deployment Process (noun phrase)
```

### Good (Parallel Noun Forms)
```markdown
## Architecture Overview
## Implementation Details
## Performance Metrics
## Security Considerations
```

### Good (Parallel Question Forms)
```markdown
## What Is the Problem?
## Why Does It Matter?
## How Do We Solve It?
## When Should We Act?
```

## Keyword Front-Loading

Place important keywords at the beginning of headers for scannability.

✅ **Good (Keywords first):**
- Cost Reduction Strategies
- Performance Optimization Results
- Security Implementation Guide
- Timeline and Milestones

❌ **Poor (Keywords buried):**
- Strategies for Reducing Costs
- Results from Performance Optimization
- A Guide to Implementing Security
- Detailed Timeline Including All Milestones

**Test:** If reader scans only first 2 words of each header, do they understand document structure?

## Header Length Guidelines

| Level | Ideal Length | Maximum | Rationale |
|-------|-------------|---------|-----------|
| H1 | 3-8 words | 12 words | Document overview |
| H2 | 2-6 words | 10 words | Section titles |
| H3 | 2-5 words | 8 words | Subsection clarity |
| H4 | 2-4 words | 6 words | Detail focus |

**Rule:** Shorter is better. If header needs 10+ words, it's probably too complex.

## Headers by Deliverable Type

### Memos
- H1: Memo subject
- H2: BLUF, Background, Details, Next Steps (typically 3-4 H2s)
- H3: Rarely needed (memo should be 1 page)

### Briefs
- H1: Brief title
- H2: Executive Summary, Analysis, Recommendations (3-5 H2s)
- H3: Supporting subcategories under each H2

### Reports
- H1: Report title
- H2: Major chapters/sections (5-10 H2s typical)
- H3: Subsections within chapters (2-5 H3s per H2)
- H4: Only if absolutely necessary

### Proposals
- H1: Proposal title
- H2: Problem, Solution, Benefits, Pricing, Next Steps (5-7 H2s)
- H3: Detail within each section

## Common Patterns

### Answer-First (Pyramid)
```markdown
# Research Findings Report

## Answer
## Three Core Principles
## Supporting Evidence: Architecture
## Supporting Evidence: Process
## Supporting Evidence: Outcomes
## Conclusion
```

### SCQA Structure
```markdown
# Strategic Recommendation

## Situation
## Complication
## Question
## Answer
### Supporting Analysis
### Implementation Plan
### Expected Outcomes
```

### Traditional Structure
```markdown
# Project Status Report

## Executive Summary
## Background
## Current Status
## Challenges
## Next Steps
## Appendices
```

## Scannability Test

Reader should be able to:
1. **Understand document structure** from headers alone (30 seconds)
2. **Navigate to relevant section** using headers
3. **Grasp main topics** without reading body text
4. **Assess document length** from header count

**Test:** Can you answer "What is this document about?" by reading only the headers?

## Common Mistakes

### Mistake 1: Too Many Levels
❌ **Bad:**
```markdown
## Level 2
### Level 3
#### Level 4
##### Level 5 (TOO DEEP)
```
✅ **Good:** Max 3 levels (H2, H3, H4)

### Mistake 2: Inconsistent Structure
❌ **Bad:**
```markdown
## Analyzing Data
## Data Collection
## Why Visualization Matters
```
(Mixed verb/noun forms)

✅ **Good:**
```markdown
## Collecting Data
## Analyzing Data
## Visualizing Results
```
(All verb forms)

### Mistake 3: Verbose Headers
❌ **Bad:** "An Analysis of the Various Factors Contributing to Performance Degradation"
✅ **Good:** "Performance Degradation Factors"

### Mistake 4: Non-Descriptive Headers
❌ **Bad:**
```markdown
## Overview
## Details
## More Information
```
✅ **Good:**
```markdown
## Problem Analysis
## Proposed Solution
## Implementation Timeline
```

## Header Checklist

Before finalizing:

- ☐ Maximum 3 levels used (H2, H3, H4)
- ☐ H1 used exactly once (document title)
- ☐ Parallel structure within each level
- ☐ Keywords front-loaded
- ☐ Headers are scannable (2-6 words each)
- ☐ Structure understandable from headers alone
- ☐ No generic headers ("Overview", "Details")
- ☐ Appropriate header density (not too many, not too few)

## See Also
- `visual-elements.md` (Visual hierarchy complements header hierarchy)
- `markdown-basics.md` (Header syntax details)
- `../01-core-principles/readability-principles.md` (Scannability focus)

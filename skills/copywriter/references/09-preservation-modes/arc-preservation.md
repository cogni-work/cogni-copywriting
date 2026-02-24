# Arc Preservation Mode

## Purpose

When copywriter is invoked to polish research content that uses story arc structures (e.g., Why Change → Why Now → Why You → Why Pay), the heading structure MUST be preserved exactly to maintain narrative integrity.

## What Qualifies as Story Arc Structure

**Story arc structure consists of:**

1. **H1 Title** - Arc-specific title (not generic "Management Summary")
2. **H2 Subtitle** - Research question or executive summary introduction
3. **4 Arc Element Headings** (H2) - Specific to the story arc pattern
4. **Bridge Section** (H2) - "Further Reading" or equivalent linking section

**Example (Corporate Visions Arc):**

```markdown
# The Case for Workflow Redesign

## Healthcare AI Adoption Barriers

[Hook paragraph...]

## Why Change

[Element 1 content...]

## Why Now

[Element 2 content...]

## Why You

[Element 3 content...]

## Why Pay

[Element 4 content...]

## Further Reading

[Bridge content with link to research-report.md]
```

## When to Use Arc Preservation Mode

Arc preservation mode should be activated when:

1. Content is passed from create-insight skill (cogni-research)
2. Explicit arc preservation constraints are provided in the Task prompt
3. Content structure includes H1 + H2 subtitle + 4 element headings + bridge section

## Preservation Requirements

### FORBIDDEN Modifications

**Never modify:**
- H1 title text
- H2 subtitle text
- Any of the 4 arc element heading texts
- Bridge section heading text
- Heading hierarchy (H1/H2 levels)
- Heading order or count

**Example of FORBIDDEN change:**

```markdown
<!-- BEFORE (correct) -->
## Why Change

<!-- AFTER (incorrect) -->
## The Case for Change
```

### ALLOWED Modifications

**Allowed within elements:**
- Improve word choice in body paragraphs
- Enhance Number Plays (e.g., "25%" → "1 in 4")
- Add Power Words to body text (not headings)
- Optimize sentence structure for readability
- Improve transitions between paragraphs

**Example of ALLOWED change:**

```markdown
<!-- BEFORE -->
Companies are adopting AI at 25% rate.

<!-- AFTER -->
Organizations are embracing AI at an accelerating pace—1 in 4 enterprises now deploying production systems.
```

## Validation Requirements

When arc preservation constraints are specified, the invoking skill will validate:

1. **H1 title** - Exact match to original
2. **H2 subtitle** - Exact match to original
3. **4 element headings** - Exact match to original arc pattern
4. **H2 count** - Total of 6 (subtitle + 4 elements + bridge)
5. **Bridge heading** - Match to "Further Reading" or localized equivalent

**If validation fails:**
- Polished output is rejected
- Original unpolished content is used as fallback
- Error is logged with `fallback_reason="arc_structure_violation"`

## Integration Pattern

**Typical invocation from create-insight skill:**

```
CRITICAL PRESERVATION REQUIREMENTS:
1. Citations: <sup>[N](12-synthesis/*.md)</sup> - PRESERVE EXACTLY
2. German characters: ä, ö, ü, ß - PRESERVE EXACTLY (if present)
3. STORY ARC STRUCTURE - PRESERVE EXACTLY:
   - H1 Title: "The Case for Workflow Redesign" - DO NOT MODIFY
   - H2 Subtitle: "Healthcare AI Adoption Barriers" - DO NOT MODIFY
   - Element 1 Heading: "Why Change" - DO NOT MODIFY
   - Element 2 Heading: "Why Now" - DO NOT MODIFY
   - Element 3 Heading: "Why You" - DO NOT MODIFY
   - Element 4 Heading: "Why Pay" - DO NOT MODIFY
   - Bridge Section: "Further Reading" - DO NOT MODIFY

ALLOWED: Improve word choice, enhance Number Plays, optimize sentences
FORBIDDEN: Change any heading text, move content between elements
```

## Story Arc Patterns

Common story arc patterns that require preservation:

### 1. Corporate Visions
- Why Change
- Why Now
- Why You
- Why Pay (or Why Pay More, Why Stay, Why Evolve)

### 2. Technology Futures
- What's Emerging
- What's Converging
- What's Possible
- What's Required

### 3. Competitive Intelligence
- Market Landscape
- Competitive Shifts
- Strategic Positioning
- Business Implications

### 4. Strategic Foresight
- Emerging Signals
- Future Scenarios
- Strategic Options
- Decision Framework

### 5. Industry Transformation
- Driving Forces
- Friction Points
- Evolution Pathways
- Leadership Imperatives

## Benefits of Arc Preservation

**Maintains narrative integrity:**
- Story flow remains consistent with arc definition
- Reader expectations set by headings are met
- Cross-references to specific elements remain valid

**Enables validation:**
- Automated checks can verify structure integrity
- Fallback to unpolished content if structure violated
- Graceful degradation without breaking user workflow

**Supports localization:**
- Headings can be in German or English
- Arc patterns work across languages
- Bridge sections adapt to project language

## Related Documentation

- create-insight skill: `cogni-research/skills/create-insight/SKILL.md`
- Story arc registry: `cogni-research/skills/create-insight/references/story-arc/arc-registry.md`
- Phase 2 workflow: `cogni-research/skills/create-insight/references/phase-workflows/phase-2-polish-optional.md`
- Phase 3 validation: `cogni-research/skills/create-insight/references/phase-workflows/phase-3-validate-and-write.md`

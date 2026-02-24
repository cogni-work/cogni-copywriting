# Arc-Aware Preservation Mode

## Purpose

When the copywriter polishes a narrative that uses story arc structures (created by cogni-narrative), it activates arc-aware preservation mode. This mode preserves arc structure while strengthening arc-specific narrative techniques within each element.

## Activation

Arc-aware mode activates when ANY of these conditions is true:

1. Document YAML frontmatter contains `arc_id` field
2. Explicit arc preservation constraints are provided in the task prompt
3. Document structure matches a known arc pattern (H1 + H2 subtitle + 4 arc element headings + bridge section)

## Arc Detection

**Step 1: Check frontmatter**

```yaml
---
arc_id: corporate-visions  # ← If present, use this arc ID
title: "..."
subtitle: "..."
---
```

**Step 2: If no frontmatter, pattern-match headings against known arcs**

| Arc ID | Element 1 | Element 2 | Element 3 | Element 4 |
|--------|-----------|-----------|-----------|-----------|
| corporate-visions | Why Change | Why Now | Why You | Why Pay |
| technology-futures | What's Emerging | What's Converging | What's Possible | What's Required |
| competitive-intelligence | Landscape | Shifts | Positioning | Implications |
| strategic-foresight | Signals | Scenarios | Strategies | Decisions |
| industry-transformation | Forces | Friction | Evolution | Leadership |

Match H2 headings against the patterns above (partial match on first word is sufficient). If 3+ of 4 elements match, activate arc-aware mode with the matching arc ID.

**Step 3: Load technique map**

```text
READ: references/09-preservation-modes/arc-technique-map.md
```

## Structure Preservation Rules

### FORBIDDEN Modifications

**Never modify:**

- H1 title text
- H2 subtitle text
- Any of the 4 arc element heading texts (exact match required)
- Bridge section heading text (e.g., "Further Reading")
- Heading hierarchy (H1/H2 levels)
- Heading order or count
- Content movement between elements (each element is self-contained)

### ALLOWED Modifications (Arc-Aware)

Within each element, the copywriter MAY:

1. **Strengthen the element's primary technique** — Consult arc-technique-map.md for which technique each element uses, then enhance it (e.g., sharpen PSB pattern in Why Change, tighten forcing functions in Why Now)
2. **Apply the element's Number Play variant** — Use the arc-specific Number Play type from the technique map (e.g., compound impact for Why Pay, ratio framing for Why Change)
3. **Enhance Power Words** — Strengthen verbs in body text. Apply sparingly (3-5 per element). Never in headings.
4. **Improve sentence rhythm** — Vary sentence length. Use short punch sentences after longer setups.
5. **Strengthen You-Phrasing** — Convert third-person to direct address where the technique map marks this technique for the element.
6. **Improve transitions** — Sharpen paragraph transitions within elements. Do NOT modify cross-element transitions (the sentence bridging from one H2 section to the next).

### NEVER in Arc-Aware Mode

- Do NOT apply messaging frameworks (BLUF, Pyramid, SCQA) — the arc IS the structure
- Do NOT restructure element content into a different pattern
- Do NOT merge or split elements
- Do NOT add new sections or headings
- Do NOT change the element's purpose (e.g., turning "Why Now" urgency into "Why Change" problem framing)

## Validation

After polishing, validate:

1. **Structure intact:**
   - H1 title — exact match to original
   - H2 subtitle — exact match to original
   - 4 element headings — exact match to original arc pattern
   - H2 count — total of 6 (subtitle + 4 elements + bridge)
   - Bridge heading — match to "Further Reading" or localized equivalent

2. **Techniques preserved:**
   - Each element's primary technique still present (check against arc-technique-map.md)
   - Number Plays applied using correct variant for each element
   - Word counts within target range (±50 words from arc definition targets)

3. **Content integrity:**
   - Citations preserved (count ≥ original count)
   - German characters preserved (ä, ö, ü, ß)
   - Protected content unchanged (diagram placeholders, figure references)
   - No content moved between elements

**If validation fails:**

- Polished output is rejected
- Original unpolished content is used as fallback
- Error logged with `fallback_reason="arc_structure_violation"` or `fallback_reason="arc_technique_violation"`

## Integration Pattern

**Typical invocation from cogni-narrative or cogni-research:**

```text
CRITICAL PRESERVATION REQUIREMENTS:
1. Citations: <sup>[N](source.md)</sup> — PRESERVE EXACTLY
2. German characters: ä, ö, ü, ß — PRESERVE EXACTLY (if present)
3. STORY ARC STRUCTURE — PRESERVE EXACTLY:
   - arc_id: corporate-visions
   - H1 Title: "The Case for Workflow Redesign" — DO NOT MODIFY
   - H2 Subtitle: "Healthcare AI Adoption Barriers" — DO NOT MODIFY
   - Element headings: Why Change, Why Now, Why You, Why Pay — DO NOT MODIFY
   - Bridge: "Further Reading" — DO NOT MODIFY

ARC-AWARE POLISH: Strengthen techniques per arc-technique-map.md
FORBIDDEN: Change headings, move content between elements, apply messaging frameworks
```

## Localization

Arc element headings may be in German or English. Both are preserved exactly:

| Arc | EN | DE |
|-----|----|----|
| corporate-visions | Why Change | Warum Aendern |
| corporate-visions | Why Now | Warum Jetzt |
| corporate-visions | Why You | Warum Wir |
| corporate-visions | Why Pay | Warum Investieren |

The bridge section adapts to project language:
- EN: "Further Reading"
- DE: "Weiterfuehrende Lektuere"

## Related Documentation

- Arc technique map: `references/09-preservation-modes/arc-technique-map.md`
- cogni-narrative: Creates the story arc narratives that this mode polishes
- cogni-research create-insight: May invoke copywriter with arc preservation constraints

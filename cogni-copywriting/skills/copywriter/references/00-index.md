---
title: Copywriting Skills Master Index
type: index
version: 7.0
last_updated: 2026-02-24
---

# Copywriting Skills Master Index

This index enables progressive disclosure for copywriting tasks. Claude loads only the references needed for the specific deliverable and approach requested.

## How to Use This System

**For users:** Specify your deliverable type and optionally a preferred framework:
- "Write a memo using BLUF"
- "Create a proposal with FAB framework"
- "Draft an executive summary with Pyramid Principle"
- "Write a brief" (framework auto-selected based on deliverable)

**For Claude:** Load references based on user request using this logic:

### Loading Logic

```
IF document has arc_id in frontmatter OR arc preservation requested:
  LOAD: references/09-preservation-modes/arc-preservation.md
  LOAD: references/09-preservation-modes/arc-technique-map.md
  LOAD: references/01-core-principles/ (clarity, conciseness, active-voice)
  SKIP: framework and deliverable type loading (arc IS the structure)
  SET: arc_mode = true

ELSE IF deliverable_type SPECIFIED:
  LOAD: references/04-deliverable-types/{deliverable_type}.md

  IF framework SPECIFIED:
    LOAD: references/02-messaging-frameworks/{framework}-framework.md
  ELSE:
    LOAD: Recommended framework from deliverable reference

  IF deliverable recommends specific principles:
    LOAD: references/01-core-principles/{principles}.md

  IF examples needed:
    LOAD: references/05-examples/example-{deliverable}-{framework}.md

  IF template requested:
    LOAD: references/06-templates/template-{deliverable}.md
```

## Progressive Disclosure Tiers

### Tier 1: Core Principles (ALWAYS LOAD)

**When to load:** Every copywriting task requires core principles.

**Files to load (3 files):**
1. `01-core-principles/clarity-principles.md` - Wolf-Schneider clarity rules, 15-20 word sentences, concrete language
2. `01-core-principles/conciseness-principles.md` - 3-5 sentence paragraphs, eliminating filler, strong verbs
3. `01-core-principles/active-voice-principles.md` - 80%+ active voice, clear subjects, transformation patterns

**Language-conditional core principles:**
- `01-core-principles/german-style-principles.md` - **LOAD WHEN GERMAN detected.** Wolf Schneider Satzbauregeln: 12-Woerter-Teilsaetze, Satzklammer aufbrechen, Mittelfeld verkuerzen, Subjekt-Verb-Naehe, Hauptsaetze reihen, deutsche Floskelliste, Rhythmus durch Abwechslung

**Optional core principles (load when needed):**
- `01-core-principles/plain-language-principles.md` - When technical content needs accessibility
- `01-core-principles/readability-principles.md` - When visual hierarchy and scannability are priorities

**Loading pattern:**
```bash
READ: references/01-core-principles/clarity-principles.md
READ: references/01-core-principles/conciseness-principles.md
READ: references/01-core-principles/active-voice-principles.md

IF document_language == de:
  READ: references/01-core-principles/german-style-principles.md
```

---

### Tier 2: Messaging Frameworks (LOAD BASED ON SELECTION)

**When to load:** After user specifies framework OR after deliverable recommends framework.

**Selection criteria:**
- User explicitly requests framework → Load that framework
- User doesn't specify → Load recommended framework from deliverable reference
- Multiple frameworks suitable → Ask user to choose

**Available frameworks:**

1. **BLUF (Bottom Line Up Front)** - `02-messaging-frameworks/bluf-framework.md`
   - Use when: Time-sensitive, action-required, executive audience
   - Deliverables: Memos, emails, briefs, executive summaries
   - Pattern: Main point + action + deadline in first 1-2 sentences

2. **Pyramid Principle** - `02-messaging-frameworks/pyramid-framework.md`
   - Use when: Complex recommendations, consulting context, structured analysis
   - Deliverables: Reports, briefs, proposals, executive summaries
   - Pattern: Main point → supporting arguments → evidence (MECE structure)

3. **SCQA (Situation-Complication-Question-Answer)** - `02-messaging-frameworks/scqa-framework.md`
   - Use when: Narrative flow needed, problem-solving focus, building urgency
   - Deliverables: Memos, reports, briefs, proposals
   - Pattern: Context → problem → solution question → answer

4. **Inverted Pyramid** - `02-messaging-frameworks/inverted-pyramid-framework.md`
   - Use when: Web content, press releases, scannable documents
   - Deliverables: Reports, emails
   - Pattern: Key information → important details → background

5. **STAR (Situation-Task-Action-Result)** - `02-messaging-frameworks/star-framework.md`
   - Use when: Examples, case studies, behavioral contexts
   - Deliverables: Reports, proposals
   - Pattern: Context → objective → approach → outcome

6. **PSB (Problem-Solution-Benefit)** - `02-messaging-frameworks/psb-framework.md`
   - Use when: Marketing, sales, customer-facing content
   - Deliverables: Proposals, one-pagers, emails
   - Pattern: Pain point → solution → quantified benefits

7. **FAB (Feature-Advantage-Benefit)** - `02-messaging-frameworks/fab-framework.md`
   - Use when: Product focus, technical translation, feature-heavy content
   - Deliverables: Proposals, one-pagers
   - Pattern: Feature → advantage → benefit (for each feature)

**Loading pattern:**
```bash
IF user_specified_framework:
  READ: references/02-messaging-frameworks/{framework}-framework.md
ELSE:
  READ: Recommended framework from deliverable reference
```

---

### Tier 3: Formatting Standards (CONDITIONAL LOAD)

**When to load:** When deliverable requires specific formatting or visual elements.

**Files available:**

1. **visual-elements.md** - `03-formatting-standards/visual-elements.md`
   - Load when: Deliverable needs tables, callouts, lists, emphasis
   - Target density: ~1 visual element per 2 paragraphs
   - Covers: Tables, bullets, callouts, bold emphasis, code blocks

2. **heading-hierarchy.md** - `03-formatting-standards/heading-hierarchy.md`
   - Load when: Document structure needs header standards
   - Guidelines: Max 3 levels (##, ###, ####), front-loaded keywords, parallel structure

3. **markdown-basics.md** - `03-formatting-standards/markdown-basics.md`
   - Load when: User needs markdown syntax reference
   - Covers: Headers, lists, links, emphasis, code blocks, tables

**Loading pattern:**
```bash
IF deliverable_recommends_visuals OR user_requests_visuals:
  READ: references/03-formatting-standards/visual-elements.md

IF deliverable_has_sections OR complex_structure:
  READ: references/03-formatting-standards/heading-hierarchy.md

IF user_needs_markdown_help:
  READ: references/03-formatting-standards/markdown-basics.md
```

---

### Tier 4: Deliverable Types (REQUIRED - LOAD BASED ON TYPE)

**When to load:** After parsing user's deliverable_type parameter (required).

**Files available (8 deliverable types):**

1. **memos.md** - `04-deliverable-types/memos.md`
   - Structure: TO/FROM/DATE/SUBJECT header + BLUF + context + details
   - Length: 1 page typically
   - Formality: Medium
   - Recommended frameworks: BLUF, Pyramid, SCQA

2. **emails.md** - `04-deliverable-types/emails.md`
   - Structure: Subject line + 3-5 paragraphs + clear CTA
   - Length: 200-300 words
   - Formality: Medium
   - Recommended frameworks: BLUF, SCQA

3. **briefs.md** - `04-deliverable-types/briefs.md`
   - Structure: Executive summary + 2-3 supporting sections + next steps
   - Length: 1-3 pages
   - Formality: Medium-high
   - Recommended frameworks: BLUF, Pyramid, SCQA

4. **reports.md** - `04-deliverable-types/reports.md`
   - Structure: Table of contents + structured sections + conclusion
   - Length: Variable (2-100+ pages)
   - Formality: High
   - Recommended frameworks: Pyramid, SCQA, Inverted Pyramid

5. **proposals.md** - `04-deliverable-types/proposals.md`
   - Structure: Exec summary + problem statement + solution + ROI + next steps
   - Length: Variable (3-200 pages)
   - Formality: High
   - Recommended frameworks: FAB, PSB, Pyramid

6. **one-pagers.md** - `04-deliverable-types/one-pagers.md`
   - Structure: High-density single page + visual elements + scannable
   - Length: Exactly 1 page
   - Formality: Medium
   - Recommended frameworks: PSB, FAB

7. **executive-summaries.md** - `04-deliverable-types/executive-summaries.md`
   - Structure: BLUF/Pyramid + condensed key points
   - Length: 1-2 pages maximum
   - Formality: High
   - Recommended frameworks: BLUF, Pyramid

8. **business-letters.md** - `04-deliverable-types/business-letters.md`
   - Structure: Formal header + body + formal close
   - Length: 1 page typically
   - Formality: Very high
   - Recommended frameworks: Direct/Indirect approach

**Loading pattern:**
```bash
READ: references/04-deliverable-types/{deliverable_type}.md
```

---

### Tier 5: Examples (LOAD ON REQUEST OR FOR LEARNING)

**When to load:** When user requests examples OR when demonstrating a new combination.

**Files available:**
- `05-examples/example-memo-bluf.md` - Complete memo with BLUF structure
- `05-examples/example-email-bluf.md` - Complete email with BLUF structure
- `05-examples/example-brief-pyramid.md` - Complete brief with Pyramid structure
- `05-examples/example-proposal-fab.md` - Complete proposal with FAB structure
- Additional examples per deliverable/framework combination

**Loading pattern:**
```bash
IF user_requests_example OR first_time_framework:
  READ: references/05-examples/example-{deliverable}-{framework}.md
```

---

### Tier 6: Templates (LOAD ON REQUEST)

**When to load:** When user explicitly requests template OR wants fillable structure.

**Files available:**
- `06-templates/template-memo.md` - Fillable memo template with placeholders
- `06-templates/template-email.md` - Fillable email template
- `06-templates/template-brief.md` - Fillable brief template
- `06-templates/template-proposal.md` - Fillable proposal template
- Additional templates per deliverable type

**Loading pattern:**
```bash
IF user_requests_template:
  READ: references/06-templates/template-{deliverable}.md
```

---

## Workflow Reference

For detailed step-by-step workflow implementation guidance, load:
- `references/workflow/step-by-step-guide.md` - Complete Steps 1-7 with sub-step details, gate checks, and validation procedures

**When to load workflow guide:**
- Complex copywriting tasks requiring procedural tracking
- First-time users learning the workflow
- When gate checks or validation steps need clarification
- Multi-step document creation with dependencies

---

## Quick Reference by Deliverable

### Emails
- **Primary frameworks:** BLUF, SCQA
- **Key principles:** Clarity, conciseness, active-voice
- **Formality:** Medium
- **Length:** 3-5 paragraphs maximum
- **Load:** Tier 4 (emails.md), Tier 2 (bluf-framework.md), Tier 1 (3 core principles)

### Memos
- **Primary frameworks:** BLUF, Pyramid, SCQA
- **Key principles:** Clarity, conciseness, active-voice
- **Formality:** Medium
- **Length:** 1 page typically
- **Load:** Tier 4 (memos.md), Tier 2 (bluf-framework.md), Tier 1 (3 core principles)

### Reports
- **Primary frameworks:** Pyramid, SCQA, Inverted Pyramid
- **Key principles:** All core principles
- **Formality:** High
- **Length:** Variable (2-100+ pages)
- **Load:** Tier 4 (reports.md), Tier 2 (pyramid-framework.md), Tier 1 (3 core principles)

### Briefs
- **Primary frameworks:** BLUF, Pyramid, SCQA
- **Key principles:** Clarity, conciseness
- **Formality:** Medium-high
- **Length:** 1-3 pages
- **Load:** Tier 4 (briefs.md), Tier 2 (bluf-framework.md), Tier 1 (3 core principles)

### Proposals
- **Primary frameworks:** FAB, PSB, Pyramid
- **Key principles:** Clarity, persuasion-focused
- **Formality:** High
- **Length:** Variable (3-200 pages)
- **Load:** Tier 4 (proposals.md), Tier 2 (fab-framework.md), Tier 1 (3 core principles)

### One-Pagers
- **Primary frameworks:** PSB, FAB
- **Key principles:** Conciseness, visual hierarchy
- **Formality:** Medium
- **Length:** Exactly 1 page
- **Load:** Tier 4 (one-pagers.md), Tier 2 (psb-framework.md), Tier 1 (3 core principles), Tier 3 (visual-elements.md)

### Executive Summaries
- **Primary frameworks:** BLUF, Pyramid
- **Key principles:** Clarity, conciseness
- **Formality:** High
- **Length:** 1-2 pages maximum
- **Load:** Tier 4 (executive-summaries.md), Tier 2 (bluf-framework.md), Tier 1 (3 core principles)

### Business Letters
- **Primary frameworks:** Direct/Indirect approach based on news type
- **Key principles:** All core principles, formality
- **Formality:** Very high
- **Length:** 1 page typically
- **Load:** Tier 4 (business-letters.md), Tier 1 (3 core principles)

## Default Loading Pattern

When deliverable type is unclear or general writing request:
1. Load: `01-core-principles/clarity-principles.md`
2. Load: `01-core-principles/conciseness-principles.md`
3. Load: `01-core-principles/active-voice-principles.md`
4. Ask user to clarify deliverable type for optimal guidance

### Tier 7: Impact Techniques (LOAD FOR HIGH-IMPACT DOCUMENTS)

**When to load:** When `impact_level: high` or audience is executive/C-suite.

**Files available:**

1. **number-plays.md** - `07-impact-techniques/number-plays.md`
   - Ratio framing, specific quantification, comparative anchoring
   - Before/after contrasts, compound impact, Rule of Three numbers
   - Load when: Presenting data, results, benefits, or comparisons

2. **power-words.md** - `07-impact-techniques/power-words.md`
   - Emotional triggers by category (urgency, exclusivity, trust, achievement)
   - Strategic placement guidelines, density control
   - Load when: Writing headlines, CTAs, key benefit statements

3. **rhetorical-devices.md** - `07-impact-techniques/rhetorical-devices.md`
   - Rule of Three, anaphora, antithesis, cadence patterns
   - Device selection by purpose, placement guidelines
   - Load when: Crafting key messages, conclusions, persuasive sections

4. **executive-impact.md** - `07-impact-techniques/executive-impact.md`
   - C-suite optimization, decision-maker patterns
   - Lead with ask, quantify everything, respect time
   - Load when: Writing for executives, board members, senior leadership

**Loading pattern:**

```bash
IF impact_level == high OR audience == executive:
  READ: references/07-impact-techniques/number-plays.md
  READ: references/07-impact-techniques/power-words.md
  READ: references/07-impact-techniques/rhetorical-devices.md
  READ: references/07-impact-techniques/executive-impact.md
```

---

### Tier 8: Sales Techniques (LOAD WHEN MODE: SALES)

**When to load:** When `MODE: sales` is specified or content contains Power Positions.

**Files available:**

1. **power-positions.md** - `08-sales-techniques/power-positions.md`
   - IS-DOES-MEANS message pyramid structure
   - Enhancement rules by layer (specificity, quantification, resonance)
   - Value Wedge criteria, proof point strengthening
   - Structure marker preservation rules
   - Load when: Enhancing sales proposals with Power Positions, value stories

**Loading pattern:**

```bash
IF MODE == sales OR content_contains_power_positions:
  READ: references/08-sales-techniques/power-positions.md
  # Also load Tier 7 impact techniques for synergy
  READ: references/07-impact-techniques/number-plays.md
  READ: references/07-impact-techniques/power-words.md
```

**Integration with Impact Techniques:**

- Number Plays: Apply primarily to DOES layer (quantify outcomes)
- Power Words: Apply primarily to MEANS layer (emotional resonance)
- Both techniques complement Power Positions enhancement

---

### Tier 9: Arc-Aware Preservation (LOAD WHEN ARC DETECTED)

**When to load:** When document has `arc_id` in YAML frontmatter, or arc preservation is requested, or H2 headings match a known arc pattern.

**Files available:**

1. **arc-preservation.md** - `09-preservation-modes/arc-preservation.md`
   - Arc detection logic (frontmatter, pattern matching)
   - Structure preservation rules (FORBIDDEN vs. ALLOWED modifications)
   - Validation requirements (heading integrity, technique integrity)
   - Integration patterns for cogni-narrative and cogni-research
   - Load when: Any story arc narrative is being polished

2. **arc-technique-map.md** - `09-preservation-modes/arc-technique-map.md`
   - Per-arc, per-element technique strengthening rules
   - Number Play variant selection by element (compound impact, ratio framing, etc.)
   - Element-specific polish rules (what to strengthen, what to preserve)
   - Cross-arc technique application table
   - Technique validation checklist
   - Load when: Arc-aware mode is active (always loaded alongside arc-preservation.md)

**Supported arcs:** corporate-visions, technology-futures, competitive-intelligence, strategic-foresight, industry-transformation

**Loading pattern:**

```bash
IF arc_id_detected OR arc_preservation_requested:
  READ: references/09-preservation-modes/arc-preservation.md
  READ: references/09-preservation-modes/arc-technique-map.md
  # Also load core principles (still apply in arc mode)
  READ: references/01-core-principles/clarity-principles.md
  READ: references/01-core-principles/conciseness-principles.md
  READ: references/01-core-principles/active-voice-principles.md
  # Also load impact techniques (applied through arc-technique-map)
  READ: references/07-impact-techniques/number-plays.md
  READ: references/07-impact-techniques/power-words.md
```

**Key rule:** When arc mode is active, do NOT load messaging frameworks or deliverable types. The arc provides the structure. The copywriter strengthens techniques within each element, not restructures.

---

## Architecture Principles

1. **Progressive Disclosure:** Load only what's needed for the specific task
2. **Modular Independence:** Each reference stands alone, no circular dependencies
3. **Consistent Structure:** All references follow standard template (frontmatter, quick reference, detailed content, examples)
4. **Extensibility:** New deliverables reference existing components, no duplication
5. **Quality Standards:** All output targets Flesch 50-60, 3-5 sentences/paragraph, max 3 header levels

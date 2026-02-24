#!/usr/bin/env python3
"""
Calculate readability metrics for markdown documents.

Supports language-aware Flesch scoring:
- English: standard Flesch formula (206.835 - 1.015*ASL - 84.6*ASW)
- German:  Amstad formula (180 - ASL - 58.5*ASW), adapted for German
           compound words and higher syllable counts

Usage:
    python3 calculate_readability.py <file_path> [--lang de|en|auto]

Returns JSON with:
- flesch_score: Flesch Reading Ease score (0-100, target 50-60)
- avg_paragraph_length: Average sentences per paragraph (target 3-5)
- total_paragraphs: Number of paragraphs in document
- visual_elements: Count of tables, callouts, lists, bold sections
- header_levels: Max header depth (target <=3)
- detected_language: Language used for scoring (en or de)
"""

import sys
import re
import json


# --- Language Detection ---

# Common German function words, articles, prepositions, conjunctions
GERMAN_MARKERS = {
    'der', 'die', 'das', 'den', 'dem', 'des',
    'ein', 'eine', 'einer', 'einem', 'einen', 'eines',
    'und', 'oder', 'aber', 'denn', 'weil', 'dass', 'wenn', 'als',
    'ist', 'sind', 'wird', 'werden', 'wurde', 'wurden', 'hat', 'haben',
    'nicht', 'auch', 'noch', 'nur', 'schon', 'sehr',
    'auf', 'aus', 'bei', 'mit', 'nach', 'von', 'vor', 'zu', 'zum', 'zur',
    'sich', 'kann', 'muss', 'soll', 'durch', 'diese', 'dieser', 'diesem',
    'zwischen', 'gegen', 'ohne', 'unter', 'sowie',
}

# Common English function words unlikely in German
ENGLISH_MARKERS = {
    'the', 'and', 'that', 'this', 'with', 'for', 'are', 'was', 'were',
    'been', 'being', 'have', 'has', 'had', 'does', 'did', 'will', 'would',
    'could', 'should', 'may', 'might', 'shall', 'can',
    'not', 'but', 'from', 'they', 'them', 'their', 'which', 'what',
    'when', 'where', 'who', 'whom', 'how', 'than', 'then',
    'into', 'about', 'because', 'between', 'through', 'during',
}


def detect_language(text):
    """Detect whether text is primarily German or English.

    Uses three signals:
    1. German-specific characters (umlauts, eszett)
    2. Function word frequency comparison
    3. Compound word indicators (long words)

    Returns 'de' or 'en'.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return 'en'

    total = len(words)

    # Signal 1: German-specific characters anywhere in the text
    german_chars = len(re.findall(r'[äöüÄÖÜß]', text))
    char_ratio = german_chars / max(len(text), 1)

    # Signal 2: Function word frequency
    de_hits = sum(1 for w in words if w in GERMAN_MARKERS)
    en_hits = sum(1 for w in words if w in ENGLISH_MARKERS)

    de_ratio = de_hits / total
    en_ratio = en_hits / total

    # Signal 3: Long compound words (>=15 chars) are a strong German signal
    long_words = sum(1 for w in words if len(w) >= 15)
    long_ratio = long_words / total

    # Scoring: weighted combination
    de_score = (char_ratio * 100) + (de_ratio * 50) + (long_ratio * 30)
    en_score = (en_ratio * 50)

    return 'de' if de_score > en_score else 'en'


# --- Syllable Counting ---

def count_syllables_en(word):
    """Estimate syllable count for an English word."""
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    previous_was_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            count += 1
        previous_was_vowel = is_vowel

    # Adjust for silent 'e'
    if word.endswith('e'):
        count -= 1

    # Ensure at least 1 syllable
    if count == 0:
        count = 1

    return count


def count_syllables_de(word):
    """Estimate syllable count for a German word.

    German vowel set includes umlauts. No silent-e adjustment
    since German final -e is almost always pronounced (e.g., Hilfe,
    Schule, Ende). Handles diphthongs (ei, eu, au, ie, etc.).
    """
    word = word.lower()
    count = 0
    vowels = "aeiouyäöü"
    previous_was_vowel = False

    i = 0
    while i < len(word):
        char = word[i]
        is_vowel = char in vowels

        if is_vowel:
            if not previous_was_vowel:
                count += 1
            # Check for German diphthongs (count as single syllable)
            # ei, eu, au, äu, ie are common diphthongs
            if i + 1 < len(word) and word[i:i+2] in ('ei', 'eu', 'au', 'ie'):
                i += 1  # skip next vowel, already counted
        previous_was_vowel = is_vowel
        i += 1

    # No silent-e reduction for German
    # Ensure at least 1 syllable
    if count == 0:
        count = 1

    return count


# --- Flesch Scoring ---

def calculate_flesch_score(text, lang='auto'):
    """Calculate Flesch Reading Ease score.

    Uses the standard English formula or the German Amstad (1978)
    formula depending on detected or specified language.

    English: FRE = 206.835 - 1.015 * ASL - 84.6 * ASW
    German:  FRE = 180 - ASL - 58.5 * ASW
    """
    # Remove markdown formatting but keep text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)  # Links
    text = re.sub(r'[*_`#>-]', '', text)  # Markdown symbols

    # Detect language if auto
    if lang == 'auto':
        lang = detect_language(text)

    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return 0, lang

    # Count words
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0, lang

    # Count syllables using language-appropriate function
    syllable_fn = count_syllables_de if lang == 'de' else count_syllables_en
    total_syllables = sum(syllable_fn(word) for word in words)

    total_words = len(words)
    total_sentences = len(sentences)

    asl = total_words / total_sentences  # Average Sentence Length
    asw = total_syllables / total_words  # Average Syllables per Word

    # Apply language-specific formula
    if lang == 'de':
        # Amstad (1978) formula for German
        score = 180 - asl - (58.5 * asw)
    else:
        # Standard English Flesch formula
        score = 206.835 - (1.015 * asl) - (84.6 * asw)

    return round(score, 1), lang


def analyze_document(file_path, lang='auto'):
    """Analyze markdown document for readability metrics."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]

    # Calculate Flesch score
    flesch_score, detected_lang = calculate_flesch_score(content, lang)

    # Analyze paragraphs
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip() and not p.strip().startswith('#')]
    total_paragraphs = len(paragraphs)

    if total_paragraphs > 0:
        total_sentences = sum(len(re.split(r'[.!?]+', p)) - 1 for p in paragraphs)
        avg_paragraph_length = round(total_sentences / total_paragraphs, 1)
    else:
        avg_paragraph_length = 0

    # Count visual elements
    visual_elements = 0

    # Tables
    visual_elements += len(re.findall(r'\|.*\|', content))

    # Callouts (blockquotes with bold text)
    visual_elements += len(re.findall(r'>\s*\*\*', content))

    # Bullet/numbered lists (count list blocks, not individual items)
    list_blocks = re.findall(r'(\n[-*+\d]+\.?\s+.+(\n[-*+\d]+\.?\s+.+)*)', content)
    visual_elements += len(list_blocks)

    # Bold emphasis sections
    visual_elements += len(re.findall(r'\*\*[^*]+\*\*', content))

    # Section dividers
    visual_elements += content.count('---')

    # Analyze header hierarchy
    headers = re.findall(r'^(#+)\s', content, re.MULTILINE)
    max_header_level = max(len(h) for h in headers) if headers else 0

    return {
        "flesch_score": flesch_score,
        "detected_language": detected_lang,
        "avg_paragraph_length": avg_paragraph_length,
        "total_paragraphs": total_paragraphs,
        "visual_elements": visual_elements,
        "header_levels": max_header_level
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: python3 calculate_readability.py <file_path> [--lang de|en|auto]"}))
        sys.exit(1)

    file_path = sys.argv[1]

    # Parse optional --lang argument
    lang = 'auto'
    if '--lang' in sys.argv:
        lang_idx = sys.argv.index('--lang')
        if lang_idx + 1 < len(sys.argv):
            lang = sys.argv[lang_idx + 1]
            if lang not in ('de', 'en', 'auto'):
                print(json.dumps({"error": "Invalid --lang value. Use: de, en, or auto"}))
                sys.exit(1)

    try:
        result = analyze_document(file_path, lang)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

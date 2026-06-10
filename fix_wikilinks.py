#!/usr/bin/env python3
"""Convert [[wikilinks]] to clean [Label](relative/path.md) across all docs."""
import re
import os

DOCS_ROOT = '/home/thinkstation/sda-wiki/docs'

# Clean display name lookup keyed by path-from-docs-root (no leading slash, no .md)
DISPLAY_NAMES = {
    'standards/ela/gr9-10-scales': 'ELA 9-10 Scales',
    'standards/ela/writing-standards': 'Writing Standards',
    'standards/ela/gr9-10-priority': 'Priority by Studio',
    'standards/social-studies/world-history/standards-overview': 'WH Standards Overview',
    'standards/social-studies/world-history/era-1-civilizations': 'Era 1 — Civilizations',
    'standards/social-studies/world-history/era-2-middle-ages': 'Era 2 — Middle Ages',
    'standards/social-studies/world-history/era-3-revolutions': 'Era 3 — Revolutions',
    'standards/social-studies/world-history/era-4-global-war': 'Era 4 — Global War',
    'standards/social-studies/us-history/standards-overview': 'USH Standards Overview',
    'standards/social-studies/us-history/unit-1-industrial': 'Unit 1 — Industrial Revolution',
    'standards/social-studies/us-history/unit-2-imperialism-wwi': 'Unit 2 — Imperialism & WWI',
    'standards/social-studies/us-history/unit-3-roaring-20s': 'Unit 3 — Roaring 20s',
    'standards/social-studies/us-history/unit-4-wwii': 'Unit 4 — WWII',
    'standards/social-studies/us-history/unit-5-cold-war': 'Unit 5 — Cold War',
    'standards/social-studies/us-history/unit-6-civil-rights': 'Unit 6 — Civil Rights',
    'standards/social-studies/us-history/unit-7-vietnam': 'Unit 7 — Vietnam',
    'standards/social-studies/us-history/unit-8-1970s-1980s': 'Unit 8 — 1970s & 1980s',
    'standards/social-studies/us-history/unit-9-1990s-2000s': 'Unit 9 — 1990s–2000s',
    'reading-library/index': 'Reading Library',
    'reading-library/social-studies/hammurabi-code': "Hammurabi's Code",
    'reading-library/social-studies/hammurabi-code': "Hammurabi's Code",
    'reading-library/social-studies/hammurabis-code': "Hammurabi's Code",
    'reading-library/social-studies/magna-carta': 'Magna Carta',
    'reading-library/social-studies/common-sense-paine': 'Common Sense — Paine',
    'reading-library/social-studies/declaration-rights-man': 'Declaration of Rights of Man',
    'reading-library/social-studies/wollstonecraft-vindication': 'Vindication of Rights of Woman',
    'reading-library/social-studies/mlk-letter-birmingham': 'Letter from Birmingham Jail',
    'reading-library/social-studies/analects-confucius': 'Analects of Confucius',
    'reading-library/social-studies/book-of-the-dead-egypt': 'Book of the Dead',
    'reading-library/social-studies/dhammapada-buddhism': 'Dhammapada',
    'reading-library/ela/night-wiesel': 'Night — Wiesel',
    'reading-library/ela/orwell-1984': '1984 — Orwell',
    'reading-library/crosswalk/crosswalk-ela-ss': 'ELA ↔ SS Crosswalk',
    'reading-library/crosswalk/common-sense-w4-crosswalk': 'Common Sense + W.4 Crosswalk',
    'reading-library/crosswalk/letter-birmingham-w4-crosswalk': 'Letter from Birmingham + W.4 Crosswalk',
    'skinnies/world-history/era-1/wh-6-12-2-belief-systems-skinny': 'WH.6_12.2 Belief Systems Skinny',
    'skinnies/world-history/era-1/wh-6-12-3-political-systems-era1-skinny': 'WH.6_12.3 Political Systems Skinny',
    'skinnies/world-history/era-2/wh-6-12-3-medieval-political-skinny': 'WH.6_12.3 Medieval Political Skinny',
    'skinnies/world-history/era-3/wh-6-12-4-revolution-social-economic-skinny': 'WH.6_12.4 Revolution Skinny',
    'skinnies/ela9/r9-informational-argumentative-skinny': 'R.9 Informational/Argumentative Skinny',
    'skinnies/templates/research-skinny': 'Research Skinny Template',
    'resources/index': 'Resource Bank',
    'resources/primary-sources/index': 'Primary Sources',
    'resources/fps-framers/index': 'FPS Framers',
    'resources/ingest': 'Ingest System',
    'crashcourse/world-history/index': 'World History CrashCourse',
    'crashcourse/world-history/ep-01-agricultural-revolution': 'CC — Agricultural Revolution',
    'crashcourse/world-history/ep-09-silk-road': 'CC — Silk Road',
    'crashcourse/world-history/ep-33-french-revolution': 'CC — French Revolution',
    'crashcourse/us-history/index': 'US History CrashCourse',
    'AGENTS': 'AGENTS.md',
    'commons/how-to-sda/index': 'Student Guide',
    'commons/studio-contract-template': 'Studio Contract',
    'index': 'Home',
}

# Standard anchor display names
ANCHOR_DISPLAY = {
    '9-10.R.9': 'R.9',
    '9-10.R.7': 'R.7',
    '9-10.R.4': 'R.4',
    '9-10.R.2': 'R.2',
    '9-10.W.3': 'W.3',
    '9-10.W.4': 'W.4',
    '9-10.C.1': 'C.1',
    'WH.6_12.1': 'WH.6_12.1',
    'WH.6_12.2': 'WH.6_12.2',
    'WH.6_12.3': 'WH.6_12.3',
    'WH.6_12.4': 'WH.6_12.4',
    'WH.6_12.5': 'WH.6_12.5',
    'WH.6_12.6': 'WH.6_12.6',
    'skinny-anatomy': 'Skinny Anatomy',
}

def get_display_name(path, anchor=None):
    clean = path.strip('/')
    if anchor:
        return ANCHOR_DISPLAY.get(anchor, anchor)
    return DISPLAY_NAMES.get(clean, clean.split('/')[-1].replace('-', ' ').replace('_', ' ').title())

def make_link(current_file, target_path, anchor=None):
    """Compute relative markdown link from current_file to target_path."""
    current_dir = os.path.dirname(current_file)
    target_clean = target_path.strip('/')

    # Check if target file exists
    possible_paths = [
        os.path.join(DOCS_ROOT, target_clean + '.md'),
        os.path.join(DOCS_ROOT, target_clean, 'index.md'),
        os.path.join(DOCS_ROOT, target_clean),
    ]

    target_file = None
    for p in possible_paths:
        if os.path.exists(p):
            target_file = p
            break

    if target_file:
        rel = os.path.relpath(target_file, current_dir)
    else:
        # File doesn't exist yet — use absolute path from docs root
        rel = '/' + target_clean + '.md'

    if anchor:
        return rel + '#' + anchor.lower().replace('.', '').replace('_', '-').replace(' ', '-')
    return rel

def convert_wikilink(current_file, match):
    content = match.group(1)

    if '#' in content:
        path, anchor = content.split('#', 1)
    else:
        path, anchor = content, None

    display = get_display_name(path, anchor)
    href = make_link(current_file, path, anchor)

    return f'[{display}]({href})'

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    new_content = re.sub(
        r'\[\[([^\]]+)\]\]',
        lambda m: convert_wikilink(filepath, m),
        content
    )

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False

if __name__ == '__main__':
    count = 0
    for root, dirs, files in os.walk(DOCS_ROOT):
        # Skip hidden dirs
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for fname in sorted(files):
            if fname.endswith('.md'):
                path = os.path.join(root, fname)
                if process_file(path):
                    rel = os.path.relpath(path, DOCS_ROOT)
                    print(f'  updated: {rel}')
                    count += 1
    print(f'\n{count} files updated.')

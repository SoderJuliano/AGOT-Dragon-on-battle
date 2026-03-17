"""Directly read AGOT legwear gene section and find max index."""
import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

agot = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT\common\genes'

# The legwear category is in 07_genes_special_accessories_misc.txt
gf = agot + r'\07_genes_special_accessories_misc.txt'
with open(gf, 'rb') as f:
    raw = f.read()
bom = raw[:3] == b'\xef\xbb\xbf'
content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')

lines = content.splitlines()
# Find all 'index = N' and the template names near them
templates = []
for i, line in enumerate(lines):
    m = re.match(r'\s*(\w+)\s*=\s*\{', line)
    if m:
        name = m.group(1)
        for j in range(i+1, min(i+5, len(lines))):
            idx_m = re.match(r'\s*index\s*=\s*(\d+)', lines[j])
            if idx_m:
                templates.append((int(idx_m.group(1)), name, i+1))
                break

templates.sort()
print(f'Total templates in 07_misc: {len(templates)}')
print('All templates:')
for idx, name, lineno in templates:
    print(f'  index={idx:4d} name={name}')
print(f'Max index: {max(t[0] for t in templates) if templates else "N/A"}')

# Also check Crowns_of_Westeros and other enabled mods for legwear additions
print()
mods_root = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod'
skip = ['AGOT Submod Core', 'AGOT.bk', 'AGOT Submod Core.bk', 'AGOT\\']
import glob
for gf2 in glob.glob(mods_root + r'\**\common\genes\*.txt', recursive=True):
    rel = os.path.relpath(gf2, mods_root)
    if any(s in rel for s in ['AGOT\\', 'AGOT.bk', 'AGOT Submod Core']):
        continue
    with open(gf2, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    cnt = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    if 'legwear' in cnt.lower():
        print(f'LEGWEAR found in: {rel}')
        lines2 = cnt.splitlines()
        for i, line in enumerate(lines2, 1):
            if 'index' in line and re.search(r'index\s*=\s*\d+', line):
                print(f'  line {i}: {line.strip()}')

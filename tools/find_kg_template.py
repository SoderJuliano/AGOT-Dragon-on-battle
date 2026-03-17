"""Find where KG_war_common template is defined and how our mod should hook in."""
import os, sys, glob, re
sys.stdout.reconfigure(encoding='utf-8')

mods = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod'

# Search all gene files for KG_war_common
print('=== Searching for KG_war_common ===')
for gf in glob.glob(mods + r'\**\common\genes\*.txt', recursive=True):
    with open(gf, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    if 'KG_war_common' in content:
        print(f'FOUND in: {os.path.relpath(gf, mods)}')
        # Find context around it
        lines = content.splitlines()
        for i, line in enumerate(lines, 1):
            if 'KG_war_common' in line:
                start = max(0, i-5)
                end = min(len(lines), i+10)
                print(f'  Line {i}:')
                for j in range(start, end):
                    print(f'  {j+1:4d}|{lines[j]}')
                print()

# Search for agot_all_armors to understand that template
print()
print('=== Searching for agot_all_armors in headgear gene files ===')
for gf in glob.glob(mods + r'\**\common\genes\*headgear*.txt', recursive=True):
    with open(gf, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    if 'agot_all_armors' in content:
        print(f'FOUND in: {os.path.relpath(gf, mods)}')
        lines = content.splitlines()
        for i, line in enumerate(lines, 1):
            if 'agot_all_armors' in line:
                start = max(0, i-2)
                end = min(len(lines), i+5)
                for j in range(start, end):
                    print(f'  {j+1:4d}|{lines[j]}')
                print()

# Also check the AGOT headgear gene file for max index and agot_all_armors
print()
print('=== AGOT headgear gene file - last 100 entries ===')
agot_hg = mods + r'\AGOT\common\genes\06_genes_special_accessories_headgear.txt'
with open(agot_hg, 'rb') as f:
    raw = f.read()
bom = raw[:3] == b'\xef\xbb\xbf'
content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
lines = content.splitlines()
# Find all template definitions and their indices
templates = []
for i, line in enumerate(lines):
    m = re.match(r'\s*(\w+)\s*=\s*\{', line)
    if m:
        name = m.group(1)
        # Check if next few lines have index = 
        for j in range(i+1, min(i+5, len(lines))):
            idx_m = re.match(r'\s*index\s*=\s*(\d+)', lines[j])
            if idx_m:
                templates.append((int(idx_m.group(1)), name, i+1))
                break
# Print last 10 templates
print(f'Total templates found: {len(templates)}')
print('Last 10 templates:')
for idx, name, lineno in sorted(templates)[-10:]:
    print(f'  index={idx} name={name} at line {lineno}')
print('Max index:', max(t[0] for t in templates) if templates else 'N/A')

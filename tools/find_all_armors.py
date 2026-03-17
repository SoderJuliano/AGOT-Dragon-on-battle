"""Find agot_all_armors template definition across all gene files."""
import os, sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

mods = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod'
agot = mods + r'\AGOT'

# Search for agot_all_armors in gene files
print('=== agot_all_armors in gene files ===')
for gf in glob.glob(agot + r'\common\genes\*.txt'):
    with open(gf, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    if 'agot_all_armors' in content:
        print(f'Found in: {os.path.basename(gf)}')
        lines = content.splitlines()
        for i, line in enumerate(lines, 1):
            if 'agot_all_armors' in line:
                start = max(0, i-2)
                end = min(len(lines), i+20)
                for j in range(start, end):
                    print(f'  {j+1:5d}|{lines[j]}')
                print()

# Also look at the actual 04_clothes_armor.txt to see full usage
print()
print('=== AGOT 04_clothes_armor.txt (first 150 lines) ===')
pm_path = agot + r'\gfx\portraits\portrait_modifiers\04_clothes_armor.txt'
with open(pm_path, 'rb') as f:
    raw = f.read()
bom = raw[:3] == b'\xef\xbb\xbf'
content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
lines = content.splitlines()
for i, line in enumerate(lines[:150], 1):
    print(f'{i:4d}|{line}')

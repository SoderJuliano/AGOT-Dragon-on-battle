"""Find agot_all_armors in headgear and legwear genes."""
import os, sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

agot = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT'

# Search all AGOT gene files for agot_all_armors
for gf in sorted(glob.glob(agot + r'\common\genes\*.txt')):
    with open(gf, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    if 'agot_all_armors' in content:
        print(f'=== {os.path.basename(gf)} ===')
        lines = content.splitlines()
        for i, line in enumerate(lines, 1):
            if 'agot_all_armors' in line:
                start = max(0, i-1)
                end = min(len(lines), i+5)
                for j in range(start, end):
                    print(f'  {j+1:5d}|{lines[j]}')
                print()

# Read the actual valyrian armor portrait modifier entry that applies valyrian war 02
print()
print('=== Full valyrian_war_02 entry in portrait modifier ===')
pm = agot + r'\gfx\portraits\portrait_modifiers\04_clothes_armor.txt'
with open(pm, 'rb') as f:
    raw = f.read()
bom = raw[:3] == b'\xef\xbb\xbf'
content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
lines = content.splitlines()
# Find valyrian_war_02 entries
for i, line in enumerate(lines, 1):
    if 'valyrian_war_02' in line and 'blackfyre' not in line and 'dynastic' not in line:
        # Find the start of this entry (go back to find the entry name)
        start = i - 1
        while start > 0 and lines[start-1].strip() != '' and not re.match(r'\s+\w+\s*=\s*\{', lines[start-1]):
            start -= 1
        # Find the end (matching brace)
        depth = 0
        end = start
        for j in range(start, min(len(lines), start+60)):
            depth += lines[j].count('{') - lines[j].count('}')
            if j > start and depth <= 0:
                end = j
                break
        print(f'Entry at line {i}:')
        for j in range(max(0,start-2), min(len(lines), end+2)):
            print(f'  {j+1:5d}|{lines[j]}')
        print()
        break  # just show first match

# Also look at agot_most_headgears definition in headgear gene
print()
print('=== agot_most_headgears in headgear gene ===')
hg = agot + r'\common\genes\06_genes_special_accessories_headgear.txt'
with open(hg, 'rb') as f:
    raw = f.read()
content = raw[3:].decode('utf-8')
lines = content.splitlines()
for i, line in enumerate(lines, 1):
    if 'agot_most_headgears' in line:
        start = max(0, i-1)
        end = min(len(lines), i+8)
        for j in range(start, end):
            print(f'{j+1:5d}|{lines[j]}')
        print()
        break

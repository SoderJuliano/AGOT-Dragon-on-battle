"""Find out how AGOT applies headgear for valyrian armor and what template is used."""
import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

agot_pm = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT\gfx\portraits\portrait_modifiers'

# Read 04_headgear_armor.txt - the headgear armor portrait modifier
hg_path = agot_pm + r'\04_headgear_armor.txt'
with open(hg_path, 'rb') as f:
    raw = f.read()
bom = raw[:3] == b'\xef\xbb\xbf'
content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
lines = content.splitlines()

# Find valyrian entries
print('=== 04_headgear_armor.txt valyrian entries ===')
for i, line in enumerate(lines, 1):
    if 'valyrian' in line.lower():
        start = max(0, i - 20)
        end = min(len(lines), i + 5)
        print(f'Context at line {i}:')
        for j in range(start, end):
            print(f'{j+1:5d}|{lines[j]}')
        print()
        break

# Read 00_custom_clothes.txt to see how custom clothes are registered
custom = agot_pm + r'\00_custom_clothes.txt'
with open(custom, 'rb') as f:
    raw = f.read()
bom = raw[:3] == b'\xef\xbb\xbf'
content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
print()
print('=== 00_custom_clothes.txt (first 80 lines) ===')
for i, line in enumerate(content.splitlines()[:80], 1):
    print(f'{i:4d}|{line}')

# Also 00_custom_headgear.txt
custom_hg = agot_pm + r'\00_custom_headgear.txt'
with open(custom_hg, 'rb') as f:
    raw = f.read()
bom = raw[:3] == b'\xef\xbb\xbf'
content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
print()
print('=== 00_custom_headgear.txt (first 80 lines) ===')
for i, line in enumerate(content.splitlines()[:80], 1):
    print(f'{i:4d}|{line}')

# Also 00_custom_legwear.txt
custom_lw = agot_pm + r'\00_custom_legwear.txt'
with open(custom_lw, 'rb') as f:
    raw = f.read()
bom = raw[:3] == b'\xef\xbb\xbf'
content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
print()
print('=== 00_custom_legwear.txt (first 80 lines) ===')
for i, line in enumerate(content.splitlines()[:80], 1):
    print(f'{i:4d}|{line}')

"""Read AGOT Submod Core gene files to understand how custom armors are added."""
import os, sys, glob
sys.stdout.reconfigure(encoding='utf-8')

submod = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT Submod Core'

# List all files
print('=== SUBMOD STRUCTURE ===')
for root, dirs, files in os.walk(submod):
    rel = os.path.relpath(root, submod)
    level = rel.count(os.sep)
    if level > 4:
        continue
    indent = '  ' * level
    bn = os.path.basename(root)
    for f in files:
        print(f'{indent}{bn}/{f}')

print()

# Read the clothes gene file 
gf = submod + r'\common\genes\05_genes_special_accessories_clothes.txt'
if os.path.exists(gf):
    print('=== SUBMOD CORE: 05_genes_special_accessories_clothes.txt ===')
    with open(gf, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    print(f'BOM: {bom}, length: {len(content)}')
    # Find kingsguard references
    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        if 'KG' in line or 'kingsguard' in line.lower() or 'agot_all_armor' in line.lower():
            # Print context
            start = max(0, i-3)
            end = min(len(lines), i+3)
            print(f'--- Found at line {i}:')
            for j in range(start, end):
                print(f'{j+1:5d}|{lines[j]}')
            print()

# Read headgear gene file
gf6 = submod + r'\common\genes\06_genes_special_accessories_headgear.txt'        
if os.path.exists(gf6):
    print('=== SUBMOD CORE: 06_genes_special_accessories_headgear.txt ===')
    with open(gf6, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    print(f'BOM: {bom}')
    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        if 'KG' in line or 'kingsguard' in line.lower() or 'agot_all_armor' in line.lower() or ('agot_most_headgear' in line.lower() and 'index' in lines[i] if i < len(lines) else False):
            start = max(0, i-3)
            end = min(len(lines), i+5)
            print(f'--- Found at line {i}:')
            for j in range(start, end):
                print(f'{j+1:5d}|{lines[j]}')
            print()
    # Also print first 30 lines to see structure
    print('--- First 50 lines:')
    for i, line in enumerate(lines[:50], 1):
        print(f'{i:4d}|{line}')

# Read portrait modifiers
pm_files = glob.glob(submod + r'\**\portrait_modifiers\*.txt', recursive=True)
print()
print('=== SUBMOD PORTRAIT MODIFIERS ===')
for pm in pm_files:
    print(f'File: {os.path.relpath(pm, submod)}')
    with open(pm, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    # Find kingsguard / KG references
    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        if 'KG' in line or 'kingsguard' in line.lower():
            start = max(0, i-5)
            end = min(len(lines), i+5)
            print(f'--- Found at line {i}:')
            for j in range(start, end):
                print(f'{j+1:5d}|{lines[j]}')
            print()

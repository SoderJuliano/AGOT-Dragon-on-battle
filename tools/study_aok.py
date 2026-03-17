"""Study Armor of the Kingsguard mod to understand the correct pattern."""
import os, sys, glob
sys.stdout.reconfigure(encoding='utf-8')

aok = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\Armor of the Kingsguard'

print('=== AOK MOD STRUCTURE ===')
for root, dirs, files in os.walk(aok):
    rel = os.path.relpath(root, aok)
    level = rel.count(os.sep)
    if level > 3:
        continue
    indent = '  ' * level
    print(f'{indent}{os.path.basename(root)}/')
    for f in files:
        print(f'{indent}  {f}')

print()

# Find portrait modifier files in AOK
pm_files = glob.glob(aok + r'\**\portrait_modifiers\*.txt', recursive=True)
pm_files += glob.glob(aok + r'\**\portrait_modifier\*.txt', recursive=True)
print('Portrait modifier files in AOK:')
for pm in pm_files:
    print(' ', os.path.relpath(pm, aok))
    with open(pm, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    print(f'   BOM: {bom}')
    print(content[:2000])
    print('...')
    print()

# Find gene files in AOK
gene_files = glob.glob(aok + r'\**\genes\*.txt', recursive=True)
print('Gene files in AOK:')
for g in gene_files:
    print(' ', os.path.relpath(g, aok))
    with open(g, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    print(f'   BOM: {bom}')
    print(content[:3000])
    print('...')
    print()

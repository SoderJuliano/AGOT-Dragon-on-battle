"""Investigate why templates don't register. Compare our gene file to AGOT's working ones."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

agot = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT\common\genes'
our  = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main\common\genes'

# Read headgear gene file from AGOT to see agot_all_armors template
print('=== AGOT 06_genes_special_accessories_headgear.txt (first 200 lines) ===')
with open(agot + r'\06_genes_special_accessories_headgear.txt', 'rb') as f:
    raw = f.read()
bom = raw[:3] == b'\xef\xbb\xbf'
content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
print(f'BOM: {bom}')
for i, line in enumerate(content.splitlines()[:200], 1):
    print(f'{i:4d}|{line}')

print()

# Read our gene file fully
print('=== OUR 00_dob_headgear_gene.txt ===')
with open(our + r'\00_dob_headgear_gene.txt', 'rb') as f:
    raw = f.read()
bom = raw[:3] == b'\xef\xbb\xbf'
content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
print(f'BOM: {bom}')
for i, line in enumerate(content.splitlines(), 1):
    print(f'{i:4d}|{line}')

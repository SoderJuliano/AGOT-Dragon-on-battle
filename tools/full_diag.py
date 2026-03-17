"""Full diagnostic: read error.log and all key files."""
import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 1. Read error.log - find ALL dob_ errors
log = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\logs\error.log'
with open(log, encoding='utf-8', errors='replace') as f:
    content = f.read()

print('=== ERROR.LOG - All dob_ mentions ===')
matches = list(re.finditer(r'[^\n]*dob_[^\n]*', content))
print(f'Total dob_ lines: {len(matches)}')
for m in matches:
    print(m.group())

print()

# 2. Check gene file
BOM = b'\xef\xbb\xbf'
gene = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main\common\genes\00_dob_headgear_gene.txt'
with open(gene, 'rb') as f:
    raw = f.read()
has_bom = raw[:3] == BOM
content_gene = raw[3:].decode('utf-8') if has_bom else raw.decode('utf-8')
print(f'=== GENE FILE: BOM={has_bom}, size={len(raw)} bytes ===')
print(content_gene)

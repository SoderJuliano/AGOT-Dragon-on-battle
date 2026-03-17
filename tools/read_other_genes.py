"""Read the mystery gene files."""
import os

base = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod'

# Read the mystery clothes fix file
fix_path = base + r'\AGOT-Dragon-on-battle-main\common\genes\00_dob_gene_clothes_fix.txt'
print('=== 00_dob_gene_clothes_fix.txt ===')
with open(fix_path, 'rb') as f:
    raw = f.read()
print('BOM:', raw[:3] == b'\xef\xbb\xbf')
print(raw.decode('utf-8', errors='replace'))
print()

# Read AGOT Submod Core gene files to understand structure
submod_genes = [
    r'AGOT Submod Core\common\genes\valyrian_steel_accessories_misc.txt',
    r'AGOT Submod Core\common\genes\05_genes_special_accessories_clothes.txt',
    r'AGOT Submod Core\common\genes\06_genes_special_accessories_headgear.txt',
]
for rel in submod_genes:
    fpath = base + '\\' + rel
    if os.path.exists(fpath):
        print(f'=== {rel} ===')
        with open(fpath, 'rb') as f:
            raw = f.read()
        print('BOM:', raw[:3] == b'\xef\xbb\xbf')
        content = raw.decode('utf-8', errors='replace')
        print(content[:2000])
        print('...(truncated)')
        print()

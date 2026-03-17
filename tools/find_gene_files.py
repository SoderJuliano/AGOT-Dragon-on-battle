"""Find other submods with gene files and check their structure."""
import os, glob

mods_root = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod'

# Look for gene files in all mods
gene_files = glob.glob(mods_root + r'\**\common\genes\*.txt', recursive=True)
print('All gene files across mods:')
for gf in gene_files:
    rel = gf.replace(mods_root + '\\', '')
    print(' ', rel)

print()

# Specifically look in Armor of Kingsguard
aok_genes = glob.glob(mods_root + r'\*[Kk]ings*\common\genes\*.txt', recursive=True)
aok_genes += glob.glob(mods_root + r'\*[Aa]rmor*\common\genes\*.txt', recursive=True)
print('Armor/Kings gene files:')
for g in aok_genes:
    print(' ', g)
    with open(g, 'rb') as f:
        raw = f.read()
    print('   BOM:', raw[:3] == b'\xef\xbb\xbf')
    print('   Content preview:')
    content = raw.decode('utf-8', errors='replace')
    for line in content.splitlines()[:20]:
        print('   |', line)
    print()

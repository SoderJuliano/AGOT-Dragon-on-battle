"""Write corrected gene file with non-conflicting indices and deploy."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BOM = b'\xef\xbb\xbf'

content = """\ufeffspecial_genes = {
\taccessory_genes = {

\t\theadgear = {
\t\t\tdob_dragon_rider_armor_headgear_tmpl = {
\t\t\t\tindex = 228
\t\t\t\tmale = {
\t\t\t\t\t1 = dob_dragon_rider_armor_headgear
\t\t\t\t}
\t\t\t\tfemale = {
\t\t\t\t\t1 = dob_dragon_rider_armor_headgear
\t\t\t\t}
\t\t\t\tboy = male
\t\t\t\tgirl = female
\t\t\t}
\t\t}

\t\tclothes = {
\t\t\tdob_dragon_rider_armor_clothes_tmpl = {
\t\t\t\tindex = 221
\t\t\t\tmale = {
\t\t\t\t\t1 = dob_dragon_rider_armor_body
\t\t\t\t}
\t\t\t\tfemale = {
\t\t\t\t\t1 = dob_dragon_rider_armor_body
\t\t\t\t}
\t\t\t\tboy = male
\t\t\t\tgirl = female
\t\t\t}
\t\t}

\t\tlegwear = {
\t\t\tdob_dragon_rider_armor_legwear_tmpl = {
\t\t\t\tindex = 35
\t\t\t\tmale = {
\t\t\t\t\t1 = dob_dragon_rider_armor_legwear
\t\t\t\t}
\t\t\t\tfemale = {
\t\t\t\t\t1 = dob_dragon_rider_armor_legwear
\t\t\t\t}
\t\t\t\tboy = male
\t\t\t\tgirl = female
\t\t\t}
\t\t}
\t}
}
"""

SRC  = r'C:\Users\Pedro\Downloads\AGOT-Dragon-on-battle-main'
INST = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main'

# The content string already starts with BOM (\\ufeff), encode as UTF-8
raw = content.encode('utf-8')

for base, label in [(SRC, 'SRC'), (INST, 'INST')]:
    path = base + r'\common\genes\00_dob_headgear_gene.txt'
    with open(path, 'wb') as f:
        f.write(raw)
    # Verify
    with open(path, 'rb') as f:
        check = f.read(3)
    print(f'{label}: Written. BOM={check == BOM}')

print()
print('Content preview:')
for i, line in enumerate(content.splitlines()[:15], 1):
    print(f'{i:3d}|{line}')

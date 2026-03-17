"""Add UTF-8 BOM to all DOB text files that are missing it."""
import os, shutil

SRC  = r'C:\Users\Pedro\Downloads\AGOT-Dragon-on-battle-main'
INST = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main'

BOM = b'\xef\xbb\xbf'

# These files need BOM added
files_to_fix = [
    r'common\genes\00_dob_headgear_gene.txt',
    r'gfx\portraits\accessories\dob_dragon_rider_armor_accessories.txt',
    r'gfx\portraits\portrait_modifiers\04_dob_dragon_rider_armor.txt',
    r'localization\english\dob_dragon_rider_armor_l_english.yml',
    r'localization\english\dragon_battle_l_english.yml',
]

for rel in files_to_fix:
    for base in [SRC, INST]:
        fpath = os.path.join(base, rel)
        if not os.path.exists(fpath):
            print(f'MISSING: {fpath}')
            continue
        with open(fpath, 'rb') as f:
            raw = f.read()
        if raw[:3] == BOM:
            print(f'Already has BOM: {rel} in {"SRC" if base == SRC else "INST"}')
        else:
            # Add BOM
            with open(fpath, 'wb') as f:
                f.write(BOM + raw)
            print(f'ADDED BOM: {rel} in {"SRC" if base == SRC else "INST"}')

print()
print('Done. Verifying...')
for rel in files_to_fix:
    fpath = os.path.join(INST, rel)
    if os.path.exists(fpath):
        with open(fpath, 'rb') as f:
            raw = f.read(3)
        print(f'  {"OK BOM" if raw == BOM else "MISSING BOM!"}: {rel}')

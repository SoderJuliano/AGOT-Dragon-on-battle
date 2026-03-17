"""Remove duplicate DDS files from legwear folder (causes Duplicate texture errors).
CK3's VFS merges all mod folders, so textures from the clothes folder are already accessible.
We should NOT have the same DDS files in both clothes and legwear folders.
"""
import os

INST = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main'
SRC  = r'C:\Users\Pedro\Downloads\AGOT-Dragon-on-battle-main'

legwear_inst = INST + r'\gfx\models\portraits\m_legwear\agot\valyrian\war_02'
legwear_src  = SRC  + r'\gfx\models\portraits\m_legwear\agot\valyrian\war_02'

# These DDS files were copied but are duplicates of files in the clothes folder
# They cause "Duplicate texture" errors - remove them
# The legwear asset references them by name; CK3 will find them in the clothes folder via VFS
dupes_to_remove = [
    'dob_dragon_rider_body_diffuse.dds',
    'valyrian_02_normal.dds',
    'valyrian_02_properties.dds',
]

for fname in dupes_to_remove:
    for folder, label in [(legwear_inst, 'INST'), (legwear_src, 'SRC')]:
        fpath = os.path.join(folder, fname)
        if os.path.exists(fpath):
            os.remove(fpath)
            print(f'REMOVED {label}: {fname}')
        else:
            print(f'Not found {label}: {fname}')

print()
print('=== Remaining legwear files (INST) ===')
for f in os.listdir(legwear_inst):
    print(' ', f)

print()
print('=== Remaining legwear files (SRC) ===')
if os.path.exists(legwear_src):
    for f in os.listdir(legwear_src):
        print(' ', f)
else:
    print('  Folder missing')

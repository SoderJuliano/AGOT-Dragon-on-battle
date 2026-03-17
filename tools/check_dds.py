"""Check DDS file headers to ensure they are valid DDS format."""
import os, struct

def check_dds(path):
    if not os.path.exists(path):
        return f'MISSING: {path}'
    size = os.path.getsize(path)
    with open(path, 'rb') as f:
        magic = f.read(4)
    if magic == b'DDS ':
        return f'OK ({size} bytes): {os.path.basename(path)}'
    else:
        return f'INVALID MAGIC {magic!r} ({size} bytes): {path}'

base_src  = r'C:\Users\Pedro\Downloads\AGOT-Dragon-on-battle-main'
base_inst = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main'

files_to_check = [
    r'gfx\models\portraits\m_clothes\agot\valyrian\war_02\dob_dragon_rider_body_diffuse.dds',
    r'gfx\models\portraits\m_headgear\agot\valyrian\war_03_high\dob_dragon_rider_headgear_diffuse.dds',
]

print('=== DDS VALIDATION (source) ===')
for rel in files_to_check:
    print(check_dds(os.path.join(base_src, rel)))

print()
print('=== DDS VALIDATION (installed) ===')
for rel in files_to_check:
    print(check_dds(os.path.join(base_inst, rel)))

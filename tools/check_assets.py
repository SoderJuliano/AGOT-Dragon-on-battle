import os, shutil

base = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main'
src  = r'C:\Users\Pedro\Downloads\AGOT-Dragon-on-battle-main'
agot = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT'

# Check legwear folder (installed)
leg_folder = base + r'\gfx\models\portraits\m_legwear\agot\valyrian\war_02'
print('=== LEGWEAR FOLDER (installed) ===')
if os.path.exists(leg_folder):
    for f in os.listdir(leg_folder):
        print(' ', f)
else:
    print('  FOLDER MISSING')

# Check headgear folder (installed)
head_folder = base + r'\gfx\models\portraits\m_headgear\agot\valyrian\war_03_high'
print('=== HEADGEAR FOLDER (installed) ===')
if os.path.exists(head_folder):
    for f in os.listdir(head_folder):
        print(' ', f)
else:
    print('  FOLDER MISSING')

# Check clothes folder
clothes_folder = base + r'\gfx\models\portraits\m_clothes\agot\valyrian\war_02'
print('=== CLOTHES FOLDER (installed) ===')
if os.path.exists(clothes_folder):
    for f in os.listdir(clothes_folder):
        print(' ', f)
else:
    print('  FOLDER MISSING')

# Check AGOT legwear folder
leg_agot = agot + r'\gfx\models\portraits\m_legwear\agot\valyrian\war_02'
print('=== AGOT LEGWEAR FOLDER ===')
if os.path.exists(leg_agot):
    for f in os.listdir(leg_agot):
        print(' ', f)
else:
    print('  FOLDER MISSING')

# Check AGOT headgear folder
head_agot = agot + r'\gfx\models\portraits\m_headgear\agot\valyrian\war_03_high'
print('=== AGOT HEADGEAR war_03_high FOLDER ===')
if os.path.exists(head_agot):
    for f in os.listdir(head_agot):
        print(' ', f)
else:
    print('  FOLDER MISSING')

# FIX: copy dob_dragon_rider_body_diffuse.dds to legwear folder
clothes_dds_path = clothes_folder + r'\dob_dragon_rider_body_diffuse.dds'
leg_dds_dest     = leg_folder + r'\dob_dragon_rider_body_diffuse.dds'
print()
print('=== DDS COPY CHECK ===')
print('Source DDS exists:', os.path.exists(clothes_dds_path))
if os.path.exists(clothes_dds_path) and not os.path.exists(leg_dds_dest):
    shutil.copy2(clothes_dds_path, leg_dds_dest)
    print('COPIED dob_dragon_rider_body_diffuse.dds to legwear folder')
elif os.path.exists(leg_dds_dest):
    print('DDS already in legwear folder')
else:
    print('ERROR: source DDS not found!')

# Also ensure same DDS is in headgear source folder? (headgear has its own DDS)
head_src_folder = src + r'\gfx\models\portraits\m_headgear\agot\valyrian\war_03_high'
print()
print('=== HEADGEAR FOLDER (source) ===')
if os.path.exists(head_src_folder):
    for f in os.listdir(head_src_folder):
        print(' ', f)
else:
    print('  FOLDER MISSING')

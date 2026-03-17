import os, shutil

src  = r'C:\Users\Pedro\Downloads\AGOT-Dragon-on-battle-main'
base = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main'

# Check source legwear folder
src_leg = src + r'\gfx\models\portraits\m_legwear\agot\valyrian\war_02'
print('=== SOURCE LEGWEAR FOLDER ===')
if os.path.exists(src_leg):
    for f in os.listdir(src_leg):
        print(' ', f)
else:
    print('  MISSING - creating...')
    os.makedirs(src_leg, exist_ok=True)

# Copy DDS to source legwear if missing
src_clothes = src + r'\gfx\models\portraits\m_clothes\agot\valyrian\war_02'
dds_src = src_clothes + r'\dob_dragon_rider_body_diffuse.dds'
dds_dst = src_leg + r'\dob_dragon_rider_body_diffuse.dds'
if not os.path.exists(dds_dst) and os.path.exists(dds_src):
    shutil.copy2(dds_src, dds_dst)
    print('COPIED DDS to source legwear')
elif os.path.exists(dds_dst):
    print('DDS already in source legwear')
else:
    print('ERROR: source clothes DDS missing')

# Also copy valyrian_02_normal.dds and _properties.dds to legwear folders
# (in case CK3 resolves relative to asset file)
for dds_name in ['valyrian_02_normal.dds', 'valyrian_02_properties.dds']:
    # Source
    src_dds = src_clothes + '\\' + dds_name
    dst_src = src_leg + '\\' + dds_name
    dst_inst = base + r'\gfx\models\portraits\m_legwear\agot\valyrian\war_02\\' + dds_name
    if os.path.exists(src_dds):
        if not os.path.exists(dst_src):
            shutil.copy2(src_dds, dst_src)
            print(f'COPIED {dds_name} to source legwear')
        else:
            print(f'{dds_name} already in source legwear')
        if not os.path.exists(dst_inst):
            shutil.copy2(src_dds, dst_inst)
            print(f'COPIED {dds_name} to installed legwear')
        else:
            print(f'{dds_name} already in installed legwear')
    else:
        print(f'ERROR: {dds_name} not found in source clothes')

# Now verify both installed folders have everything
print()
print('=== INSTALLED LEGWEAR FOLDER ===')
inst_leg = base + r'\gfx\models\portraits\m_legwear\agot\valyrian\war_02'
for f in os.listdir(inst_leg):
    print(' ', f)

# Verify source body.asset has name+index in meshsettings
with open(src + r'\gfx\models\portraits\m_clothes\agot\valyrian\war_02\dob_dragon_rider_armor_body.asset') as f:
    content = f.read()
print()
print('=== SOURCE body.asset has correct meshsettings? ===')
print('name = "male_clothes_secular_valyrian_war_02Shape" present:', 'name = "male_clothes_secular_valyrian_war_02Shape"' in content)
print('index = 0 present:', 'index = 0' in content)

# Check portrait modifier
with open(base + r'\gfx\portraits\portrait_modifiers\04_dob_dragon_rider_armor.txt') as f:
    pm_content = f.read()
print()
print('=== INSTALLED portrait_modifier templates used ===')
import re
for match in re.finditer(r'template\s*=\s*\S+', pm_content):
    print(' ', match.group())

import os

agot = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT'

# Read the blackfyre body asset (our reference)
with open(agot + r'\gfx\models\portraits\m_clothes\agot\valyrian\war_02\male_clothes_secular_valyrian_war_blackfyre_02.asset') as f:
    print('=== AGOT BLACKFYRE body asset ===')
    print(f.read())

# List the AGOT clothes war_02 folder to see if blend shape meshes exist
folder = agot + r'\gfx\models\portraits\m_clothes\agot\valyrian\war_02'
print('=== AGOT CLOTHES war_02 FOLDER ===')
for fname in sorted(os.listdir(folder)):
    print(' ', fname)

"""Find max indices in clothes and legwear gene categories across ALL active mods."""
import os, sys, glob, re
sys.stdout.reconfigure(encoding='utf-8')

mods = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod'

# Active mods (from debug.log) - skip disabled ones
# Enabled: Valyrian_Steel, AGOT More Dragon Eggs, 3324579171, AGOT Better Domain Mgmt,
#           Armor of the Kingsguard, AGOT, Crowns_of_Westeros, AGOT_expanded_Dragons,
#           AGOT-Dragon-on-battle-main, Bookmarked, AGOT expanded travel,
#           Armies of Westeros, AGOT Holdings Art
# Disabled: AGOT Submod Core, Better AI Education, Big Battle View, Canon Children, Battle Graphics*

# Don't include .bk or Submod Core (disabled)
skip_dirs = ['AGOT Submod Core', 'AGOT.bk', 'AGOT Submod Core.bk']

def get_max_index(gene_category_pattern):
    """Find max index for a given gene category across all active mods."""
    max_idx = 0
    for gf in glob.glob(mods + r'\**\common\genes\*.txt', recursive=True):
        # Skip disabled mods
        rel = os.path.relpath(gf, mods)
        if any(skip in rel for skip in skip_dirs):
            continue
        with open(gf, 'rb') as f:
            raw = f.read()
        bom = raw[:3] == b'\xef\xbb\xbf'
        content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
        if gene_category_pattern not in content:
            continue
        # Find templates with indices in this category
        lines = content.splitlines()
        in_category = False
        brace_depth = 0
        for i, line in enumerate(lines):
            if gene_category_pattern in line and '=' in line and '{' in line:
                in_category = True
                brace_depth = 1
                continue
            if in_category:
                brace_depth += line.count('{') - line.count('}')
                if brace_depth <= 0:
                    in_category = False
                    continue
                idx_m = re.match(r'\s*index\s*=\s*(\d+)', line)
                if idx_m:
                    idx = int(idx_m.group(1))
                    if idx > max_idx:
                        max_idx = idx
                        print(f'  New max {idx} in {os.path.relpath(gf, mods)}')
    return max_idx

print('=== Max index in HEADGEAR gene category ===')
hg_max = get_max_index('headgear = {')
print(f'Headgear max: {hg_max}')

print()
print('=== Max index in CLOTHES gene category ===')
cl_max = get_max_index('clothes = {')
print(f'Clothes max: {cl_max}')

print()
print('=== Max index in LEGWEAR gene category ===')
lw_max = get_max_index('legwear = {')
print(f'Legwear max: {lw_max}')

print()
print(f'Safe indices to use:')
print(f'  headgear: {hg_max + 1}')
print(f'  clothes:  {cl_max + 1}')
print(f'  legwear:  {lw_max + 1}')

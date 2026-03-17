"""Find how AGOT applies valyrian armor in portrait modifiers."""
import os, sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

mods = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod'
agot = mods + r'\AGOT'

# Find all portrait modifier files in AGOT
pm_files = glob.glob(agot + r'\gfx\portraits\portrait_modifiers\*.txt')
print(f'AGOT portrait modifier files: {len(pm_files)}')
for f in pm_files:
    print(f'  {os.path.basename(f)}')

print()

# Search for valyrian war armor in portrait modifiers across ALL mods
print('=== Searching for valyrian_war in portrait modifiers ===')
for pm in glob.glob(mods + r'\**\gfx\portraits\portrait_modifiers\*.txt', recursive=True):
    with open(pm, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    if 'valyrian_war' in content.lower() or 'valyrian_war_02' in content.lower():
        rel = os.path.relpath(pm, mods)
        print(f'Found in: {rel}')
        lines = content.splitlines()
        for i, line in enumerate(lines, 1):
            if 'valyrian_war' in line.lower():
                start = max(0, i-8)
                end = min(len(lines), i+5)
                print(f'  Line {i}:')
                for j in range(start, end):
                    print(f'  {j+1:5d}|{lines[j]}')
                print()

print()
print('=== Searching for template = agot_all_armors across all portrait modifiers ===')
for pm in glob.glob(mods + r'\**\gfx\portraits\portrait_modifiers\*.txt', recursive=True):
    with open(pm, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    if 'agot_all_armors' in content:
        rel = os.path.relpath(pm, mods)
        print(f'Found in: {rel}')
        for m in re.finditer(r'.{0,100}agot_all_armors.{0,100}', content):
            print(f'  {m.group()}')
        print()

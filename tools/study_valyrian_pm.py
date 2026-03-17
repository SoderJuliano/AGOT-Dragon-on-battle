"""Find complete valyrian armor portrait modifier entries in AGOT."""
import os, sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

agot = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT\gfx\portraits\portrait_modifiers'

# Find all portrait modifier files
pm_files = sorted(glob.glob(agot + r'\*.txt'))
print(f'Portrait modifier files: {[os.path.basename(f) for f in pm_files]}')
print()

# Search for valyrian_war_blackfyre_02 (the specific armor type we're trying to clone)
for pm in pm_files:
    with open(pm, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    if 'valyrian_war_blackfyre_02' in content or ('valyrian' in content and 'armor' in content.lower()):
        print(f'=== {os.path.basename(pm)} ===')
        lines = content.splitlines()
        for i, line in enumerate(lines, 1):
            if 'valyrian_war_blackfyre_02' in line or 'valyrian_war_02' in line:
                # Find the enclosing entry - look back for the entry name 
                # and forward for all accessories
                start = i - 1
                while start > 5 and not re.match(r'\s{1,8}\w+\s*=\s*\{', lines[start-1]):
                    start -= 1
                depth = 0
                end = start
                for j in range(start, min(len(lines), start+80)):
                    depth += lines[j].count('{') - lines[j].count('}')
                    if j > start and depth <= 0:
                        end = j
                        break
                print(f'Entry found at line {i}:')
                for j in range(max(0, start-1), min(len(lines), end+2)):
                    print(f'{j+1:5d}|{lines[j]}')
                print()
                break

# Also directly search for headgear template usage with valyrian context
print()
print('=== headgear + template in AGOT portrait modifiers ===')
for pm in pm_files:
    with open(pm, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    if 'gene = headgear' in content and 'valyrian' in content:
        lines = content.splitlines()
        prev_template = None
        for i, line in enumerate(lines, 1):
            if 'gene = headgear' in line:
                # Get the template from nearby lines
                for j in range(max(0,i), min(len(lines), i+5)):
                    tm = re.search(r'template\s*=\s*(\S+)', lines[j])
                    if tm:
                        tmpl = tm.group(1)
                        acc_line = next((k for k in range(j, min(len(lines), j+5)) if 'accessory' in lines[k] and '=' in lines[k] and 'mode' not in lines[k]), None)
                        acc = ''
                        if acc_line is not None:
                            am = re.search(r'accessory\s*=\s*(\S+)', lines[acc_line])
                            if am:
                                acc = am.group(1)
                        if 'valyrian' in lines[i-1:j+5][0] if i-1 < len(lines) else False or 'valyrian' in acc:
                            print(f'  {os.path.basename(pm)}:{i}: gene=headgear template={tmpl} accessory={acc}')
                        break

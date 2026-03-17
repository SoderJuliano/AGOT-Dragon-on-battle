"""Study how AOK applies its armor - read key files."""
import os, sys, glob
sys.stdout.reconfigure(encoding='utf-8')

aok = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\Armor of the Kingsguard'

# Read all gfx files
for root, dirs, files in os.walk(aok + r'\gfx'):
    for fname in files:
        fpath = os.path.join(root, fname)
        if fname.endswith('.txt'):
            print(f'=== {os.path.relpath(fpath, aok)} ===')
            with open(fpath, 'rb') as f:
                raw = f.read()
            bom = raw[:3] == b'\xef\xbb\xbf'
            content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
            print(content[:3000])
            print()

# Also read decisions
print('=== DECISIONS ===')
for fname in glob.glob(aok + r'\common\decisions\*.txt'):
    with open(fname, 'rb') as f:
        raw = f.read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    content = raw[3:].decode('utf-8') if bom else raw.decode('utf-8')
    print(content[:5000])

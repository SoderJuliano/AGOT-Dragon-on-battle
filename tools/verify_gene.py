"""Verify installed gene file is correct."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BOM = b'\xef\xbb\xbf'
inst = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main\common\genes\00_dob_headgear_gene.txt'
src  = r'C:\Users\Pedro\Downloads\AGOT-Dragon-on-battle-main\common\genes\00_dob_headgear_gene.txt'

for path, label in [(inst, 'INST'), (src, 'SRC')]:
    with open(path, 'rb') as f:
        raw = f.read()
    has_bom = raw[:3] == BOM
    content = raw[3:].decode('utf-8') if has_bom else raw.decode('utf-8')
    print(f'=== {label}: BOM={has_bom} ===')
    print(content)
    print()

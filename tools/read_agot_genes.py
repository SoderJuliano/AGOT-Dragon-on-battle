"""Read AGOT gene files to understand exact structure."""
import os

agot = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT\common\genes'

# Read the clothes gene file - most relevant
with open(agot + r'\05_genes_special_accessories_clothes.txt', 'rb') as f:
    raw = f.read()
print('05_genes CLOTHES - Has BOM:', raw[:3] == b'\xef\xbb\xbf')
print(raw.decode('utf-8', errors='replace')[:3000])
print('...(truncated)')

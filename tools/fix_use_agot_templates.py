"""Rewrite portrait modifier to use EXISTING AGOT templates and empty the gene file."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BOM = b'\xef\xbb\xbf'

SRC  = r'C:\Users\Pedro\Downloads\AGOT-Dragon-on-battle-main'
INST = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main'

# ── 1. New portrait modifier ──────────────────────────────────────────────────
# Use EXISTING AGOT template names instead of our custom ones:
# - gene=clothes   -> template = agot_all_armors    (defined by AGOT, index 190)
# - gene=legwear   -> template = agot_all_legwear   (defined by AGOT, index 25)
# - gene=headgear  -> template = agot_most_headgears (defined by AGOT, index 217)
pm_content = """\ufeff###############################################################
# DRAGON ON BATTLE - Portrait Modifiers: Dragon Rider's Plate
#
# Usa os templates EXISTENTES do AGOT (agot_all_armors, agot_all_legwear,
# agot_most_headgears) para evitar o problema de templates custom nao
# serem registrados pelo motor do CK3.
###############################################################

# \u2500\u2500 Body + Legwear \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
clothes_armor = {

\tusage = game
\tselection_behavior = weighted_random
\tpriority = 4

\tdob_clothing_dragon_rider_armor = {
\t\tdna_modifiers = {
\t\t\taccessory = {
\t\t\t\tmode = add
\t\t\t\tgene = clothes
\t\t\t\ttemplate = agot_all_armors
\t\t\t\taccessory = dob_dragon_rider_armor_body
\t\t\t}
\t\t\taccessory = {
\t\t\t\tmode = add
\t\t\t\tgene = legwear
\t\t\t\ttemplate = agot_all_legwear
\t\t\t\taccessory = dob_dragon_rider_armor_legwear
\t\t\t}
\t\t\tmorph = {
\t\t\t\tmode = modify_multiply
\t\t\t\tgene = gene_bs_bust
\t\t\t\tvalue = 0.8
\t\t\t\ttemplate = bust_clothes
\t\t\t}
\t\t}
\t\toutfit_tags = { military_outfit }
\t\tweight = {
\t\t\tbase = 0
\t\t\tmodifier = {
\t\t\t\tadd = 1000000
\t\t\t\texists = this
\t\t\t\tagot_has_artifact_equipped = { ARTIFACT_VARIABLE = dob_dragon_rider_armor_artifact }
\t\t\t}
\t\t}
\t}
}

# \u2500\u2500 Headgear override \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
dob_headgear_override = {

\tusage = game
\tselection_behavior = weighted_random
\tpriority = 5

\tdob_headgear_dragon_rider_armor = {
\t\tdna_modifiers = {
\t\t\taccessory = {
\t\t\t\tmode = add
\t\t\t\tgene = headgear
\t\t\t\ttemplate = agot_most_headgears
\t\t\t\taccessory = dob_dragon_rider_armor_headgear
\t\t\t}
\t\t}
\t\toutfit_tags = { military_outfit }
\t\tweight = {
\t\t\tbase = 0
\t\t\tmodifier = {
\t\t\t\tadd = 1000000
\t\t\t\texists = this
\t\t\t\tagot_has_artifact_equipped = { ARTIFACT_VARIABLE = dob_dragon_rider_armor_artifact }
\t\t\t}
\t\t}
\t}
}
"""

# ── 2. New gene file: just empty (no more custom template names) ──────────────
gene_content = """\ufeff# Dragon on Battle - Gene file
# Templates removidos: usar agot_all_armors / agot_all_legwear / agot_most_headgears
# diretamente no portrait modifier. CK3 nao registra template names novos de mods.
"""

# Write portrait modifier
for base, label in [(SRC, 'SRC'), (INST, 'INST')]:
    pm_path   = base + r'\gfx\portraits\portrait_modifiers\04_dob_dragon_rider_armor.txt'
    gene_path = base + r'\common\genes\00_dob_headgear_gene.txt'

    with open(pm_path, 'wb') as f:
        f.write(pm_content.encode('utf-8'))
    with open(gene_path, 'wb') as f:
        f.write(gene_content.encode('utf-8'))

    # Verify BOM
    for path in [pm_path, gene_path]:
        with open(path, 'rb') as f:
            bom_check = f.read(3)
        name = os.path.basename(path)
        print(f'{label} {name}: BOM={bom_check == BOM}')

print()
print('Done. Portrait modifier now uses agot_all_armors/agot_all_legwear/agot_most_headgears.')
print('Gene file is now empty (custom templates removed).')

# Dragon on Battle — AGOT Addon
### Mod para CK3 + A Game of Thrones (AGOT) | v0.1

---

## O que esse mod faz

Adiciona **visibilidade ao sistema de dragões em batalha** do AGOT:

| Recurso | Descrição |
|---|---|
| 🔔 Notificação ao declarar guerra | Mostra o poder do seu dragão |
| 🏆 Evento de vitória | Mostra quanto o dragão contribuiu |
| 💀 Evento de derrota | Idem para derrotas |
| 🏅 Modifier de prestígio (30 dias) | Fama de vencer com dragão (não duplica AGOT) |
| 🛠️ **FIX: More Dragon Eggs crash** | Previne crash `Failed to fetch variable for 'current_rider'` |

### O que o AGOT já faz (nosso mod NÃO duplica):
- **Bonuses de batalha** (advantage, combat_roll, casualty reduction) → AGOT aplica `base_dragon_army_modifier_1-10` automaticamente via story cycle
- **Dragons aliados** no mesmo exército (via `every_knight`) → AGOT já processa
- **Dragon combat events** (dragão vs dragão, vs scorpions) → sistema próprio do AGOT

---

## Descobertas técnicas (AGOT 0.4.27)

### Hook correto para fim de batalha:
```
on_combat_end_winner   ← NÃO on_battle_end_winner!
on_combat_end_loser    ← NÃO on_battle_end_loser!
```
Root nesses scopes = `combat_side` (não character). Acesso via:
- `side_commander` → comandante principal
- `side_primary_participant` → ruler/dono do exército

### Sistema de dragões em batalha do AGOT:
- `dragon_army_modifier_calculation` → chamado da story cycle do dragão a cada 2 dias
- Itera o comandante + knights dragonriders no mesmo exército
- Aplica `base_dragon_army_modifier_1-10` com `days = 2` (refresh constante)
- Modifiers usam `min/max_combat_roll` e `enemy_hard_casualty_modifier`

---

## Como instalar

### ⚠️ IMPORTANTE: Converter para UTF-8 BOM

**O jogo NÃO VAI ABRIR se os arquivos não estiverem em UTF-8 BOM!**

1. **Execute o arquivo `!FIX_ENCODING_UTF8_BOM.bat`** na pasta do mod
   - Isso converte todos os `.txt` e `.yml` para UTF-8 BOM
   - Obrigatório para o CK3 aceitar os arquivos

2. Copie a pasta `AGOT - Dragon on battle` para:
   - **Windows:** `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **Linux:** `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
   
3. Crie um arquivo `dragon_on_battle.mod` na pasta `mod/` com:
   ```
   name = "Dragon on Battle - AGOT Addon"
   path = "mod/AGOT - Dragon on battle"
   ```
   
4. **IMPORTANTE:** Ordem de carregamento no Launcher:
   ```
   1. A Game of Thrones (AGOT)         ← Base obrigatória
   2. AGOT More Dragon Eggs           ← DEVE vir ANTES do Dragon on Battle
   3. [Outros mods AGOT...]
   4. Dragon on Battle                ← Sempre por ÚLTIMO
   ```
   **⚠️ Se carregar na ordem errada, o jogo pode crashar!**

---

## 🛠️ Fix para Crash do More Dragon Eggs

**Problema resolvido:**
```
Error: Failed to fetch variable for 'current_rider' due to not being set
```

Este mod inclui um fix automático que previne crashs quando o More Dragon Eggs (ou outros mods) tentam acessar `var:current_rider` em dragões sem verificar se a variável existe.

**⚠️ ORDEM CRÍTICA:**
O More Dragon Eggs DEVE ser carregado ANTES do Dragon on Battle. Se estiver tendo crashes ao carregar o jogo, verifique a ordem no launcher!

**Como funciona:**
- Anualmente, o mod verifica todos os dragões do seu realm
- Dragões órfãos/selvagens sem `current_rider` recebem um valor padrão
- Previne crash sem afetar a gameplay

**Ordem de load recomendada:**
1. A Game of Thrones (AGOT)
2. AGOT More Dragon Eggs
3. **Dragon on Battle** ← aplica o fix

📄 Detalhes técnicos: [MORE_DRAGON_EGGS_FIX.md](MORE_DRAGON_EGGS_FIX.md)

---

## Estrutura de arquivos

```
AGOT - Dragon on battle/
├── descriptor.mod
├── README.md
├── common/
│   ├── scripted_triggers/
│   │   └── 00_dob_dragon_triggers.txt     ← usa is_current_dragonrider_warfare
│   ├── scripted_values/
│   │   └── 00_dob_dragon_values.txt       ← usa var:current_dragon.dragon_size + dob_dragon_prestige_gain
│   ├── scripted_effects/
│   │   └── 00_dob_dragon_post_combat_effects.txt  ← lógica principal (winner/loser/morte)
│   ├── modifiers/
│   │   └── 00_dob_dragon_modifiers.txt    ← prestígio pós-batalha (não duplica AGOT)
│   └── on_action/
│       └── 00_dob_on_actions.txt          ← on_combat_end_winner/loser + on_war_started
├── events/
│   └── dragon_battle_events.txt
└── localization/
    └── english/
        └── dragon_battle_l_english.yml    ← UTF-8 BOM obrigatório
```

---

## Verificar erros
```
~/.local/share/Paradox Interactive/Crusader Kings III/logs/error.log
```

---

## 🐛 Troubleshooting

### Battle Tier mostrando 0/10

Se o ícone de Battle Tier na janela do dragão mostrar 0/10 para todos os dragões:

1. **Execute** `!FIX_ENCODING_UTF8_BOM.bat` (converte arquivos para UTF-8 BOM)
2. **DELETE** a pasta antiga do mod
3. **Copie** a nova pasta convertida
4. **Feche** o jogo COMPLETAMENTE (não basta F5!)
5. **Reabra** o launcher e carregue o save

O valor correto deve ser **1-10** baseado no tamanho do dragão:
- Size 17-33: Tier 1
- Size 68-84: Tier 4
- Size 136-152: Tier 8
- Size 170+: Tier 10

📄 Detalhes: [FIX_BATTLE_TIER_ZERO.md](FIX_BATTLE_TIER_ZERO.md)

### Jogo crasha ao carregar

**Causa mais comum:** Ordem de carregamento errada no launcher.

**Solução:**
1. More Dragon Eggs deve vir ANTES do Dragon on Battle
2. Dragon on Battle deve ser o ÚLTIMO mod AGOT

📄 Detalhes: [ORDEM_DE_LOAD.txt](ORDEM_DE_LOAD.txt)

---

## Roadmap futuro
- [x] v0.1: Notificações de guerra, vitória e derrota com dragão
- [x] v0.1: Modifier de prestígio pós-batalha (3 tiers por size)
- [x] v0.1: Chance de morte do dragão pós-batalha (20% perdedor, 1% vencedor)
- [ ] v0.2: Notificação quando dragão inimigo vai à batalha contra você
- [ ] v0.3: Ícone de dragão no resumo de batalha (GUI)
- [ ] v0.4: Integração com `dragon_army_modifier_calculation` do AGOT para exibir tier real

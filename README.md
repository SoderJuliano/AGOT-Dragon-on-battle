# Dragon on Battle — AGOT Addon
### Mod para CK3 + A Game of Thrones (AGOT) | v0.2

---

## O que esse mod faz

Adiciona **visibilidade completa ao sistema de dragões em batalha** do AGOT, com eventos, notificações, títulos e feedback de aliados e inimigos.

| Recurso | Descrição |
|---|---|
| 🔔 Guerra declarada por você | Notificação com poder do seu dragão |
| 🛡️ Guerra declarada contra você | Notificação: seu dragão se prepara para defender |
| 🏆 Vitória ofensiva com dragão | Evento com prestígio ganho |
| 🏆 Vitória defensiva com dragão | Evento específico de defesa do território |
| 💀 Derrota ofensiva com dragão | Evento de derrota em ataque |
| 💀 Derrota defensiva com dragão | Evento de derrota defendendo suas terras |
| 🐉 Dragão morto na vitória (1%) | Evento raro — vitória cara demais |
| 🐉 Dragão morto na derrota (20%) | Evento catastrófico de perda |
| 🩸 Dragão ferido (10–35%) | Evento de sobrevivência com cicatrizes |
| 🤝 Relatório: dragão aliado | Situação do dragão do aliado 2 dias após a batalha |
| ⚔️ Relatório: dragão inimigo | Situação do dragão do inimigo 3 dias após |
| 🏅 Modifier de prestígio (30 dias) | Fama de vencer com dragão (3 tiers) |
| 🛡️ **Títulos defensivos permanentes** | Field Guardian → Army Defender → Shield of the Realm |
| 📊 Battle Tier na janela do dragão | Indica o tier de poder (0–10) baseado no `dragon_size` do AGOT |
| 🛠️ **FIX: More Dragon Eggs crash** | Previne crash `Failed to fetch variable for 'current_rider'` |
| 🛠️ **FIX: Battle Tier 0/10** | Pasta `script_values` (sem 'd') carregada corretamente |

### O que o AGOT já faz (nosso mod NÃO duplica):
- **Bonuses de batalha** (advantage, combat_roll, casualty reduction) → AGOT aplica `base_dragon_army_modifier_1-10` automaticamente via story cycle
- **Dragons aliados** no mesmo exército (via `every_knight`) → AGOT já processa
- **Dragon combat events** (dragão vs dragão, vs scorpions) → sistema próprio do AGOT

---

## Fluxo completo de eventos por batalha

```
Dia 0  — Declaração de guerra
           → Se você é o ATACANTE:  evento 001 (seu dragão parte para a guerra)
           → Se você é o DEFENSOR:  evento 008 (seu dragão se prepara para defender)
           → Se um ALIADO IA declara guerra com dragão: evento 004

Dia 1  — Resultado da batalha (seus dragões)
           → Vitória ofensiva:      evento 002
           → Vitória defensiva:     evento 009
           → Derrota ofensiva:      evento 003
           → Derrota defensiva:     evento 010
           → Dragão morto vitória:  evento 005 (ofensivo) / 011 (defensivo)  [1%]
           → Dragão morto derrota:  evento 006 (ofensivo) / 012 (defensivo)  [20%]

Dia 2  — Ferimento + relatório aliados
           → Dragão ferido sobreviveu: evento 007 (ofensivo) / 013 (defensivo) [10%]
           → Para cada dragão ALIADO:  evento 014 (morto / ferido / vivo)

Dia 3  — Relatório inimigos
           → Para cada dragão INIMIGO: evento 015 (morto / ferido / vivo)
```

---

## Títulos defensivos permanentes no dragão

Cada vitória defensiva tem **15% de chance** de conceder o próximo título ao dragão. São permanentes, não expiram, e progridem em ordem:

| Título | Ícone | Prowess | Prestígio mensal | Bônus extra |
|---|---|---|---|---|
| **Field Guardian** | martial_positive | +5 | +0.15 | — |
| **Army Defender** | prowess_positive | +8 | +0.25 | — |
| **Shield of the Realm** | prestige_positive | +12 | +0.40 | stress −5% |

O dragão só pode ter cada título uma vez. Quando tem os três, não ganha mais.

---

## Descobertas técnicas (AGOT 0.4.27)

### Hook correto para fim de batalha:
```
on_combat_end_winner   ← NÃO on_battle_end_winner!
on_combat_end_loser    ← NÃO on_battle_end_loser!
```
Root nesses scopes = `combat_side` (não character). Acesso via:
- `every_side_commander` → itera todos os commanders do lado
- `side_primary_participant` → ruler/dono do exército
- `enemy_side` → acessa o lado oposto

### Detecção de batalha ofensiva vs defensiva:
```
any_character_war = {
    any_war_defender = { this = scope:dob_rider }
}
```
Se `true` → rider é defensor. Caso contrário → atacante.

### Pasta correta para script values no CK3:
```
common/script_values/    ← CORRETO (sem 'd')
common/scripted_values/  ← ERRADO (jogo ignora completamente)
```

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

**Como funciona:**
- Anualmente, o mod verifica todos os dragões do seu realm
- Dragões órfãos/selvagens sem `current_rider` recebem um valor padrão
- Previne crash sem afetar a gameplay

📄 Detalhes técnicos: [MORE_DRAGON_EGGS_FIX.md](MORE_DRAGON_EGGS_FIX.md)

---

## Estrutura de arquivos

```
AGOT - Dragon on battle/
├── descriptor.mod
├── README.md
├── common/
│   ├── scripted_triggers/
│   │   └── 00_dob_dragon_triggers.txt
│   ├── script_values/                              ← sem 'd' (padrão CK3)
│   │   └── 00_dob_dragon_values.txt               ← dob_dragon_battle_tier, dob_dragon_battle_bonus_display, etc.
│   ├── scripted_effects/
│   │   └── 00_dob_dragon_post_combat_effects.txt  ← winner/loser + notificações aliados/inimigos
│   ├── modifiers/
│   │   └── 00_dob_dragon_modifiers.txt            ← prestígio + títulos defensivos permanentes
│   └── on_action/
│       └── 00_dob_on_actions.txt                  ← on_combat_end_winner/loser + on_war_started
├── events/
│   └── dragon_battle_events.txt                   ← eventos 001–015
└── localization/
    └── english/
        └── dragon_battle_l_english.yml            ← UTF-8 BOM obrigatório
```

---

## Verificar erros
```
~/.local/share/Paradox Interactive/Crusader Kings III/logs/error.log
```

---

## 🐛 Troubleshooting

### Battle Tier mostrando 0/10

Problema histórico já resolvido: a pasta estava nomeada como `scripted_values` (com 'd'), que o CK3 ignora completamente. Corrigida para `script_values`.

Se ainda aparecer 0/10:
1. **Execute** `!FIX_ENCODING_UTF8_BOM.bat`
2. **DELETE** a pasta antiga do mod e copie a nova
3. **Feche** o jogo COMPLETAMENTE (não basta F5!)
4. **Reabra** o launcher e carregue o save

📄 Detalhes: [FIX_BATTLE_TIER_ZERO.md](FIX_BATTLE_TIER_ZERO.md)

### Jogo crasha ao carregar

**Causa mais comum:** Ordem de carregamento errada no launcher.

**Solução:**
1. More Dragon Eggs deve vir ANTES do Dragon on Battle
2. Dragon on Battle deve ser o ÚLTIMO mod AGOT

📄 Detalhes: [ORDEM_DE_LOAD.txt](ORDEM_DE_LOAD.txt)

---

## Changelog

### v0.2
- Eventos de guerra **defensiva** (008–013): notificação ao ser atacado, vitória/derrota/morte/ferimento defendendo
- **Relatório de dragões aliados** (evento 014): situação do dragão do aliado 2 dias após a batalha
- **Relatório de dragões inimigos** (evento 015): situação do dragão inimigo 3 dias após
- **Títulos defensivos permanentes** no dragão (Field Guardian / Army Defender / Shield of the Realm)
- Ferimento na derrota (35% chance, 180 dias) — antes inexistente
- Evento 006 (dragão morto em derrota ofensiva) agora disparado corretamente
- **FIX:** pasta renomeada de `scripted_values` → `script_values` (causa raiz do Battle Tier 0/10)
- **FIX:** `dob_dragon_battle_tier` e `dob_dragon_battle_bonus_display` com valores reais (thresholds do AGOT)

### v0.1
- Notificações ao declarar guerra, vitória e derrota com dragão
- Modifier de prestígio pós-batalha (3 tiers por dragon_size)
- Chance de morte do dragão (20% perdedor, 1% vencedor)
- Battle Tier e Combat Effectiveness na janela do dragão
- FIX: crash do More Dragon Eggs (`var:current_rider`)


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

# Dragon on Battle — AGOT Addon
### Mod para CK3 + A Game of Thrones (AGOT) | v0.3

> **Requer:** A Game of Thrones (AGOT) 0.4.27+ | CK3 1.18.3+
> **Compatível com:** More Dragon Eggs (MDE) — com fixes incluídos

---

## O que esse mod faz

Adiciona **visibilidade completa ao sistema de dragões em batalha** do AGOT, com eventos, notificações, títulos permanentes e um painel de relatório de batalha.

| Recurso | Descrição |
|---|---|
| 🔔 War started — você ataca | Notificação com poder do seu dragão |
| 🛡️ War started — você defende | Notificação: seu dragão se prepara para defender |
| 🤝 Aliado declara guerra com dragão | Evento informativo |
| 🏆 Vitória ofensiva | Evento com prestígio ganho |
| 🏆 Vitória defensiva | Evento específico de defesa do território |
| 💀 Derrota ofensiva | Evento de derrota em ataque |
| 💀 Derrota defensiva | Evento de derrota defendendo suas terras |
| 🐉 Dragão morto na vitória (1%) | Evento raro — vitória cara demais |
| 🐉 Dragão morto na derrota (20%) | Evento catastrófico de perda |
| 🩸 Dragão ferido (10–35%) | Evento de sobrevivência com cicatrizes |
| 🤝 Relatório: dragão aliado | Situação do dragão do aliado 2 dias após |
| ⚔️ Relatório: dragão inimigo | Situação do dragão inimigo 3 dias após |
| 🏅 Modifier de prestígio (30 dias) | Fama de vencer com dragão (3 tiers) |
| 🛡️ **Títulos defensivos permanentes** | Field Guardian → Army Defender → Shield of the Realm |
| ⚔️ **Títulos ofensivos permanentes** | The Warbringer → The Realmforged → The Worldbreaker |
| 📊 **Battle Report GUI** | Painel de dragões aliados e inimigos na tela de vitória |
| 📊 Battle Tier na janela do dragão | Tier de poder (0–10) baseado no `dragon_size` |
| ★ **Skybreaker** | Habilidade permanente dada a todo dragão Tier 10 (size ≥ 170) |
| 🛠️ **FIX: MDE crash** | Previne crash `Failed to fetch variable for 'current_rider'` |
| 🛠️ **FIX: Tamanho de dragões** | Corrige `dragon_size` bugado ao entrar no jogo |
| 🛠️ **FIX: Compatibilidade MDE** | Eventos e títulos funcionam com dragões do MDE |

---

## Fluxo completo de eventos por batalha

```
Dia 0  — Declaração de guerra
           → Você ataca com dragão:   evento 001
           → Você defende com dragão: evento 008
           → Aliado IA com dragão:    evento 004

Dia 1  — Resultado da batalha
           → Vitória ofensiva:        evento 002
           → Vitória defensiva:       evento 009
           → Derrota ofensiva:        evento 003
           → Derrota defensiva:       evento 010
           → Dragão morto na vitória: evento 005 (ofensivo) / 011 (defensivo) [1%]
           → Dragão morto na derrota: evento 006 (ofensivo) / 012 (defensivo) [20%]

Dia 2  — Ferimento + relatório aliados + títulos defensivos
           → Dragão ferido sobreviveu:   evento 007 / 013 [10–35%]
           → Dragão aliado IA:           evento 014
           → Título defensivo ganho:     evento 019

Dia 2–4 — Títulos ofensivos (1 evento por título, dias diferentes)
           → The Warbringer ganho:    evento 020 (dia 2)
           → The Realmforged ganho:   evento 021 (dia 3)
           → The Worldbreaker ganho:  evento 022 (dia 4)

Dia 3  — Relatório inimigos
           → Dragão inimigo:          evento 015
```

---

## Títulos defensivos permanentes

Ganhos em **vitórias defensivas** — 15% de chance por vitória. Progridem em ordem, o dragão não pode repetir o mesmo.

| Título | Prowess | Prestígio/mês | Bônus extra |
|---|---|---|---|
| **Field Guardian** | +5 | +0.15 | — |
| **Army Defender** | +8 | +0.25 | — |
| **Shield of the Realm** | +12 | +0.40 | stress −5% |

---

## Títulos ofensivos permanentes

Ganhos em **vitórias ofensivas** — cada um tem roll independente por batalha:

| Título | Chance | Prowess | Prestígio/mês | Bônus extra |
|---|---|---|---|---|
| **The Warbringer** | 55% | +3 | +0.10 | — |
| **The Realmforged** | 40% | +6 | +0.20 | baixas inimigas +5% |
| **The Worldbreaker** | 5% | +15 | +0.60 | baixas inimigas +10%, stress −10% |

> Os rolls são **independentes**: um dragão pode ganhar Warbringer e Realmforged na mesma batalha. Cada título pode ser ganho apenas uma vez.

---

## Tamanho de dragão × Idade (piso mínimo)

O mod aplica automaticamente ao entrar no jogo um piso mínimo de `dragon_size_base` baseado na idade. Isso corrige dragões MDE que ficaram com tamanho abaixo do esperado.

| Idade | `dragon_size_base` mínimo | Dragon Tier equivalente |
|---|---|---|
| < 5 anos | 5 | — |
| 5–9 anos | 15 | — |
| 10–14 anos | 30 | Tier 1 |
| 15–19 anos | 40 | Tier 1 |
| 20–24 anos | 50 | Tier 2 |
| 25–29 anos | 65 | Tier 3 |
| 30–34 anos | 80 | Tier 4 |
| 35–39 anos | 95 | Tier 5 |
| 40–44 anos | 110 | Tier 6 |
| 45–59 anos | 120 | Tier 7 |
| 60–74 anos | 135 | Tier 8 |
| 75–79 anos | 150 | Tier 9 |
| 80+ anos | 175 | Tier 10 |

> O tamanho **nunca é reduzido** — se o AGOT já registrou um valor maior, ele é mantido.

---

## Battle Report GUI

Ao abrir a tela de resumo/detalhes de uma batalha, um painel extra exibe até 3 dragões de cada lado:

- **Nome** do dragão e **rider** (rider mostrado abaixo, em cinza)
- Ícone de 💀 morto ou 🩸 ferido quando aplicável
- Fundo vermelho (morto) ou amarelo (ferido)

Funciona tanto para vitórias quanto para derrotas. Visível apenas quando ao menos um dragão participou.

---

## Compatibilidade com More Dragon Eggs (MDE)

Dragões criados pelo MDE não usam o sistema de registro padrão do AGOT, o que causa:
- `is_current_dragonrider = yes` retorna `false` para dragões MDE
- `dragon_size` retorna `0` mesmo para dragões adultos
- Eventos e títulos nunca disparam

**Fixes incluídos neste mod:**

| Fix | Como funciona |
|---|---|
| `on_game_start`: registra dragões sem story cycle | `agot_dragon_transfer_vars_to_story_cycle_effect` |
| Piso de tamanho por idade no load | Corrige `dragon_size` bugado sem esperar o birthday |
| OR fallback nos triggers de guerra | Usa `var:current_dragon` quando `is_current_dragonrider` falha |
| Remoção de `has_trait = dragonrider` dos loops | MDE não aplica esse trait |
| `every_side_knight` incluído nos loops | Captura riders de dragão que são knights, não commanders |

> **⚠️ Nota:** A decisão "Ride Dragon" do MDE **pode crashar** o jogo se o MDE estiver desatualizado (versão 1.16, incompatível com CK3 1.18). Isso não é causado por este mod.

---

## Como instalar

### ⚠️ IMPORTANTE: UTF-8 BOM

**O jogo NÃO abre arquivos sem UTF-8 BOM!**

1. **Execute** `!FIX_ENCODING_UTF8_BOM.bat` na pasta do mod
2. Copie a pasta para:
   - **Windows:** `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
3. Verifique que `dragon_on_battle.mod` aponta para o caminho correto

### Ordem de carregamento obrigatória

```
1. A Game of Thrones (AGOT)    ← base
2. More Dragon Eggs (MDE)      ← se usar
3. Dragon on Battle            ← SEMPRE por último
```

**⚠️ Ordem errada = crash ao carregar o jogo.**

---

## 🐛 Troubleshooting

### Dragão não aparece no Battle Report

1. Verifique se o `dragon_size` do dragão é > 0 (abra a janela do dragão, olhe o Battle Tier)
2. Se for 0, use a decisão **"Restore Dragon Records"** (em Decisões) — ela corrige dragões MDE com size 0
3. O fix automático roda ao carregar o save, mas só funciona se o dragão já tem `dragon_age` definido

### Battle Tier mostrando 0

1. Execute `!FIX_ENCODING_UTF8_BOM.bat`
2. Delete a pasta antiga do mod e copie a nova versão
3. Feche o jogo completamente (não apenas F5), reabra e carregue o save

### Títulos defensivos/ofensivos não aparecem no dragão

- Os títulos são aplicados no **dragão** como `character_modifier`, visíveis na ficha do dragão
- Para o player, um evento dispara notificando o ganho
- Para dragões de AI: titre aplicado silenciosamente, sem evento

### Jogo crasha usando "Ride Dragon" (decisão do MDE)

Problema no MDE 1.16 — incompatível com CK3 1.18 e AGOT 0.4.27. Não há fix possível sem atualizar o MDE. Evite usar essa decisão específica.

---

## Descobertas técnicas (AGOT 0.4.27)

### Hooks corretos de fim de batalha
```
on_combat_end_winner   ← NÃO on_battle_end_winner
on_combat_end_loser    ← NÃO on_battle_end_loser
```
`root` nesses scopes = `combat_side` (não character).
- `every_side_commander` → itera commanders do lado
- `every_side_knight` → itera cavaleiros (inclui dragonriders que não são commanders)
- `enemy_side { every_side_commander }` → lado oposto

### Detecção ofensiva vs defensiva
```
any_character_war = {
    any_war_defender = { this = scope:dob_rider }
}
```
Se `true` → rider é defensor. Caso contrário → atacante.

### Sistema de storage do AGOT
`dragon_size_base` é armazenado em **dois lugares**: no personagem do dragão (`var:dragon_size_base`) e na story cycle (`gl_dragon_variable_storage`). O AGOT **lê da story cycle**. Qualquer fix de tamanho deve propagar para lá também:
```
every_in_global_list = {
    variable = gl_dragon_variable_storage
    limit = { var:dragon_id ?= scope:meu_dragon }
    set_variable = { name = dragon_size_base value = scope:meu_dragon.var:dragon_size_base }
}
```

### Incompatibilidade MDE — fallback correto
```
OR = {
    is_current_dragonrider = yes
    AND = {
        has_variable = current_dragon
        exists = var:current_dragon
        var:current_dragon = { is_alive = yes has_trait = dragon }
    }
}
```

### Pasta correta para script values
```
common/script_values/    ← CORRETO
common/scripted_values/  ← ERRADO (jogo ignora completamente)
```

---

## Estrutura de arquivos

```
AGOT-Dragon-on-battle/
├── !FIX_ENCODING_UTF8_BOM.bat
├── descriptor.mod
├── README.md
├── common/
│   ├── decisions/
│   │   ├── 00_dob_fix_dragons_decision.txt       ← "Restore Dragon Records"
│   │   └── 00_dob_release_dragon_decision.txt    ← "Sever Dragon Bond"
│   ├── modifiers/
│   │   └── 00_dob_dragon_modifiers.txt           ← prestígio, títulos defensivos e ofensivos
│   ├── on_action/
│   │   └── 00_dob_on_actions.txt                 ← war started, combat end, birthday, game start
│   ├── script_values/
│   │   └── 00_dob_dragon_values.txt              ← dob_dragon_battle_bonus, prestige gain, etc.
│   ├── scripted_effects/
│   │   ├── 00_dob_dragon_post_combat_effects.txt ← winner/loser effects + battle report
│   │   └── 00_dob_fix_mde_dragons.txt            ← fix de tamanho e registro de dragões MDE
│   ├── scripted_guis/
│   │   ├── 00_dob_battle_report_gui.txt          ← ScriptedGUIs do painel de batalha
│   │   └── 00_dob_release_dragon.txt
│   └── scripted_triggers/
│       └── 00_dob_dragon_triggers.txt
├── events/
│   └── dragon_battle_events.txt                  ← eventos 001–022
├── gui/
│   ├── window_battle_summary.gui                 ← override com painel de dragões
│   └── custom_gui/
│       └── agot_dragon_character_window.gui      ← janela do dragão com Battle Tier
└── localization/
    └── english/
        └── dragon_battle_l_english.yml           ← UTF-8 BOM obrigatório
```

---

## Changelog

### v0.3
- **Títulos ofensivos permanentes**: The Warbringer (55%), The Realmforged (40%), The Worldbreaker (5%)
- **Eventos 019–022**: notificações quando dragão ganha título defensivo ou ofensivo
- **Battle Report GUI**: painel de dragões aliados/inimigos na tela de vitória
- **Skybreaker**: habilidade permanente (+5 prowess, +0.5 prestígio/mês, +5% baixas) aplicada a todo dragão Tier 10 (size ≥ 170), no primeiro mês após carregar e no aniversário anual
- **FIX notificações de batalha**: `on_combat_start` não detectava dragões MDE (`has_trait = dragonrider` → OR com fallback `var:current_dragon`)
- **FIX eventos winner/loser**: threshold `dragon_size >= 10` no limite externo bloqueava TODOS os eventos para dragões com size < 10 — reduzido para `>= 1`
- **FIX notificações de aliados e inimigos**: mesmo threshold corrigido em 4 blocos (aliado/inimigo no winner e loser)
- **FIX on load**: tamanho de todos os dragões vivos corrigido ao entrar no jogo (sem esperar birthday)
- **FIX MDE**: removido `has_trait = dragonrider` de todos os loops — dragões MDE agora funcionam
- **FIX MDE**: `every_side_knight` incluído no battle report
- **FIX MDE**: threshold `dragon_size >= 30` reduzido para `>= 10`
- **FIX MDE**: fallback `var:current_dragon` nos triggers de guerra e join war
- **FIX Battle Report**: threshold de gravação baixado para `dragon_size >= 1` — dragões com size bugada aparecem no painel
- **FIX progressão de tier**: faixas de idade divididas em intervalos de 5 anos (20–79) para cobrir todos os tiers sem saltos
- **FIX birthday sync**: handler de aniversário agora sincroniza `dragon_size` além de `dragon_size_base` na story cycle — tier visual atualiza imediatamente

### v0.2
- Eventos de guerra defensiva (008–013)
- Relatório de dragões aliados (evento 014) e inimigos (evento 015)
- Títulos defensivos permanentes: Field Guardian / Army Defender / Shield of the Realm
- Ferimento na derrota (35% chance, 180 dias)
- FIX: pasta `scripted_values` → `script_values` (causa raiz do Battle Tier 0/10)

### v0.1
- Notificações ao declarar guerra, vitória e derrota com dragão
- Modifier de prestígio pós-batalha (3 tiers por dragon_size)
- Chance de morte do dragão (20% perdedor, 1% vencedor)
- Battle Tier e Combat Effectiveness na janela do dragão
- FIX: crash do More Dragon Eggs (`var:current_rider`)

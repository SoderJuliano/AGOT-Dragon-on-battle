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

1. Copie a pasta `AGOT - Dragon on battle` para:
   - **Windows:** `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **Linux:** `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
2. Crie um arquivo `dragon_on_battle.mod` na pasta `mod/` com:
   ```
   name = "Dragon on Battle - AGOT Addon"
   path = "mod/AGOT - Dragon on battle"
   ```
3. Ative o mod no Launcher do CK3 **depois** do AGOT

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

## Roadmap futuro
- [x] v0.1: Notificações de guerra, vitória e derrota com dragão
- [x] v0.1: Modifier de prestígio pós-batalha (3 tiers por size)
- [x] v0.1: Chance de morte do dragão pós-batalha (20% perdedor, 1% vencedor)
- [ ] v0.2: Notificação quando dragão inimigo vai à batalha contra você
- [ ] v0.3: Ícone de dragão no resumo de batalha (GUI)
- [ ] v0.4: Integração com `dragon_army_modifier_calculation` do AGOT para exibir tier real

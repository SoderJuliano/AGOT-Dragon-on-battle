# Fix para Crash do More Dragon Eggs

## Problema Detectado nos Logs

```
[effect_impl_character.cpp:1016]: Command: Failed to fetch variable for 'current_rider' due to not being set
[effect.cpp:1296]: file: events/agot_events/mde_agot_filler_events_dragon.txt line: 282
[on_action.cpp:156]: Error running effect for on action: agot_yearly_owned_dragon_pulse, trigger event: mde_filler_dragon.0003
```

## Causa Raiz

O More Dragon Eggs (ou outro mod) tenta acessar `var:current_rider` em dragões sem verificar se a variável existe. Isso acontece quando:

1. **Dragões selvagens** (nunca tiveram rider)
2. **Dragões órfãos** (rider morreu, variável não foi limpa)
3. **Dragões criados por outros mods** que não seguem o sistema padrão do AGOT

O crash ocorre no on_action `agot_yearly_owned_dragon_pulse` que roda anualmente em TODOS os dragões vivos.

## Solução Implementada

### Arquivo: `common/on_action/00_dob_on_actions.txt`

Adicionado no `dob_on_yearly_pulse`:

```
every_living_dragon = {
    limit = {
        OR = {
            liege = root    # Dragão do player ou vassals
            host = root     # Dragão em dragonpit do player
        }
        NOT = { exists = var:current_rider }
    }
    # Setar current_rider como 0 (null) para prevenir crashes
    set_variable = { name = current_rider value = 0 }
}
```

### Arquivo: `events/dob_mde_crash_fix.txt`

Criado evento hidden de backup (não usado atualmente, mas disponível se necessário).

## Como Funciona

1. **Anualmente**, o Dragon on Battle verifica todos os dragões do realm do player
2. Se um dragão NÃO tem `var:current_rider` setado, inicializa com valor `0`
3. Isso previne o crash quando o More Dragon Eggs (ou outro mod) tenta acessar a variável

## Limitações

- **Só funciona para dragões do player**: Dragões de AI em outros reinos não são tocados (para evitar impacto em performance)
- **Não corrige o bug do More Dragon Eggs**: Apenas previne o crash. O More Dragon Eggs ainda deveria adicionar `exists = var:current_rider` antes de acessar a variável

## Instalação

Este fix já está incluído no Dragon on Battle v0.1+. Basta ativar o mod DEPOIS do AGOT e do More Dragon Eggs no launcher.

## ⚠️ ORDEM DE LOAD CRÍTICA

**IMPORTANTE:** Se a ordem estiver errada, o jogo **IRÁ CRASHAR** ao carregar o save!

```
1. A Game of Thrones (AGOT)          ← Base obrigatória
2. AGOT More Dragon Eggs            ← DEVE vir ANTES do Dragon on Battle
3. Dragon on Battle                 ← SEMPRE por último
```

**Por quê?**
- O Dragon on Battle aplica fixes no sistema de dragões
- Se o More Dragon Eggs carregar DEPOIS, os fixes não são aplicados
- Resultado: crash com `EXCEPTION_ACCESS_VIOLATION`

**Como verificar:**
- No CK3 Launcher, arraste os mods para reordenar
- More Dragon Eggs deve ficar ACIMA na lista
- Dragon on Battle deve ser o ÚLTIMO mod AGOT

## Se o Crash Persistir

### 1. Verificar ordem de load
   - Abra o Launcher
   - Confirme que More Dragon Eggs está ANTES do Dragon on Battle
   - Se estiver invertido, reordene e teste novamente

### 2. Limpar cache do jogo
   - Deletar: `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\cache\`
   - Reabrir o launcher

### 3. Verificar integridade dos arquivos
   - Steam → CK3 → Propriedades → Arquivos locais → Verificar integridade

### 4. Desativar o More Dragon Eggs temporariamente
   - Para confirmar se o problema é realmente desse mod
   - Teste com APENAS: AGOT + Dragon on Battle

### 5. Reportar o bug ao autor do More Dragon Eggs
   - URL: (encontre no Workshop da Steam)
   - Mencionar: "crash in agot_yearly_owned_dragon_pulse when accessing var:current_rider without exists check"

## Informações Técnicas

O arquivo `mde_agot_filler_events_dragon.txt` mencionado no crash log **não existe fisicamente** no More Dragon Eggs instalado. Possíveis causas:

- Cache antigo do jogo
- Arquivo foi renomeado/movido em versão mais nova do mod
- Path virtual gerado pelo engine em tempo de execução
- Conflito entre AGOT base e More Dragon Eggs

Este fix funciona independente da causa raiz, pois garante que `current_rider` sempre existe em dragões acessíveis pelo player.

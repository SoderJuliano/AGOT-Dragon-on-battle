# 🔧 FIX: Battle Tier mostrando 0/10

## Problema

Na janela do dragão, o ícone de "Battle Tier" está mostrando **0/10** para todos os dragões, mesmo dragões grandes.

## Causa

O `scripted_value` estava tentando acessar `dragon_size` incorretamente. Corrigido para usar a sintaxe correta do AGOT.

## Solução Aplicada

**Arquivo modificado:** `common/scripted_values/00_dob_dragon_values.txt`

**Mudança:**
```
dob_dragon_battle_tier = {
    value = 0
    
    if = {
        limit = {
            is_alive = yes
            has_character_flag = dragon
        }
        
        # Usar dragon_size do AGOT diretamente
        add = dragon_size
        divide = 17
        floor = yes
    }
    
    min = 0
    max = 10
}
```

## Como Testar o Fix

### 1️⃣ Converter encoding (se ainda não fez)

```batch
!FIX_ENCODING_UTF8_BOM.bat
```

### 2️⃣ Copiar pasta atualizada

**DELETE** a pasta antiga do mod e copie a nova versão convertida para:
```
C:\Users\SEU_USUARIO\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT - Dragon on battle\
```

### 3️⃣ Reiniciar o jogo COMPLETAMENTE

**IMPORTANTE:** Não basta F5 ou recarregar o save!

1. **Feche** o CK3 completamente (Ctrl+Alt+Del → Processos → Forçar encerramento se necessário)
2. **Abra** o Launcher novamente
3. **Carregue** o save

### 4️⃣ Verificar na janela do dragão

1. Abra a janela de um dragão adulto (size > 17)
2. Veja o ícone de **Battle Tier** (ao lado de Combat Effectiveness)
3. O valor deve mostrar algo entre **1-10** dependendo do tamanho

**Exemplos esperados:**
- Dragão size **17**: Battle Tier = **1**
- Dragão size **34**: Battle Tier = **2**
- Dragão size **68**: Battle Tier = **4**
- Dragão size **97** (Blackfyre na imagem): Battle Tier = **5** ou **6**
- Dragão size **136**: Battle Tier = **8**
- Dragão size **170+**: Battle Tier = **10**

### 5️⃣ Verificar tooltip

Passe o mouse sobre o ícone — deve mostrar:
```
Battle Tier
Tier X/10

This dragon's raw power in battle, based on size.

Size: [número]
(Tier increases with dragon size)
```

## ⚠️ Se AINDA mostrar 0/10

### Verificar erro no log

1. Abra: `Documents\...\Crusader Kings III\logs\error.log`
2. Procure por: **`dob_dragon_battle_tier`**
3. Se houver erro, copie a linha e reporte

### Teste isolado (sem outros mods)

1. **Desative** TODOS os mods exceto:
   - A Game of Thrones (AGOT)
   - Dragon on Battle

2. **Teste** novamente

Se funcionar, algum outro mod estava interferindo.

### Verificar se dragon_size do AGOT funciona

No tooltip do Battle Tier, a linha:
```
Size: [número]
```

**Se mostrar `Size: 0`** → O problema é no AGOT base (dragon_size não está calculando)
**Se mostrar `Size: 97`** (ou outro número) → O problema é na fórmula do Dragon on Battle

## 🎯 Valores de Referência

Para comparar com dragões conhecidos:

| Dragão | Size Aproximado | Battle Tier Esperado |
|--------|-----------------|----------------------|
| Filhote (< 1 ano) | 5-15 | 0 |
| Jovem (1-10 anos) | 17-50 | 1-2 |
| Adulto (10-30 anos) | 51-100 | 3-5 |
| Maduro (30-60 anos) | 101-135 | 6-7 |
| Antigo (60-100 anos) | 136-170 | 8-10 |
| Lendário (100+ anos) | 170+ | 10 (máximo) |

**Blackfyre** na imagem tem 97 anos, então deveria ter size ~136-150 → Battle Tier **8 ou 9**.

Se estiver mostrando 0, o cálculo não está funcionando.

## 🔍 Debug Avançado

Se você souber editar arquivos:

### Testar se dragon_size funciona

Adicione um texto debug na GUI:

**Arquivo:** `gui/custom_gui/agot_dragon_character_window.gui`

Procure pela seção do Battle Tier e adicione:

```gui
text_single = {
    name = "debug_dragon_size"
    text = "DEBUG Size: [CharacterWindow.GetCharacter.MakeScope.ScriptValue('dragon_size')|0]"
    align = nobaseline
}
```

Se mostrar "DEBUG Size: 0", o problema é no AGOT.
Se mostrar um número válido, o problema é na nossa fórmula.

---

**Resumo:** Execute `!FIX_ENCODING_UTF8_BOM.bat`, copie o mod atualizado, feche o jogo completamente, reabra e teste.

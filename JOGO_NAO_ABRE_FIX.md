# 🚨 FIX URGENTE — Jogo não abre

## Problema identificado nos logs:

```
Error: "Unexpected token: prestige_gain_mult" in common/modifiers/00_dob_dragon_modifiers.txt
File should be in utf8-bom encoding (will try to use it anyways)
```

---

## ✅ SOLUÇÃO (2 minutos):

### 1️⃣ Converter encoding (OBRIGATÓRIO)

Execute o arquivo na pasta do mod:
```
!FIX_ENCODING_UTF8_BOM.bat
```

Isso converte todos os `.txt` e `.yml` para UTF-8 BOM (exigido pelo CK3).

### 2️⃣ Aplicar fix no modifier (JÁ FEITO)

O modificador inválido `prestige_gain_mult` foi removido. Se você baixou a versão mais recente, já está corrigido.

**Antes (causava crash):**
```
prestige_gain_mult = 0.05  ← NÃO EXISTE no CK3!
```

**Depois (correto):**
```
monthly_prestige = 2  ← Funciona
```

---

## 🎮 Como testar se funcionou:

1. **Execute** `!FIX_ENCODING_UTF8_BOM.bat`
2. **Copie** a pasta para `Documents\Paradox Interactive\Crusader Kings III\mod\`
3. **Abra** o CK3 Launcher
4. **Ative** o mod (DEPOIS do AGOT)
5. **Jogue** normalmente

Se ainda crashar:
- Veja `Documents\...\logs\error.log`
- Procure por linhas com "dob_" ou "dragon_battle"
- Reporte aqui

---

## 📋 Modificadores que EXISTEM no CK3 (referência):

✅ **Válidos para character modifiers:**
- `monthly_prestige`
- `monthly_prestige_gain`
- `prestige` (valor fixo)
- `stress_gain_mult`
- `stress_loss_mult`
- `prowess`
- `monthly_character_prestige`

❌ **NÃO existem:**
- `prestige_gain_mult` ← esse foi o problema!
- `prestige_per_month`
- `prestige_mult`

---

## 🔧 Outros erros comuns:

### "Failed to find script_value: dob_dragon_battle_bonus"
**Causa:** Arquivo `00_dob_dragon_values.txt` não está em UTF-8 BOM  
**Fix:** Rode o `.bat` de conversão

### "Unrecognized loc key: dragon_battle.005.t"
**Causa:** Arquivo de localization sem UTF-8 BOM  
**Fix:** Rode o `.bat` de conversão

### "Unknown iterator: every_living_dragon"
**Causa:** AGOT não está ativado no launcher  
**Fix:** Ative AGOT ANTES do Dragon on Battle

---

## 📞 Se nada funcionar:

1. Desative TODOS os mods
2. Ative APENAS o AGOT
3. Confirme que o jogo abre
4. Ative o Dragon on Battle
5. Se crashar, envie o `error.log` completo

---

## ✨ Versão corrigida:

Todos os arquivos no diretório `c:\Users\Pedro\Downloads\AGOT-Dragon-on-battle-main\` já estão com:
- ✅ `prestige_gain_mult` removido
- ✅ Localizações dos eventos 004-007 adicionadas
- ✅ Fix do More Dragon Eggs aplicado

**Basta rodar o `.bat` e copiar para a pasta de mods!**

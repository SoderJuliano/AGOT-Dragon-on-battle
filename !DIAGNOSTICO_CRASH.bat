@echo off
chcp 65001 >nul
:: ===================================================================
:: Diagnóstico de Crash - Dragon on Battle
:: Verifica se o mod está instalado corretamente e analisa logs
:: ===================================================================

echo.
echo ========================================
echo  Dragon on Battle - Diagnostico
echo ========================================
echo.

set "MODPATH=%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT - Dragon on battle"
set "LOGPATH=%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III"

:: ===== VERIFICAR SE O MOD ESTÁ INSTALADO =====
echo [1/4] Verificando instalacao do mod...
if exist "%MODPATH%\descriptor.mod" (
    echo [OK] Mod encontrado em: %MODPATH%
) else (
    echo [ERRO] Mod NAO encontrado!
    echo       Copie a pasta para: %MODPATH%
    pause
    exit /b 1
)

:: ===== VERIFICAR ENCODING UTF-8 BOM =====
echo.
echo [2/4] Verificando encoding dos arquivos...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference = 'SilentlyContinue'; $files = Get-ChildItem -Path '%MODPATH%' -Include *.txt,*.yml -Recurse -File | Select-Object -First 5; $hasErrors = $false; foreach ($file in $files) { $bytes = [System.IO.File]::ReadAllBytes($file.FullName); if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) { Write-Host \"[OK] UTF-8 BOM: $($file.Name)\" -ForegroundColor Green; } else { Write-Host \"[ERRO] Sem BOM: $($file.Name)\" -ForegroundColor Red; $hasErrors = $true; } } if ($hasErrors) { Write-Host \"`nARQUIVOS SEM UTF-8 BOM ENCONTRADOS!\" -ForegroundColor Red; Write-Host \"Execute: !FIX_ENCODING_UTF8_BOM.bat\" -ForegroundColor Yellow; exit 1; }"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Execute o !FIX_ENCODING_UTF8_BOM.bat e copie novamente!
    pause
    exit /b 1
)

:: ===== ANALISAR ERROR.LOG =====
echo.
echo [3/4] Analisando error.log...
if exist "%LOGPATH%\logs\error.log" (
    findstr /C:"dob_" /C:"dragon_battle" "%LOGPATH%\logs\error.log" > nul
    if %ERRORLEVEL% EQU 0 (
        echo [AVISO] Erros do Dragon on Battle encontrados:
        findstr /C:"dob_" /C:"dragon_battle" "%LOGPATH%\logs\error.log" | findstr /C:"[E]" | more
    ) else (
        echo [OK] Nenhum erro do Dragon on Battle no log
    )
) else (
    echo [INFO] error.log nao encontrado (jogo ainda nao foi executado?)
)

:: ===== VERIFICAR CONFLITOS COM OUTROS MODS =====
echo.
echo [4/4] Verificando conflitos com outros mods AGOT...
echo.
echo IMPORTANTE: ORDEM DE CARREGAMENTO
echo.
echo Se voce tem More Dragon Eggs instalado, a ordem DEVE ser:
echo   1. A Game of Thrones (AGOT)
echo   2. AGOT More Dragon Eggs          ^<-- PRIMEIRO
echo   3. [Outros mods AGOT...]
echo   4. Dragon on Battle               ^<-- POR ULTIMO
echo.
echo Se o More Dragon Eggs vier DEPOIS do Dragon on Battle,
echo o jogo vai crashar ao carregar!
echo.
echo Mods AGOT detectados:
echo.

dir /b "%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT*" 2>nul
dir /b "%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\*Dragon*" 2>nul | findstr /V /I "AGOT-Dragon-on-battle" 2>nul

echo.
echo ========================================
echo  Diagnostico Completo
echo ========================================
echo.
echo PROXIMOS PASSOS:
echo.
echo 1. VERIFICAR ORDEM DE LOAD NO LAUNCHER:
echo    - More Dragon Eggs deve vir ANTES do Dragon on Battle
echo    - Dragon on Battle deve ser o ULTIMO mod AGOT
echo.
echo 2. Se houver erros de UTF-8 BOM:
echo    - Execute: !FIX_ENCODING_UTF8_BOM.bat
echo    - Copie a pasta novamente
echo.
echo 3. Se o error.log mostrar erros do Dragon on Battle:
echo    - Copie a linha do erro e reporte
echo.
echo 4. Se o crash continuar:
echo    - Desative TEMPORARIAMENTE outros mods AGOT
echo    - Teste com APENAS: AGOT base + Dragon on Battle
echo    - Isso identifica se o conflito e com outro mod
echo.
echo 5. Para ver o error.log completo:
echo    - Abra: %LOGPATH%\logs\error.log
echo    - Procure por "dragon_battle" ou "dob_"
echo.
pause

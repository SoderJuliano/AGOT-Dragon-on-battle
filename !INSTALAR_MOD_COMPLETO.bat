@echo off
chcp 65001 >nul
echo ════════════════════════════════════════════════════════════
echo  INSTALADOR AUTOMÁTICO - DRAGON ON BATTLE
echo ════════════════════════════════════════════════════════════
echo.

set "ORIGEM=%~dp0"
set "DESTINO=%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\dragon_on_battle"

echo [1/4] Verificando diretório de destino...
if exist "%DESTINO%" (
    echo       └─ APAGANDO pasta antiga...
    rmdir /S /Q "%DESTINO%" 2>nul
)

echo.
echo [2/4] Criando estrutura de pastas...
mkdir "%DESTINO%" 2>nul
mkdir "%DESTINO%\common" 2>nul
mkdir "%DESTINO%\common\modifiers" 2>nul
mkdir "%DESTINO%\common\on_action" 2>nul
mkdir "%DESTINO%\common\scripted_effects" 2>nul
mkdir "%DESTINO%\common\scripted_triggers" 2>nul
mkdir "%DESTINO%\common\scripted_values" 2>nul
mkdir "%DESTINO%\events" 2>nul
mkdir "%DESTINO%\gui" 2>nul
mkdir "%DESTINO%\gui\custom_gui" 2>nul
mkdir "%DESTINO%\localization" 2>nul
mkdir "%DESTINO%\localization\english" 2>nul

echo.
echo [3/4] Copiando arquivos...
xcopy /Y /Q "%ORIGEM%common\*.*" "%DESTINO%\common\" >nul
xcopy /Y /Q "%ORIGEM%common\modifiers\*.*" "%DESTINO%\common\modifiers\" >nul
xcopy /Y /Q "%ORIGEM%common\on_action\*.*" "%DESTINO%\common\on_action\" >nul
xcopy /Y /Q "%ORIGEM%common\scripted_effects\*.*" "%DESTINO%\common\scripted_effects\" >nul
xcopy /Y /Q "%ORIGEM%common\scripted_triggers\*.*" "%DESTINO%\common\scripted_triggers\" >nul
xcopy /Y /Q "%ORIGEM%common\scripted_values\*.*" "%DESTINO%\common\scripted_values\" >nul
xcopy /Y /Q "%ORIGEM%events\*.*" "%DESTINO%\events\" >nul
xcopy /Y /Q "%ORIGEM%gui\custom_gui\*.*" "%DESTINO%\gui\custom_gui\" >nul
xcopy /Y /Q "%ORIGEM%localization\english\*.*" "%DESTINO%\localization\english\" >nul
copy /Y "%ORIGEM%descriptor.mod" "%DESTINO%\..\dragon_on_battle.mod" >nul

echo.
echo [4/4] Convertendo para UTF-8 BOM...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
"Get-ChildItem -Path '%DESTINO%' -Include *.txt,*.yml -Recurse | ForEach-Object { ^
    $content = Get-Content $_.FullName -Raw -Encoding UTF8; ^
    $utf8BOM = New-Object System.Text.UTF8Encoding $true; ^
    [System.IO.File]::WriteAllText($_.FullName, $content, $utf8BOM) ^
}"

echo.
echo ════════════════════════════════════════════════════════════
echo  ✓ MOD INSTALADO COM SUCESSO!
echo ════════════════════════════════════════════════════════════
echo.
echo  Localização: %DESTINO%
echo.
echo  AGORA:
echo  1. FECHE o CK3 completamente (launcher também)
echo  2. Abra o launcher
echo  3. Verifique se o mod está ativo
echo  4. Inicie o jogo
echo.
echo ════════════════════════════════════════════════════════════
pause

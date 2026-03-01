@echo off
:: ===================================================================
:: Converte todos os arquivos .txt e .yml do mod para UTF-8 BOM
:: Necessário para o CK3 aceitar os arquivos (requisito do engine)
:: ===================================================================

echo.
echo ====================================
echo  Dragon on Battle - UTF-8 BOM Fix
echo ====================================
echo.

:: Verificar se está na pasta correta
if not exist "descriptor.mod" (
    echo ERRO: Este .bat deve estar na pasta raiz do mod!
    echo Procure pela pasta que contem "descriptor.mod"
    pause
    exit /b 1
)

echo Convertendo arquivos para UTF-8 BOM...
echo.

:: Converter arquivos usando PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference = 'Stop'; try { $files = Get-ChildItem -Path '%~dp0' -Include *.txt,*.yml -Recurse -File; $converted = 0; foreach ($file in $files) { try { $content = Get-Content $file.FullName -Raw -Encoding UTF8; $utf8BOM = New-Object System.Text.UTF8Encoding $true; [System.IO.File]::WriteAllText($file.FullName, $content, $utf8BOM); $converted++; Write-Host \"[OK] $($file.Name)\" -ForegroundColor Green; } catch { Write-Host \"[ERRO] $($file.Name): $_\" -ForegroundColor Red; } } Write-Host \"`n$converted arquivos convertidos com sucesso!\" -ForegroundColor Cyan; } catch { Write-Host \"`nERRO FATAL: $_\" -ForegroundColor Red; exit 1; }"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ====================================
    echo ERRO na conversao!
    echo ====================================
    pause
    exit /b 1
)

echo.
echo ====================================
echo Conversao concluida com SUCESSO!
echo ====================================
echo.
echo IMPORTANTE: Agora copie manualmente esta pasta para:
echo %USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT - Dragon on battle\
echo.
echo ATENCAO:
echo - SUBSTITUA a pasta antiga se existir
echo - NAO copie ANTES de rodar este .bat
echo - Ative no Launcher DEPOIS do AGOT
echo.
pause


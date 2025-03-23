@echo off
chcp 65001 > nul
UTF-8
setlocal


if exist "install.bat" (
    call install.bat
) else (
    echo Файл install.bat не найден.
)

if exist "start.py" (
    echo Запуск парсера...
    python start.py
) else (
    echo Файл start.py не найден.
)

echo Готово!
endlocal
pause

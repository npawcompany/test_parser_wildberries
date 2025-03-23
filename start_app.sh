#!/bin/bash

# Установка кодовой страницы UTF-8
export LANG=en_US.UTF-8

# Проверяем наличие install.sh
if [ -f "install.sh" ]; then
    source install.sh
else
    echo "Файл install.sh не найден."
fi

# Проверяем наличие start.py
if [ -f "start.py" ]; then
    echo "Запуск парсера..."
    python3.10 start.py
else
    echo "Файл start.py не найден."
fi

echo "Готово!"
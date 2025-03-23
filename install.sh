#!/bin/bash

# Определяем текущую директорию
current_dir=$(pwd)

# Имя директории для виртуальной среды
venv_dir="$current_dir/.env"

# Проверяем, существует ли виртуальная среда
if [ ! -d "$venv_dir" ]; then
    echo "Виртуальная среда не найдена. Создаем новую..."
    python3.10 -m venv "$venv_dir"
else
    echo "Виртуальная среда уже существует."
fi

# Активируем виртуальную среду
source "$venv_dir/bin/activate"

# Устанавливаем необходимые библиотеки из requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Устанавливаем библиотеки из requirements.txt..."
    python -m pip install --upgrade pip
    pip install -U -r requirements.txt
    playwright install
else
    echo "Файл requirements.txt не найден."
fi

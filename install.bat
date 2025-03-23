
:: Определяем текущую директорию
set "current_dir=%cd%"

:: Имя директории для виртуальной среды
set "venv_dir=%current_dir%\.env"

:: Проверяем, существует ли виртуальная среда
if not exist "%venv_dir%" (
    echo Виртуальная среда не найдена. Создаем новую...
    python -m venv "%venv_dir%"
) else (
    echo Виртуальная среда уже существует.
)

:: Активируем виртуальную среду
call "%venv_dir%\Scripts\activate"

:: Устанавливаем необходимые библиотеки из requirements.txt
if exist "requirements.txt" (
    echo Устанавливаем библиотеки из requirements.txt...
    python -m pip install --upgrade pip
    pip install -U -r requirements.txt
    playwright install
) else (
    echo Файл requirements.txt не найден.
)
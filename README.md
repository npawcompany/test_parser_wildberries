# test_parser_wildberries
Тестовое задание, парсер для товаров wildberries


## Запуск парсера

### Запуск на Windows
Запускаете файл `start_app.bat`

### Запуск на Linux/MacOS
Запуск файла 
```bash
source start_app.sh
```

## Модули которые используются для парсера

- `playwright` - Нужен для того чтобы открыть каждую страницу на Wildberries, так чтобы страница не блокироваола бота
- `nltk` - Нужен для того чтобы получить ключевые слова из описание товара

Список модулей находится в файле `requirements.txt`

Исходный файл парсера находится в файле `start.py`
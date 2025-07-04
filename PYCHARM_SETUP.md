# Настройка проекта в PyCharm

## Шаг 1: Открытие проекта

1. Запустите PyCharm
2. Выберите "Open" или "Open Directory"
3. Выберите папку с проектом `PASHKADUROV-1-1`

## Шаг 2: Настройка интерпретатора Python

### Автоматическая настройка:
1. PyCharm предложит создать виртуальное окружение - нажмите "OK"
2. Выберите Python 3.8+ в качестве базового интерпретатора

### Ручная настройка:
1. Перейдите в `File` → `Settings` (или `Ctrl+Alt+S`)
2. Выберите `Project: PASHKADUROV-1-1` → `Python Interpreter`
3. Нажмите на шестеренку → `Add`
4. Выберите `Virtualenv Environment` → `New environment`
5. Выберите Python 3.8+ и нажмите `OK`

## Шаг 3: Установка зависимостей

### Способ 1: Через PyCharm
1. Откройте `requirements.txt`
2. PyCharm предложит установить зависимости - нажмите "Install requirements"

### Способ 2: Через терминал PyCharm
1. Откройте терминал в PyCharm (`View` → `Tool Windows` → `Terminal`)
2. Выполните:
```bash
pip install -r requirements.txt
```

### Способ 3: Автоматический скрипт
```bash
python setup.py
```

## Шаг 4: Создание папки instance

В терминале PyCharm выполните:
```bash
mkdir instance
```

## Шаг 5: Запуск бота

### Способ 1: Через PyCharm
1. Откройте файл `main.py`
2. Нажмите правой кнопкой мыши на файл
3. Выберите `Run 'main'`

### Способ 2: Через терминал
```bash
python main.py
```

## Проверка работы

После запуска в консоли PyCharm вы должны увидеть:
```
INFO:aiogram.dispatcher:Start polling
INFO:aiogram.dispatcher:Run polling for bot @PashadurovvBot id=7399928399 - 'Pashadurov'
```

## Остановка бота

- Нажмите красную кнопку "Stop" в PyCharm
- Или нажмите `Ctrl+C` в терминале

## Возможные проблемы

### Проблема: "No module named 'aiogram'"
**Решение:** Убедитесь, что интерпретатор настроен на виртуальное окружение и зависимости установлены

### Проблема: "Permission denied"
**Решение:** Запустите PyCharm от имени администратора

### Проблема: Неправильная рабочая директория
**Решение:** В настройках запуска (`Run/Debug Configurations`) установите правильную рабочую директорию

## Полезные советы

1. **Автодополнение:** PyCharm будет предлагать автодополнение для всех импортированных модулей
2. **Отладка:** Можете поставить точки останова в коде для отладки
3. **Git интеграция:** PyCharm автоматически покажет изменения в файлах
4. **Линтер:** PyCharm будет подчеркивать ошибки в коде

## Структура проекта в PyCharm

```
PASHKADUROV-1-1/
├── main.py              # Главный файл (запускайте его)
├── config.py            # Конфигурация
├── requirements.txt     # Зависимости
├── setup.py            # Автоматическая установка
├── INSTALL.md          # Подробная инструкция
├── PYCHARM_SETUP.md    # Эта инструкция
├── handlers/           # Обработчики команд
├── db/                 # База данных
├── utils/              # Утилиты
└── tests/              # Тесты
``` 
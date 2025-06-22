# Инструкция по установке и запуску Telegram бота

## Для преподавателей и студентов

### Предварительные требования:
- Python 3.8+ (рекомендуется Python 3.11+)
- Git
- PyCharm или любая другая IDE

### Шаг 1: Клонирование репозитория

```bash
git clone <URL_РЕПОЗИТОРИЯ>
cd PASHKADUROV-1-1
```

### Шаг 2: Проверка Python

Убедитесь, что Python установлен:

**Windows:**
```bash
py --version
# или
python --version
```

**Linux/Mac:**
```bash
python3 --version
```

### Шаг 3: Создание виртуального окружения

**Windows:**
```bash
py -m venv venv
```

**Linux/Mac:**
```bash
python3 -m venv venv
```

### Шаг 4: Активация виртуального окружения

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Шаг 5: Установка зависимостей

```bash
pip install -r requirements.txt
```

### Шаг 6: Создание папки для базы данных

```bash
mkdir instance
```

### Шаг 7: Запуск бота

```bash
py main.py
```

## Альтернативные способы запуска

### Способ 1: Через готовые скрипты

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh
```

### Способ 2: Через PyCharm

1. Откройте проект в PyCharm
2. Убедитесь, что интерпретатор Python настроен на виртуальное окружение
3. Откройте файл `main.py`
4. Нажмите правой кнопкой мыши на файл → "Run 'main'"

## Возможные проблемы и решения

### Проблема 1: "Python not found"
**Решение:** Установите Python с официального сайта python.org

### Проблема 2: "No such file or directory"
**Решение:** Убедитесь, что вы находитесь в правильной папке проекта

### Проблема 3: "Permission denied" (Linux/Mac)
**Решение:** 
```bash
chmod +x run.sh
```

### Проблема 4: Ошибки с зависимостями
**Решение:** Обновите pip и переустановите зависимости
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Проблема 5: Ошибки с SQLAlchemy
**Решение:** Убедитесь, что папка `instance` создана

## Проверка работы бота

После запуска вы должны увидеть:
```
INFO:aiogram.dispatcher:Start polling
INFO:aiogram.dispatcher:Run polling for bot @PashadurovvBot id=7399928399 - 'Pashadurov'
```

## Остановка бота

Нажмите **Ctrl+C** в терминале, где запущен бот.

## Структура проекта после установки

```
PASHKADUROV-1-1/
├── main.py
├── config.py
├── requirements.txt
├── venv/                 # Виртуальное окружение
├── instance/             # База данных
├── handlers/
├── db/
├── utils/
└── tests/
```

## Контакты для поддержки

Если возникли проблемы, обратитесь к разработчику проекта.

## Установка

### 1. Клонирование проекта
```bash
git clone <repository-url>
cd PASHKADUROV-1-1
```

### 2. Создание виртуального окружения (рекомендуется)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Создание папки для базы данных
```bash
mkdir instance
```

## Проверка установки

Запустите тестовый скрипт для проверки всех компонентов:

```bash
python test_bot.py
```

Если все тесты пройдены успешно, вы увидите:
```
🎉 Все тесты пройдены! Бот готов к запуску.
```

## Запуск бота

### Простой запуск
```bash
python main.py
```

### Запуск в фоновом режиме (Linux/Mac)
```bash
nohup python main.py > bot.log 2>&1 &
```

### Запуск через systemd (Linux)
Создайте файл `/etc/systemd/system/telegram-bot.service`:

```ini
[Unit]
Description=Telegram Bot for VM File Checking
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/PASHKADUROV-1-1
ExecStart=/path/to/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Затем:
```bash
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
sudo systemctl status telegram-bot
```

## Использование бота

### 1. Начальная настройка
Отправьте боту команду `/start` для регистрации.

### 2. Настройка подключения к ВМ
Отправьте данные в формате:
```
/vmpath 192.168.1.100:ubuntu:mypassword
```

### 3. Проверка подключения
```
/check
```

### 4. Работа с файлами
```
/ls - список файлов
/cat - содержимое текстовых файлов
```

## Устранение неполадок

### Проблема: "ModuleNotFoundError"
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Проблема: "Microsoft Visual C++ 14.0 or greater is required"
Установите Microsoft Visual C++ Build Tools:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

### Проблема: "Permission denied" при подключении к SSH
1. Проверьте правильность IP адреса, логина и пароля
2. Убедитесь, что SSH сервер запущен на ВМ
3. Проверьте настройки файрвола

### Проблема: "Database is locked"
Убедитесь, что только один экземпляр бота запущен одновременно.

## Логирование

Бот выводит логи в консоль. Для сохранения логов в файл:

```bash
python main.py > bot.log 2>&1
```

## Обновление

1. Остановите бота
2. Обновите код: `git pull`
3. Установите новые зависимости: `pip install -r requirements.txt`
4. Запустите бота заново

## Безопасность

⚠️ **Важно**: 
- Пароли хранятся в базе данных в открытом виде
- В продакшене рекомендуется шифровать пароли
- Используйте бота только в доверенной сети
- Регулярно обновляйте зависимости

## Поддержка

При возникновении проблем:
1. Проверьте логи бота
2. Убедитесь, что все зависимости установлены
3. Проверьте подключение к интернету
4. Убедитесь, что токен бота корректный 
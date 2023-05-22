# Куда пойти — Афиша Москвы
Сайт о самых интересных местах в Москве

[Демка сайта](http://aregadad.pythonanywhere.com/)

![main page screenshot](https://dvmn.org/media/screenshot-2020-06-04-204720.png)

[Скачать репозиторий](https://github.com/aregadad/afisha/archive/refs/heads/main.zip). Файлы должны быть разархивированы

## Зависимости
Python3.10+ должен быть установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

## Переменные окружения
- SECRET_KEY
- DEBUG=True
- ALLOWED_HOSTS=localhost,127.0.0.1
- DB_ENGINE
- DB_NAME
- STATIC_URL=static/
- STATIC_ROOT=static
- MEDIA_URL=media/
- MEDIA_ROOT=media

1. Поместите файл `.env` рядом с `manage.py`.
2. `.env` должен содержать текстовые данные без кавычек.

Например, если вы распечатаете содержимое `.env`, то увидите:

```bash
$ cat .env
SECRET_KEY=mykey123
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
STATIC_URL=static/
STATIC_ROOT=static
MEDIA_URL=media/
MEDIA_ROOT=media
```

## Как запустить
Сначала примените миграции:
```bash
$ python manage.py migrate
```

Запуск на Linux(Python 3) или Windows:
```bash
$ python manage.py runserver
```

Вы увидите:
```
Performing system checks...
System check identified no issues (0 silenced).
Django version 4.2.1, using settings 'where_to_go.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
...
```
Откройте сайт по [ссылке](http://127.0.0.1:8000/)
## Как загрузить место на сайт
### Используте админку
Создайте профиль администратора, введя команду
```bash
$ python manage.py createsuperuser
```
Перейдите в админку по [ссылке](http://127.0.0.1:8000/admin)

### Используте загрузку из .json
Введите в консоль
```bash
$ python manage.py load_place URL
```
где URL - это ссылка на файл в формате `.json` вида
```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий.",
    "description_long": "Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

## Режим отладки
Внизу слева на странице можно включить отладочный режим логгирования.
Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки, удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
# Проект парсинга pep

## Описание
Асинхронный парсер, который собирает информацию о пакетах PEP. 
Название, статус и его номер. 
Так же подбивает результаты о количестве пакетов в статусе.

### Функции парсера:

* Сбор статусов документов PEP и подсчёт статусов документов;


## Применяемые технологии

[![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Scrapy-2.5.1-blue?style=flat-square&labelColor=d0d0d0)](https://beautiful-soup-4.readthedocs.io)

### Порядок действия для запуска парсера

Клонировать репозиторий и перейти в папку в проектом:

```bash
git clone git@github.com:AlexandrVasilchuk/scrapy_parser_pep.git
```

```bash
cd scrapy_parser_pep
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

## Работа с парсером

### Режимы работы
Сбор статусов документов PEP и подсчёт статусов:
```bash
scrapy crawl pep
```

### Пример результатов работы:
Пример файла pep_

| Number | Name                               | Status     |
|--------|------------------------------------|------------|
| 1      | PEP 1 – PEP Purpose and Guidelines | Active     |
| 212    | PEP 212 – Loop Counter Iteration   | Rejected   |
| 215    | PEP 215 – String Interpolation     | Superseded |

Пример файла status_summary_

| Статус | Количество |
|--------|------------|
| Active | 31         |
| Final  | 276        |
| ...    | ...        |
| Итого: | 624        |
## Контакты
___
Автор:
[Васильчук Александр](https://github.com/AlexandrVasilchuk/)



#### Контакты:
![Gmail-badge](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)  
alexandrvsko@gmail.com  
![Telegram-badge](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)  
@vsko_ico
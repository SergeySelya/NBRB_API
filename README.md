# RBNR_API (Currency Rates)

*Author: Sergey Selivonchik


## Инструкция по настройке проекта:

1. Клонировать проект
```bash
git clone https://github.com/SergeySelya/RBNR_API.git
```
2. Открыть проект в PyCharm с наcтройками по умолчанию
3. Создать виртуальное окружение (через settings -> project "RBNR_API" -> project interpreter)
4. Открыть терминал в PyCharm, проверить, что виртуальное окружение активировано.
5. Обновить pip:
   ```bash
   pip install --upgrade pip
   ```
6. Установить в виртуальное окружение необходимые пакеты: 
   ```bash
   pip install --default-timeout=100 -r requirements.txt
   ```
7. Запускаем приложение в в PyCharm (файл `manage.py`, опция `runserver`)
python manage.py runserver

#EndPoints
* rateView/<str:date>/ ( возвращает OK ,  если ответ по курсам на указанную дату <str:date> - успешный)
  <img width="754" alt="image" src="https://github.com/SergeySelya/RBNR_API/assets/88445455/8dbf1982-42f2-44a4-8b19-549d9650d854">

* rateView/<str:date>/<str:curr_name>/ (Возвращает Курс по указанной дате и коду валюты + в поле "diff_rate" отображает курс в сравнении с предыдущим днем )
  <img width="692" alt="image" src="https://github.com/SergeySelya/RBNR_API/assets/88445455/01c443b1-c18a-43c4-9d9b-53b80bb1632d">

# Все запросы и ответы логируются в "logs/request.log"


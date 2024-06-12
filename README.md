# NBRB_API (Currency Rates)

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

# EndPoints
* rateView/<str:date>/ ( возвращает OK ,  если ответ по курсам на указанную дату <str:date> - успешный + добавил CRC32)
  
 <img width="398" alt="image" src="https://github.com/SergeySelya/RBNR_API/assets/88445455/ac46f922-5d87-4203-8a0e-6a30867d7666">


* rateView/<str:date>/<str:curr_name>/ (Возвращает Курс по указанной дате и коду валюты + в поле "diff_rate" отображает курс в сравнении с предыдущим днем + добавил CRC32 )
  
  <img width="581" alt="image" src="https://github.com/SergeySelya/RBNR_API/assets/88445455/71f6d32f-01eb-464d-952c-4cf51fcec244">

# Все запросы и ответы логируются в "logs/request.log"
<img width="1271" alt="image" src="https://github.com/SergeySelya/NBRB_API/assets/88445455/2483765b-d3db-439d-b8a4-f7bcdbbe3bc9">



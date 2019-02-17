# selection-modeling

https://habr.com/ru/post/181556/

Установил библиотеку для виртуального окружения: 
    pip install virtualenv

Создал виртуальное окружение:
    virtualenv env

Разрешил выполнение скриптов без подписи (запустить с правами админа):
(https://virtualenv.pypa.io/en/stable/userguide/)
    Set-ExecutionPolicy RemoteSigned

Активация виртуального окружения:
    env\Scripts\activate

Устанавливка фреймворка для веб-сервера:
    pip install django

Создание проекта с помощью django-admin:
    django-admin.py startproject selection_modeling
    cd selection_modeling

Устанавливаю адаптер базы данных:
    pip install psycopg2

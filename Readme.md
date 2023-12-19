# employee_hierarchy
Цей проект - це веб-сайт, який виводить ієрархію та список співробітників з бази даних. Він реалізований за допомогою Django, Twitter Bootstrap та jQuery.

## Функціональність

- Веб-сайт має дві сторінки: hierarchy та list.
- Сторінка hierarchy показує деревоподібну структуру співробітників, де кожен співробітник має одного начальника.
- Сторінка list показує таблицю з усією інформацією про співробітників, яка зберігається в базі даних, такою як ім'я, посада, дата прийому та email.
- Наявна можливість сгенерувати будь-яку кількість співробітників
- На сторінці list можна сортувати та шукати співробітників за будь-яким полем.
- Веб-сайт має автентифікацію користувача, яка дозволяє видаляти співробітників.
- Коли користувач авторизований:
- ![image](https://github.com/ArtemVasylchuck/employee_hierarchy/assets/93206845/d6ef8f47-6932-40ca-917a-d196e74ce911)
- ![image](https://github.com/ArtemVasylchuck/employee_hierarchy/assets/93206845/f8fa5e38-0ce3-472f-be68-3eab4e2069ad)
- Коли користувач неавторизований:
- ![image](https://github.com/ArtemVasylchuck/employee_hierarchy/assets/93206845/9096236c-bb16-4711-82fe-d4dd5cdd244a)
- ![image](https://github.com/ArtemVasylchuck/employee_hierarchy/assets/93206845/62cf2873-f44b-4f03-980d-b058879340b6)




## Встановлення та запуск

- Для запуску цього проекту вам потрібно мати Python 3.8 або вище та pip.
- Склонуйте цей репозиторій за допомогою команди `git clone https://github.com/ArtemVasylchuck/employee_hierarchy.git`.
- Перейдіть до папки проекту за допомогою команди `cd employeeHierarchy`.
- Створіть віртуальне середовище за допомогою команди `pip install -r requirements.txt`.
- Створіть базу даних за допомогою команд `python manage.py makemigrations` та `python manage.py migrate`.
- Заповніть базу даних випадковими даними про співробітників за допомогою команди `python manage.py seed_employees <кількість>`.
- Запустіть сервер за допомогою команди `python manage.py runserver`.
- Відкрийте браузер і перейдіть за адресою http://localhost:8000/.
- Для перевірки авторизації користувачів скористуйтеся командою `python manage.py createsuperuser` та виконайте авторизацію на сайті

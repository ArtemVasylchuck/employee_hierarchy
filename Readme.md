# employee_hierarchy
Цей проект - це веб-сайт, який виводить ієрархію та список співробітників з бази даних. Він реалізований за допомогою Django, Twitter Bootstrap та jQuery.

## Функціональність

- Веб-сайт має дві сторінки: hierarchy та list.
- Сторінка hierarchy показує деревоподібну структуру співробітників, де кожен співробітник має одного начальника.
- Сторінка list показує таблицю з усією інформацією про співробітників, яка зберігається в базі даних, такою як ім'я, посада, дата прийому та email.
- Реалізована пагінація для списку робітників
- Наявна можливість сгенерувати будь-яку кількість співробітників
- На сторінці list можна сортувати та шукати співробітників за будь-яким полем.
- Веб-сайт має автентифікацію користувача, яка дозволяє видаляти співробітників.
  
- Коли користувач авторизований:
- ![image](https://github.com/ArtemVasylchuck/employee_hierarchy/assets/93206845/7b0ea3d4-39be-4646-a0d4-b3d8b8a13a6f)
- ![image](https://github.com/ArtemVasylchuck/employee_hierarchy/assets/93206845/f00ac27e-d153-4f40-b1df-2b14f893216f)

- Коли користувач неавторизований:
- ![image](https://github.com/ArtemVasylchuck/employee_hierarchy/assets/93206845/c820a3ac-fef4-4ff9-ab46-cbe548791530)
- ![image](https://github.com/ArtemVasylchuck/employee_hierarchy/assets/93206845/c331e135-cf66-4f55-9f5f-c2df9a267fa0)






## Встановлення та запуск

- Для запуску цього проекту вам потрібно мати Python 3.8 або вище та pip.
- Склонуйте цей репозиторій за допомогою команди `git clone https://github.com/ArtemVasylchuck/employee_hierarchy.git`.
- Перейдіть до папки проекту за допомогою команди `cd employee_hierarchy`.
- Створіть віртуальне середовище за допомогою команди `pip install -r requirements.txt`.
- Створіть базу даних за допомогою команд `python manage.py makemigrations` та `python manage.py migrate`.
- Заповніть базу даних випадковими даними про співробітників за допомогою команди `python manage.py seed_employees <кількість>`.
- Запустіть сервер за допомогою команди `python manage.py runserver`.
- Відкрийте браузер і перейдіть за адресою http://localhost:8000/.
-  - /list - для списку робітників
   - /hierarchy - для їєрархії співробітників
   - /account/login - для авторизації
- Для перевірки авторизації користувачів скористуйтеся командою `python manage.py createsuperuser` та виконайте авторизацію на сайті

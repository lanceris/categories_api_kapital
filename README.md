CategoriesAPI application can be used by two endpoints:
* /categories/ puts JSON data to DB or renders all entries. Use "GET" method to get all entries or "POST" to put data.
* /categories/<int:pk>/ gets specific category data. Only "GET" method is allowed.

How to run:
1. `git clone https://github.com/lanceris/categories_api_kapital.git`
2. `virtualenv env`
3. `env\Scripts\activate` on Windows, `source env\bin\activate` on Linux
4. `pip install -r requirements.txt`
5. `cd api`
6. `.\manage.py migrate`
7. (Optional) `.\manage.py createsuperuser`
8. `.\manage.py runserver [ip:port]`

on steps 6-8 for Linux systems replace "\" with "/"
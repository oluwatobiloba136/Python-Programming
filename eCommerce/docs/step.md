
### Basic Set up
- cd eCommerce

- python -m venv env

- pip freeze

- .\env\Scripts\activate

- pip freeze

- pip install Django

- python.exe -m pip install --upgrade pip

- django-admin startproject wrightShop .
- python manage.py runserver

### Configure Template

- mkdir eCommerce\templates
- configure TEMPLATES in settings.py file : 
    - 'DIRS': ['templates'],

### Configure Static Folder
- mkdir eCommerce\wrightShop\static : create the static folder in project 
- configure STATIC in settings.py file : 
```
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR /'static'
STATICFILES_DIRS = [
        'eCommerce/static',
     ]
```

### Collect static files

```shell
    python manage.py collectstatic
```

### Set up the templates files
- base.html
- home.html
- footer.html
- navbar.html

- load static file , extend base files


### Create a Category App
- add the category app in the INSTALLED APP list in the setting files
- create your model
- register the model in the admin.py file
- pip install pillow to allow ImageField
- make migration
- apply migration

### Create SuperUser

```python
python manage.py createsuperuser
```

### create a customized Account app
- using AbstractBaseUser and BaseUserManager to customizing custom user creation model
 (https://docs.djangoproject.com/en/6.0/topics/auth/customizing/)

- AbstractBaseUser
This is an abstract base class containing only the core authentication infrastructure (password hashing, is_active, is_staff flags) without Django's default fields like username or email.
- Use when: You want to completely redefine user fields (e.g., login with email + phone, no username, or custom identifiers like customer_id).

- BaseUserManager
This provides create_user() and create_superuser() methods for safely creating users with hashed passwords.

- Use when: You need custom logic for user creation (validation, normalization, default values).


- register the account app in the admin.py file

- delete existing database to avoid conflict
- delete any migration files in an of the app 
- run make migrate
- run migrate
- run the server again

### Craete store app
- create the Product class  using models.Model approach and class Meta
- create the

### Associate the product to the home.html
- create the home views in the project level view  file that fetch the queryset of product



### URL paatern and views for Store and store_by_category
- create views for store and store_by_category

### context processor
# Django Setup and Development Steps

- Installing Python  
- Creating a Python virtual environment  
- Installing Django  
- Creating and configuring a Django project  
- Building a Django application  
- Designing data models  
- Creating and applying model migrations  
- Setting up an administration site for your models  
- Working with QuerySets and model manages  
- Building views, templates, and URLs
- Understanding the Django request/response cycle

## Requirements
- asgiref==3.11.0
- Django==6.0
- sqlparse==0.5.5
- tzdata==2025.3

### Highlights
- enum
- python shell
- sqlmigrate command: takes the migration names and returns their SQL without executing it


### change username or  password

- change username

```python
python manage.py shell

from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.get(username="admin")  # Replace 'admin' with current username
user.username = "new_username"              # Set new username
user.save()

```


- change password

```python

python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.get(username="admin")  # Replace 'admin' with your username
user.set_password("new_secure_password")   # Replace with your new password
user.save()

```

### Admin Model
- (admin.ModelAdmin) [https://docs.djangoproject.com/en/6.0/ref/contrib/admin/]

### Interfacing the database: QuerySet
- https://docs.djangoproject.com/en/5.0/ref/models/querysets/
- objects method
    - get() 
    - save()
    - create()
    - get_or_create()
    - all()
    - filter()
    - field__lookup e.g. 
        - filter(id__exact=1)
        - Post.objects.filter(title__iexact='who was django reinhardt?')
        - Post.objects.filter(title__contains='Django')
        - Post.objects.filter(title__icontains='django')
        - Post.objects.filter(id__in=[1, 3])
        - Post.objects.filter(id__gt=3)
        - Post.objects.filter(id__gte=3)
        - Post.objects.filter(id__lte=3)
        - Post.objects.filter(id__istartswith='who')
        - Post.objects.filter(id__iendswith='who')
        - Post.objects.filter(publish__date=date(2024,1,31))
        - Post.objects.filter(publish__year=2024)
        - Post.objects.filter(publish__month=1)
        - Post.objects.filter(publish__day=1)
        - Post.objects.filter(publish__date__gt=date(2024,1,1))
        - Post.objects.filter(author__username='admin')
        - Post.objects.filter(author__username__startswith='ad')
        - Post.objects.filter(publish__year=2024, author__username='admin')
        - Post.objects.filter(publish__year=2024) \
                      .filter(author__username='admin')
        - Post.objects.filter(publish__year=2024) \
                      .exclude(title__startswith='why')
        - Post.objects.order_by('title')
        - Post.objects.order_by('?')
        - Post.objects.all()[:5]
        - Post.objects.all()[3:6]
        - Post.objects.order_by('?')[0]
        - Post.objects.filter(id_lt=3).count()
        -  Post.objects.filter(title__startswith='Why').exists()
        - post = Post.objects.get(id=1)
          post =delete()

### Models.Manager
https://docs.djangoproject.com/en/6.0/topics/db/managers/

### Django shortcuts functions
https://docs.djangoproject.com/en/5.2/topics/http/shortcuts/

### Path Converters
https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters

### re_path()
https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.re_path

### URL namespaces
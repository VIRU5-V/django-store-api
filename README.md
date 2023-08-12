# django-shop-restapi
Django based CRM e-commerce RESTAPI. 


# Tasks
- Admin should be able to upload a product to sell ✅
- Admin should be notified when a new user registers ✅
- Admin should be notified when an order is placed ✅

access api from here [api_demo](https://django-store-api-production.up.railway.app/api/)

# To run this project open your terminal and write these commands

clone repo
```
git clone -b submission https://github.com/webcoupersorg/django-shop-restapi.git
cd <project_directory>

```
Install Dependencies
```
pip install -r requirements.txt

```
Database Setup
```
python manage.py migrate

```
run server

```
python manage.py runserver

```

to add product create superuser
```
python manage.py createsuperuser

```
add countries for shipping
```
python manage.py oscar_populate_countries

```


# Available apis
```
    
    "register": "/api/register/",
    "login": "/api/login/",
    "basket": "/api/basket/",
    "basket-add-product": "/api/basket/add-product/",
    "basket-add-voucher": "/api/basket/add-voucher/",
    "basket-shipping-methods": "/api/basket/shipping-methods/",
    "baskets": "/api/baskets/",
    "categories": "/api/categories/",
    "checkout": "/api/checkout/",
    "orders": "/api/orders/",
    "options": "/api/options/",
    "products": "/api/products/",
    "countries": "/api/countries/",
    "useraddresses": "/api/useraddresses/",
    
    "admin": {
        "productclasses": "/api/admin/productclasses/",
        "products": "/api/admin/products/",
        "categories": "/api/admin/categories/",
        "orders": "/api/admin/orders/",
        "partners": "/api/admin/partners/",
        "users": "/api/admin/users/"
    }
```

## Required environments variables

```
# base url
BASE_URL = BASE_URL # example 'http://localhost:8000'

# email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'    # Your SMTP server
EMAIL_PORT = 587  # SMTP port (usually 587 for TLS)
EMAIL_USE_TLS = True  # Use TLS (True/False)
EMAIL_USE_SSL = False  # Use SSL (True/False)
EMAIL_HOST_USER = EMAIL_HOST_USER  # Your SMTP username
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD  # Your SMTP password
DEFAULT_FROM_EMAIL = DEFAULT_FROM_EMAIL  # Default sender email address


# paypal settings
PAYPAL_CLIENT_ID = PAYPAL_CLIENT_ID
PAYPAL_SECRET = PAYPAL_SECRET

# optional DB settings
DB_ENGINE = DB_ENGINE
DB_NAME = DB_NAME
DB_USER = DB_USER
DB_PASSWORD = DB_PASSWORD
DB_HOST = DB_HOST
DB_PORT = DB_PORT

ALLOWED_HOSTS =  '["domain name"]'
```
# django-shop-restapi
Django based CRM e-commerce RESTAPI. 


# Tasks
- Admin should be able to upload a product to sell ✅
- Admin should be notified when a new user registers ✅
- Admin should be notified when an order is placed ✅

# To run this project open your terminal and write these commands

clone repo
```
git clone https://github.com/VIRU5-V/django-store-api.git
cd django-store-api

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
```
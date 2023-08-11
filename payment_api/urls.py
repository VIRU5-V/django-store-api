from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r"^paypal/(?P<pk>[0-9]+)/$", views.PaymentView.as_view(), name='api-payment'),
    path('verify_payment/', view=views.PaymentVerfification.as_view(), name='verifpy-payment')
]
# enquiry/urls.py
from django.urls import path
from .views import inquiry, inquiry_success

urlpatterns = [
    path('inquiry/', inquiry, name='inquiry'),
    path('inquiry/success/', inquiry_success, name='inquiry_success'),
]

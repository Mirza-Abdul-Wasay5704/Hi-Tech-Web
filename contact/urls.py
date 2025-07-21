from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('quote/', views.request_quote, name='quote'),
    path('success/', views.success, name='success'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gnillib-home'),
    path('contact/', views.contact, name='gnillib-contact'),
]
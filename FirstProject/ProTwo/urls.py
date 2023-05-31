from django.urls import path, include
from ProTwo import views

urlpatterns = [
    path('', views.help, name='help'),
]

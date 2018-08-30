from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewForm, name = 'viewForm'),
]

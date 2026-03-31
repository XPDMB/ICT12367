from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('delete/<int:id>/', views.delete, name='delete'),
]

from .views import *
from django.urls import path

urlpatterns = [
    path('', Index, name="index"),
    path("forms", My_Forms, name="forms"),
    path("update/<str:pk>", Update, name="update"),
    path("delete/<str:pk>", Delete, name="delete")
]

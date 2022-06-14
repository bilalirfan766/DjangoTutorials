from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('link',views.StudentAPI.as_view(),name="studentapi"),
]

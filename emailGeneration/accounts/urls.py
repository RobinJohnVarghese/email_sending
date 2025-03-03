from django.contrib import admin
from django.urls import path
from .import views
from .views import *



urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_email, name='submit_email'),
    path('trigger-email-task/', views.tigger_email_task, name='trigger-email-task'),

]
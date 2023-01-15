from django.urls import path
from grovers import views

urlpatterns = [
    path('',  views.home, name='home'),
    path('grovers/', views.grovers)]
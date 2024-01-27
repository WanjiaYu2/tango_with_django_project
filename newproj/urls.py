from django.urls import path
from rango import views
app_name = 'newproj'
urlpatterns = [
    path('', views.index, name='index'),
]
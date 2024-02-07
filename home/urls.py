from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.GoHome.as_view(), name='go_home'),
]

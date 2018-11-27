from django.urls import include, path
from . import views


urlpatterns = [
 # post views
 path('', views.user_login, name='login'),
]
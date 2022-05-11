from django.test import tag
from django.urls import path
from basic_app import views

#TEMPLATE URLS used in href of <a> tag
app_name='basic_app'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
from django.urls import path
from schoolapp import views

app_name = 'schoolapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('form', views.formpage, name='formpage'),
    path('newpage', views.newpage, name='newpage'),
    path('profile', views.profile, name='profile'),
    path('add', views.add, name='add'),
    path('submit', views.submit, name='submit'),
    ]

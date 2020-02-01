from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    path('newsdate/<int:year>', views.newsdate, name='newsdate'),
    path('register/', views.register, name='register'),
    path('adduser/', views.adduser, name='adduser'),
    path('addnews', views.addnews, name='addnews'),
    path('addnewnews', views.addnewnews, name='addnewnews')
]
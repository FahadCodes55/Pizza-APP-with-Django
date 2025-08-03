from django.urls import path
from .import views


# write urls below

urlpatterns = [
    path('index/', views.index, name='Index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('menu/', views.pizza_menu, name='menu'),
    path('order/<int:pk>/', views.order_pizza, name='order'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # For the homepage
    path('home/', views.home, name='home'),  # For the home page
    path('shop/', views.shop, name='shop'),  # For the shop page
    path('official/', views.official, name='official'),
    path('sports/', views.sports, name='sports'),
    path('login/', views.login_user, name='login'),  # For the login page
    path('logout/', views.logout_user, name='logout'),  # For the login page
    path('register/', views.register, name='register'),  # For the register page
    path('product/<int:pk>', views.product, name='product'),  # For the product (detail) page


]
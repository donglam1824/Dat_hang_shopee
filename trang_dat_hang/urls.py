from django.contrib import admin
from django.urls import path, include
from trang_dat_hang import views

urlpatterns = [
    path('', views.home, name='home'),
    path('themsanpham', views.them_san_pham, name='them_san_pham'),
]

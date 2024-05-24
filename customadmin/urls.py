from django.urls import path
from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('danhsachsanpham', views.product_list, name='product_list'),
    path('danhsachdongy', views.approved_list, name='approved_list'),
    path('', views.product_list, name='app_list'),
]

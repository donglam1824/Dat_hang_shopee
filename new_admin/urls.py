from django.urls import path, include
from new_admin import views

urlpatterns = [
    path('admin', views.admin, name="admin"),   
]

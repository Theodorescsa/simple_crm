# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list_create, name='customer-list-create'),
    path('customers/<int:pk>/', views.customer_detail, name='customer-detail'),
    path('products/', views.product_list_create, name='product-list-create'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('employees/', views.employee_list_create, name='employee-list-create'),
    path('employees/<int:pk>/', views.employee_detail, name='employee-detail'),
    path('task-board/', views.task_list_create, name='task-list-create'),
    path('task-board/<int:pk>/', views.task_detail, name='task-detail'),
]

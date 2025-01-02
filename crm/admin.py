from django.contrib import admin
from .models import Customer, Product, Employee, Board, Column, Task

# Quản lý Khách hàng
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')  
    search_fields = ('name', 'email', 'phone') 
    list_filter = ('address',) 

# Quản lý Sản phẩm
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock') 
    search_fields = ('name',)  
    list_filter = ('price',)  

# Quản lý Nhân sự
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'phone')
    search_fields = ('name', 'email')
    list_filter = ('position',)

# Quản lý Bảng
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')  
    search_fields = ('name', 'created_by__username')
    list_filter = ('created_by',)

# Quản lý Cột
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'board')
    search_fields = ('name', 'board__name')  
    list_filter = ('board',)

# Quản lý Công việc
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'column', 'assigned_to', 'due_date')
    search_fields = ('name', 'description')  
    list_filter = ('status', 'assigned_to', 'due_date')  

# Đăng ký các model vào admin site
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Task, TaskAdmin)

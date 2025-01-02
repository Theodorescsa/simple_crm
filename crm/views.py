# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Customer, Product, Employee, Board, Task
from .serializers import (
    CustomerSerializer, ProductSerializer, EmployeeSerializer,
    BoardSerializer, TaskSerializer
)
from drf_spectacular.utils import extend_schema, OpenApiParameter

# Khách hàng (Customer) - CRUD
@extend_schema(
    request=CustomerSerializer,  
    responses=CustomerSerializer, 
    description="Retrieve and create customers",
    tags=["Customer Management"],  

)
@api_view(['GET', 'POST'])
def customer_list_create(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@extend_schema(
    request=CustomerSerializer, 
    responses=CustomerSerializer,  
    description="Retrieve and create customers",
    tags=["Customer Management"],  
    
)
@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Sản phẩm (Product) - CRUD
@extend_schema(
    request=ProductSerializer,  
    responses=ProductSerializer, 
    description="Retrieve and create products",
    tags=["Product Management"],  
    
)
@api_view(['GET', 'POST'])
def product_list_create(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@extend_schema(
    request=ProductSerializer,  
    responses=ProductSerializer, 
    description="Retrieve and create products",
    tags=["Product Management"],  
    
)
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Nhân sự (Employee) - CRUD
@extend_schema(
    request=EmployeeSerializer,  
    responses=EmployeeSerializer, 
    description="Retrieve and create employees",
    tags=["Employees Management"],  
)
@api_view(['GET', 'POST'])
def employee_list_create(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=EmployeeSerializer,  
    responses=EmployeeSerializer, 
    description="Retrieve and create employees",
    tags=["Employees Management"],
)
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Bảng công việc (Task Board) - CRUD và Lọc
@extend_schema(
    request=TaskSerializer,
    responses={200: TaskSerializer, 201: TaskSerializer},  
    description="Retrieve a list of tasks with optional filtering by status and assigned user. "
                "Also allows creating a new task by providing task details in the request body.",
    tags=["Task Management"],  
    )
@api_view(['GET', 'POST'])
def task_list_create(request):
    if request.method == 'GET':
        status_filter = request.query_params.get('status', None)
        assigned_to_filter = request.query_params.get('assigned_to', None)

        tasks = Task.objects.all()
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        if assigned_to_filter:
            tasks = tasks.filter(assigned_to=assigned_to_filter)
        
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=TaskSerializer,  
    responses=TaskSerializer, 
    description="Retrieve and create tasks",
    tags=["Task Management"],  

)
@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

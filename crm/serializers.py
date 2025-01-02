# serializers.py
from rest_framework import serializers
from .models import Customer, Product, Employee, Board, Column, Task

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Column
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = '__all__'

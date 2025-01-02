from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Customer(Person):
    address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Customer: {self.name}"

class Employee(Person):
    position = models.CharField(max_length=255)

    def __str__(self):
        return f"Employee: {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Board(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Column(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, related_name='columns', on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    column = models.ForeignKey('Column', related_name='tasks', on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Open')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name
from rest_framework import serializers
from .models import Employee


class EmployeesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'role', 'customer', 'user')


class EmployeesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'customer')

from django.contrib import admin
from .models import Employee, Customer


admin.site.register(Customer)
admin.site.register(Employee)
# Register your models here.

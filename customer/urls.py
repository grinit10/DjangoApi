from django.urls import path
from .views import (
    CustomerCreateView,
    CustomerListView,
    CustomerDetailView,
    CustomerUpdateView,
    CustomerDeleteView)


urlpatterns = [
    path('customers/employees/', CustomerListView.as_view(), name="employees-create"),
    path('customers/employees/create/', CustomerCreateView.as_view(), name="employees-all"),
    path('customers/employees/<int:pk>/', CustomerDetailView.as_view(), name="employees-Detail"),
    path('customers/employees/<int:pk>/edit', CustomerUpdateView.as_view(), name="employees-Update"),
    path('customers/employees/<int:pk>/delete', CustomerDeleteView.as_view(), name="employees-Delete")
]

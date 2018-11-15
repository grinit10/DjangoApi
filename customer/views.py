from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView)
from .models import Employee
from .serializers import (
    EmployeesListSerializer,
    EmployeesDetailSerializer
)


class CustomerCreateView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CustomerListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesListSerializer


class CustomerDetailView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesDetailSerializer


class CustomerUpdateView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesDetailSerializer


class CustomerDeleteView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesDetailSerializer


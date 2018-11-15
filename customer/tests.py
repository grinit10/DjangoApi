from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Employee
from .serializers import EmployeesSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_Employee(firstname="", lastname=""):
        if firstname != "" and lastname != "":
            Employee.objects.create(First_Name=firstname, Last_Name=lastname, Role='')

    def setUp(self):
        # add test data
        self.create_Employee("Arnab", "Chakraborty")
        self.create_Employee("Arpita", "Sen")


class GetAllEmployeesTest(BaseViewTest):

    def test_get_all_employees(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("customers-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Employee.objects.all()
        serialized = EmployeesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

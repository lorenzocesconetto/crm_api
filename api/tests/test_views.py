from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from api.models import Customer
from api.serializers import CustomerSerializer
from rest_framework.test import APIRequestFactory


# initialize the APIClient app
client = Client()


class GetAllCustomersTest(TestCase):
    """ Test module for GET all customers API """

    def setUp(self):
        Customer.objects.create(first_name='A', last_name='B',
                                title='C', company='D', city='E', email='F', gender='G')
        Customer.objects.create(first_name='B', last_name='C',
                                title='D', company='E', city='F', email='G', gender='H')
        Customer.objects.create(first_name='C', last_name='D',
                                title='E', company='F', city='G', email='H', gender='I')
        Customer.objects.create(first_name='D', last_name='E',
                                title='F', company='G', city='H', email='I', gender='J')

    def test_get_all_customers(self):
        # get API response
        response = client.get(reverse('api:customer-list'), format='json')
        response_data = [dict(x) for x in response.data['results']]
        # get data straight from db
        customers = [x for x in Customer.objects.all().values()]
        self.assertEqual(response_data, customers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleCustomerTest(TestCase):
    """ Test module for GET single customer API """

    def setUp(self):
        self.customer_1 = Customer.objects.create(first_name='A', last_name='B',
                                                  title='C', company='D', city='E', email='F', gender='G')
        self.customer_2 = Customer.objects.create(first_name='B', last_name='C',
                                                  title='D', company='E', city='F', email='G', gender='H')

    def test_get_valid_single_puppy(self):
        response = client.get(
            reverse('api:customer-detail', kwargs={'pk': self.customer_1.pk}))
        customer_1 = Customer.objects.get(pk=self.customer_1.pk)
        serializer = CustomerSerializer(customer_1)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_puppy(self):
        response = client.get(
            reverse('api:customer-detail', kwargs={'pk': 1200}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

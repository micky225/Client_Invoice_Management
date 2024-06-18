from django.test import TestCase, Client
from django.urls import reverse
from app.models import Invoice
from app.tasks import process_csv_file
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase
import tempfile
import csv
import time


#API List and CSV Upload Test
class InvoiceTests(APITestCase):
    def test_upload_csv(self):
        url = reverse('api:api_invoice_upload_csv')
        with open('/home/michael/Documents/invoice2.csv', 'rb') as csv_file:
            response = self.client.post(url, {'file': csv_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_list_invoices(self):
        url = reverse('api:api_invoice_list_create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


#Test to ensure all Rest endpoints respond within 100 milliseconds (ms)
class ApiResponseTimeTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.api_invoice_list_create_url = reverse('api:api_invoice_list_create')
        self.api_invoice_upload_csv_url = reverse('api:api_invoice_upload_csv')

    def test_api_response_times(self):
        urls = [
            self.api_invoice_list_create_url,
            self.api_invoice_upload_csv_url,
        ]

        for url in urls:
            with self.subTest(url=url):
                start_time = time.time()
                response = self.client.get(url)
                end_time = time.time()

                response_time = (end_time - start_time) * 1000
                self.assertLess(response_time, 100, f"{url} response time is {response_time}ms, which exceeds 100ms")        
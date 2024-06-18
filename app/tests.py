from django.test import TestCase, Client
from django.urls import reverse
from .models import Invoice
from .tasks import process_csv_file
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile
import csv


class InvoiceViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('app:list_invoices')
        self.create_url = reverse('app:create')
        self.update_url = lambda pk: reverse('app:update_invoice', args=[pk])
        self.upload_csv_url = reverse('app:upload_csv')
        self.invoice = Invoice.objects.create(
            recipient="MPedigree",
            description="Test Description",
            num_items=5,
            expiration_date="2024-06-11"
        )

    def test_list_invoices(self):
        response = self.client.get(self.list_url)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.invoice.recipient)

    def test_create_invoices(self):
        data = {
            "recipient": "MPedigree",
            "description": "New Description",
            "num_items": 10,
            "expiration_date": "2024-06-11" 
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Invoice.objects.filter(recipient="MPedigree").exists())
        
        response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_update_invoice(self):
        data = {
            "recipient": "Updated Company",
            "description": "Updated Description",
            "num_items": 15,
            "expiration_date": "2023-12-31"
        }
        response = self.client.post(self.update_url(self.invoice.pk), data)
        self.assertEqual(response.status_code, 302)
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.recipient, "Updated Company")

    def test_upload_csv_post(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp_file:
            writer = csv.writer(tmp_file)
            writer.writerow(['recipient', 'description', 'num_items', 'expiration_date'])
            writer.writerow(['Company1', 'Description1', 10, '2023-12-31'])
            writer.writerow(['Company2', 'Description2', 20, '2023-12-31'])
            tmp_file.seek(0)
            tmp_file.close()

            with open(tmp_file.name, 'rb') as csv_file:
                response = self.client.post(self.upload_csv_url, {'file': csv_file})
                self.assertEqual(response.status_code, 302)
        
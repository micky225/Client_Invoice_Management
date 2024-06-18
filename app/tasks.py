from celery import shared_task
import csv
from io import StringIO
from .models import Invoice
import random
import string

def generate_random_code(length=10):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@shared_task
def process_csv_file(csv_data):
    csv_file = StringIO(csv_data)
    reader = csv.DictReader(csv_file)
    invoice_objects = []
    
    for row in reader:
        invoice_code = generate_random_code()
        while Invoice.objects.filter(invoice_code=invoice_code).exists():
            invoice_code = generate_random_code()

        invoice_objects.append(
            Invoice(
                invoice_code=invoice_code,
                recipient=row['recipient'],
                description=row['description'],
                num_items=int(row['num_items']),
                expiration_date=row['expiration_date']
            )
        )
    
    Invoice.objects.bulk_create(invoice_objects)

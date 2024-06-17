from celery import shared_task
import csv
from io import StringIO
from .models import Invoice


@shared_task
def process_csv_file(csv_data):
    csv_file = StringIO(csv_data)
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        Invoice.objects.create(
            recipient=row['recipient'],
            description=row['description'],
            num_items= int(row['num_items']),
            expiration_date=row['expiration_date']
        )

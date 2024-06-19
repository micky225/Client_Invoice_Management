import csv
import random
from datetime import datetime, timedelta
import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Generate a CSV file with 10,000 rows of randomized invoice data'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The file path where the CSV file will be saved')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        self.generate_csv(file_path, 10000)
        self.stdout.write(self.style.SUCCESS(f'CSV file generated successfully at {file_path}'))

    def random_date(self, start, end):
        return start + timedelta(days=random.randint(0, (end - start).days))

    def generate_csv(self, file_path, num_rows):
        fieldnames = ['recipient', 'description', 'num_items', 'expiration_date']
        recipients = ['Amali Tech', 'Tech Corp', 'Innovate LLC', 'Future Solutions', 'Global Services']
        descriptions = ['Item in process', 'Item delivered', 'Pending approval', 'Awaiting shipment', 'Completed order']
        num_items = range(1, 100)
        start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
        end_date = datetime.strptime('2024-12-31', '%Y-%m-%d')

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for _ in range(num_rows):
                row = {
                    'recipient': random.choice(recipients),
                    'description': random.choice(descriptions),
                    'num_items': random.choice(num_items),
                    'expiration_date': self.random_date(start_date, end_date).strftime('%Y-%m-%d')
                }
                writer.writerow(row)

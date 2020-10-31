from django.core.management.base import BaseCommand, CommandError
from django.db import connection
import os

class Command(BaseCommand):
    help = 'Imports customer data from csv into the database'

    def handle(self, *args, **options):
        file_path = os.path.join(os.getcwd(), 'customers.csv')
        command = "COPY public.api_customer (id, first_name, last_name, email, gender, company, city, title) " + \
            f"FROM '{file_path}' " + \
            "DELIMITER ',' CSV HEADER ENCODING 'UTF8';"
        with connection.cursor() as cursor:
            cursor.execute(command)
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

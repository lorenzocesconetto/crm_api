import requests
from api.models import Customer
from django.core.management.base import BaseCommand

key = ''

class Command(BaseCommand):
    help = 'Fill database columns latitude and longitude information from customer city using Google Maps Geocoding API'

    def handle(self, *args, **options):
        for customer in Customer.objects.all():
            if customer.latitude is not None and customer.longitude is not None:
                continue
            url = f"https://maps.googleapis.com/maps/api/geocode/json?address={customer.city}&key={key}"
            response = requests.get(url)
            try:
                location = response.json()['results'][0]['geometry']['location']
                customer.latitude = location['lat']
                customer.longitude = location['lng']
                customer.save()
                
            except (IndexError, requests.exceptions.ConnectionError) as e:
                self.stdout.write(self.style.ERROR(e))
                self.stdout.write(self.style.WARNING('Could not locate: ' + customer.city + ' from customer: ' + str(customer)))

        self.stdout.write(self.style.SUCCESS('Latitude and Longitude filled successfully!'))

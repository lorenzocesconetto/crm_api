from django.db import models


class Customer(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50, null=True)
    email = models.EmailField('Email')
    gender = models.CharField('Gender', max_length=50, choices=Gender.choices)
    company = models.CharField('Company', max_length=50)
    city = models.CharField('City', max_length=50)
    title = models.CharField('Title', max_length=50, null=True)
    latitude = models.FloatField('Latitude', null=True)
    longitude = models.FloatField('Longitude', null=True)

    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.first_name
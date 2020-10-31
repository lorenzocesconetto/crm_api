from rest_framework import serializers
from api.models import Customer
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name',
                  'email', 'gender', 'company', 'city', 'title', 'latitude', 'longitude']

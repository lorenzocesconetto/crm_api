from django.contrib import admin
from api.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'company', 'title', 'city')


admin.site.register(Customer, CustomerAdmin)

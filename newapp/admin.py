from django.contrib import admin
from newapp.models import Customer
# Register your models here.

# admin.site.register(Customer)   # This is the shortest way to register a model

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'mobile']
    class Meta:
        model = Customer


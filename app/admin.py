from django.contrib import admin

from app.models import Order, Ticket

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Order)

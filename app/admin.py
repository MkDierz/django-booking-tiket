from django.contrib import admin

from app.models import Order, Ticket

# Register your models here.

admin.site.register(Ticket)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "uuid",
        "user",
        "ticket",
        "total",
        "payment_ref",
        "payment_status",
    ]
    list_editable = ["payment_status"]
    pass

import random
from uuid import uuid5
import uuid
from django.db import models

from django.contrib.auth.models import User


def random_string():
    return str(random.randint(10000, 99999))


class Ticket(models.Model):
    """Model definition for Ticket."""

    name = models.CharField(null=False, max_length=50)
    price = models.IntegerField(null=False)

    class Meta:
        """Meta definition for Ticket."""

        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return f"{self.name} - {self.price}"


class Order(models.Model):
    """Model definition for Order."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date = models.DateField(null=False, auto_now=False, auto_now_add=False)
    uuid = models.UUIDField(default=uuid5(uuid.NAMESPACE_DNS, "aaa"), editable=False)
    qty = models.PositiveIntegerField(null=False, default=1)
    payment_status = models.BooleanField(null=False, default=False)
    payment_ref = models.CharField(default=random_string, max_length=50, editable=False)

    class Meta:
        """Meta definition for Order."""

        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.user.username} - {self.qty} - {self.ticket.name}"

    def total(self):
        return self.ticket.price * self.qty

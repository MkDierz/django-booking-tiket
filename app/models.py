from django.db import models

from django.contrib.auth.models import User


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
    qty = models.IntegerField(null=False)

    class Meta:
        """Meta definition for Order."""

        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.user.username} - {self.qty} - {self.ticket.name}"

    def total(self):
        return self.ticket.price * self.qty

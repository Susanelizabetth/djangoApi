from django.db import models
from orders.models import Order
from uuid import uuid4
# Create your models here.

# crear modelo de paquete


class Package(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False)
    order = models.ForeignKey(
        Order, related_name='packages', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return f"{self.id}: {self.description}"

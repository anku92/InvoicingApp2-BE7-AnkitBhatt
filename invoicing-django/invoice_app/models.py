from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class UserModel(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=12, validators=[MinLengthValidator(3)])
    username = models.CharField(max_length=12, validators=[MinLengthValidator(3)])


class InvoiceModel(models.Model):
    invoice_id = models.IntegerField()
    date = models.DateField()
    client_name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])


class ItemModel(models.Model):
    invoice = models.ForeignKey(InvoiceModel, on_delete=models.CASCADE, related_name="items")
    desc = models.CharField(max_length=50)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)

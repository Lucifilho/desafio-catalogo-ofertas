from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    installment = models.CharField(max_length=255, null=True, blank=True)
    entire_price = models.CharField(max_length=255, null=True, blank=True)
    shipping_type = models.CharField(max_length=255, null=True, blank=True)
    free_shipping = models.CharField(max_length=255, null=True, blank=True)
    percentual_discount = models.CharField(max_length=255, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    shipping_info = models.CharField(max_length=255, null=True, blank=True)  # Adicionar este campo


    def __str__(self):
        return self.name
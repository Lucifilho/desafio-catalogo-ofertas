from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome do Produto")
    link = models.URLField(null=True, blank=True, verbose_name="Link")
    pricePrevious = models.CharField(max_length=255, null=True, blank=True, verbose_name="Preço Anterior")
    installment = models.CharField(max_length=255, null=True, blank=True, verbose_name="Parcelamento")
    entire_price = models.CharField(max_length=255, null=True, blank=True, verbose_name="Preço Total")
    shipping_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="Tipo de Entrega")
    free_shipping = models.CharField(max_length=255, null=True, blank=True, verbose_name="Frete Grátis")
    percentual_discount = models.IntegerField(null=True, blank=True, verbose_name="Percentual de Desconto")
    image = models.URLField(null=True, blank=True, verbose_name="Imagem")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name
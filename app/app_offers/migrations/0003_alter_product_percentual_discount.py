# Generated by Django 4.2.5 on 2025-02-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_offers', '0002_alter_product_entire_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='percentual_discount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Percentual de Desconto'),
        ),
    ]

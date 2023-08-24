# Generated by Django 4.2.4 on 2023-08-23 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ACosmeticos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="compra",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="compras",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="carrinho",
            name="cliente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ACosmeticos.cliente"
            ),
        ),
    ]
# Generated by Django 4.2.4 on 2023-10-11 16:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ACosmeticos", "0010_itemcarrinho_carrinho"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="marca",
            name="sub_produto",
        ),
    ]
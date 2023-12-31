# Generated by Django 4.2.4 on 2023-10-06 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ACosmeticos", "0007_alter_itemcarrinho_produto"),
    ]

    operations = [
        migrations.RenameField(
            model_name="carrinho",
            old_name="total_da_compra",
            new_name="total",
        ),
        migrations.RemoveField(
            model_name="itemcarrinho",
            name="carrinho",
        ),
        migrations.AlterField(
            model_name="itemcarrinho",
            name="produto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="ACosmeticos.produto",
            ),
        ),
    ]

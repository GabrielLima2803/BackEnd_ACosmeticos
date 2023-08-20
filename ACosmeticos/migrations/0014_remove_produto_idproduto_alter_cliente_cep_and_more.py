# Generated by Django 4.2.4 on 2023-08-20 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ACosmeticos", "0013_alter_itemcarrinho_compra"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produto",
            name="idProduto",
        ),
        migrations.AlterField(
            model_name="cliente",
            name="cep",
            field=models.CharField(default="bla", max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="cpf",
            field=models.CharField(default="bla", max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name="itemcarrinho",
            name="compra",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="itens",
                to="ACosmeticos.compra",
            ),
        ),
    ]

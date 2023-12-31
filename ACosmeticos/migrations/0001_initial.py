# Generated by Django 4.2.4 on 2023-08-23 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carrinho",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "total_da_compra",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("numero_telefone", models.CharField(max_length=20)),
                ("endereco", models.TextField()),
                ("numero_casa", models.CharField(max_length=10)),
                ("bairro", models.CharField(max_length=50)),
                ("cidade", models.CharField(max_length=50)),
                ("estado", models.CharField(max_length=2)),
                ("cep", models.CharField(default="bla", max_length=9, null=True)),
                ("cpf", models.CharField(default="bla", max_length=11, null=True)),
            ],
            options={
                "verbose_name_plural": "Clientes",
            },
        ),
        migrations.CreateModel(
            name="Compra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "Carrinho"),
                            (2, "Realizado"),
                            (3, "Pago"),
                            (4, "Entregue"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ACosmeticos.cliente",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FormaPagamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo_de_pagamento", models.CharField(max_length=100)),
                (
                    "quantidade_de_parcelas",
                    models.PositiveIntegerField(blank=True, default=1),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Marca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_marcas", models.CharField(max_length=100)),
                ("tipo_do_Produto", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("descricao", models.TextField(blank=True)),
                (
                    "preco",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10, null=True
                    ),
                ),
                ("quantia", models.IntegerField(default=1, null=True)),
                ("validade", models.DateField(auto_now_add=True)),
                (
                    "capa",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="uploader.image",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="ACosmeticos.marca",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemCarrinho",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantidade", models.PositiveIntegerField(default=1)),
                (
                    "carrinho",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ACosmeticos.carrinho",
                    ),
                ),
                (
                    "compra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itens",
                        to="ACosmeticos.compra",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ACosmeticos.produto",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Favorito",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ACosmeticos.cliente",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ACosmeticos.produto",
                    ),
                ),
            ],
        ),
    ]

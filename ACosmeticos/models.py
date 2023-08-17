from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero_telefone = models.CharField(max_length=20, blank=True)
    endereco = models.TextField(blank=True)
    numero_casa = models.CharField(max_length=10, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.nome

    def nome_completo(self):
        return f"{self.nome}"


# Crição do models Carrinho

from clients.models import (
    Cliente,
)  # importar o modelo Cliente do seu aplicativo de clientes


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(
        "products.Produto", through="ItemCarrinho"
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Carrinho de {self.cliente.nome}"

from django.db import models
from django.contrib.auth.models import User

# Criação Cliente

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.IntegerField(max_length=16)
    email = models.EmailField(unique=True)
    numero_telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    numero_casa = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9, null=True, default="0")
    cpf = models.CharField(max_length=11, null=True, default="0")

    class Meta:
        verbose_name_plural = "Clientes"

 # importar o modelo Cliente do seu aplicativo de clientes

    def __str__(self):
        return self.nome

    def nome_completo(self):
        return f"{self.nome}"

# Criação Carrinho

class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total_da_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # data_do_pedido = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"Carrinho de {self.cliente.nome}"
    
# Criação Marcas
class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        Entregue = 4, 'Entregue'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO, null=True)

class Marcas(models.Model):
    nome_marcas = models.CharField(max_length=100)
    tipo_do_Produto = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_marcas

# Produto

class Produto(models.Model):
    idProduto = models.IntegerField()
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    marca = models.ForeignKey(Marcas, on_delete=models.PROTECT)
    quantia = models.IntegerField(null=True, default=1)
    validade = models.DateField(auto_now_add=True)
    # imagem = models.ImageField(upload_to='products/')

    
    def __str__(self):
        return self.nome

# Criação ItemCarrinho
    
class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}"

# Criação Favorito

class Favorito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente.nome} - {self.produto.nome}"

# Criação Forma de pagamento

class FormaPagamento(models.Model):
    tipo_de_pagamento = models.CharField(max_length=100)
    quantidade_de_parcelas = models.PositiveIntegerField(default=1, blank=True)

    def __str__(self):
        return self.tipo_de_pagamento
    


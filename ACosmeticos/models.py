from django.db import models

# Create your models here.


class Cliente(models.Model):
    # idCliente = models.IntegerField()
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero_telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    numero_casa = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

    def nome_completo(self):
        return f"{self.nome}"

 # importar o modelo Cliente do seu aplicativo de clientes


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # total_da_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # data_do_pedido = models.DateField(auto_created=True)

    def __str__(self):
        return f"Carrinho de {self.cliente.nome}"
    

class Marcas(models.Model):
    nome_marcas = models.CharField(max_length=100)
    tipo_do_Produto = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_marcas


class Produto(models.Model):
    idProduto = models.IntegerField()
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    marca = models.ForeignKey(Marcas, on_delete=models.PROTECT, null=True)
    validade = models.DateField(auto_now_add=True)
    # imagem = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.nome
    
class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    #  def __str__(self):
    #     # return f"{self.quantidade} x {self.produto.nome} em {self.carrinho.cliente.nome}"
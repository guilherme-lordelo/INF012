from django.db import models
from datetime import datetime
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.

owner = models.ForeignKey('auth.User', related_name='sistema', on_delete=models.CASCADE)
highlighted = models.TextField()

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])



class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.IntegerField()
    rg = models.IntegerField()
    cnh = models.IntegerField()
    email = models.EmailField()
    senha = models.CharField(max_length=12)

    def _str_(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=120)
    cnpj = models.IntegerField()
    telefone = models.IntegerField()
    email = models.EmailField()
    senha = models.CharField(max_length=12)

    def _str_(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.IntegerField()
    rg = models.IntegerField()
    cnh = models.IntegerField()
    email = models.EmailField()
    senha = models.CharField(max_length=12)

    def _str_(self):
        return self.nome

CLASSIFICASSOES = (
        ('utilitario', 'UTILITARIO'),
        ('passeio', 'PASSEIO'),
        ('familiar', 'FAMILIAR'),
        ('esporte', 'ESPORTE'),
        ('carga', 'CARGA'),
)
CORES = (
        ('verde', 'VERDE'),
        ('amarelo', 'AMARELO'),
        ('vermelho', 'VERMELHO'),
        ('branco', 'BRANCO'),
        ('preto', 'PRETO'),
        ('azul', 'AZUL')
)

received_datetime_repr = '1950-01-01 00:00:00'
 # convert to datetime object
received_datetime = datetime.strptime(received_datetime_repr, '%Y-%m-%d %H:%M:%S')
my_date_obj = received_datetime.date()

class Veiculo(models.Model):

    classificacao = models.CharField(max_length=20, choices=CLASSIFICASSOES)
    placa = models.CharField(max_length=10)
    cor = models.CharField(max_length=10, choices=CORES)
    chassi = models.IntegerField()
    foto = models.ImageField()
    gps = models.BooleanField(default=False)
    cadeiras = models.IntegerField(default=5)
    tracao = models.BooleanField(default=False)
    ultimadatadisponivel = models.DateField(default=my_date_obj)
    idade = models.DateField(default=my_date_obj)


    def _str_(self):
        return self.reservado







from django.db import models

from avaliacao.models import Avaliacao
from comentario.models import Comentario
from endereco.models import Endereco
from atracao.models import Atracao


class DocIdentificacao(models.Model):
    description = models.CharField(max_length=100)  

    class Meta:
        verbose_name = 'Documento de Identificação'
        verbose_name_plural = 'Documentos de Identificação'


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    campo_teste = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True
    )
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    doc_identificacao = models.OneToOneField(
        DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Ponto Turístico'
        verbose_name_plural = 'Pontos Turísticos'

    @property
    def descricao_completa2(self):
       return '%s - %s' % (self.nome, self.descricao)

    def __str__(self):
        return self.nome
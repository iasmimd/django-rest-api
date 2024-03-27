# Generated by Django 5.0.2 on 2024-03-27 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_alter_atracao_options'),
        ('avaliacao', '0002_alter_avaliacao_options'),
        ('comentario', '0002_alter_comentario_options'),
        ('core', '0002_alter_pontoturistico_options'),
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.atracao'),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacao.avaliacao'),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='campo_teste',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(to='comentario.comentario'),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
        ),
    ]

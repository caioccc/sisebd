# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-02 00:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('primeira_entrada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('ofertas', models.CharField(max_length=10)),
                ('biblias', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('revistas', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('visitantes', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('faltosos', models.ManyToManyField(related_name='aula_faltosos', to='app.Aluno')),
                ('presentes', models.ManyToManyField(related_name='aula_presentes', to='app.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade_minima', models.IntegerField()),
                ('idade_maxima', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alunos', models.ManyToManyField(to='app.Aluno')),
                ('aulas', models.ManyToManyField(to='app.Aula')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('classes', models.ManyToManyField(to='app.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='Igreja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_responsavel', models.CharField(max_length=100)),
                ('email_responsavel', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('nome_igreja', models.CharField(max_length=100)),
                ('qtd_membros', models.IntegerField(blank=True, null=True)),
                ('foto', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('primeira_entrada', models.BooleanField(default=False)),
                ('alunos', models.ManyToManyField(to='app.Aluno')),
                ('aulas', models.ManyToManyField(to='app.Aula')),
                ('classes', models.ManyToManyField(to='app.Classe')),
                ('departamentos', models.ManyToManyField(to='app.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(blank=True, choices=[('', ''), ('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=50, null=True)),
                ('nome_pai', models.CharField(blank=True, max_length=100, null=True)),
                ('nome_mae', models.CharField(blank=True, max_length=100, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('estado_civil', models.CharField(blank=True, choices=[('', ''), ('Solteiro(a)', 'Solteiro(a)'), ('Casado(a)', 'Casado(a)'), ('Viuvo(a)', 'Viuvo(a)'), ('Divorciado(a)', 'Divorciado(a)')], max_length=100, null=True)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefone_residencial', models.CharField(blank=True, max_length=30, null=True)),
                ('telefone_comercial', models.CharField(blank=True, max_length=30, null=True)),
                ('telefone_celular', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.BooleanField(default=True)),
                ('endereco', models.CharField(blank=True, max_length=200, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
                ('cep', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('primeira_entrada', models.BooleanField(default=False)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='igreja',
            name='professores',
            field=models.ManyToManyField(to='app.Professor'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='professores',
            field=models.ManyToManyField(to='app.Professor'),
        ),
        migrations.AddField(
            model_name='classe',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Professor'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pessoa'),
        ),
    ]
# Generated by Django 2.2.5 on 2019-09-04 14:06
# flake8: noqa
# fmt: off

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'vaga',
                'verbose_name_plural': 'vagas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('obrigatorio', models.BooleanField(default=True)),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vagas.Vaga')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vagas.Vaga')),
            ],
        ),
    ]

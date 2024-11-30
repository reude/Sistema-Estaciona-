# Generated by Django 5.1.1 on 2024-11-30 17:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VeiculoSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('tipo_veiculo', models.CharField(choices=[('carro', 'Carro'), ('moto', 'Moto')], max_length=5)),
                ('placa', models.CharField(max_length=10)),
                ('publico', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SaidaSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_saida', models.DateField()),
                ('hora_saida', models.TimeField()),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saidas', to=settings.AUTH_USER_MODEL)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saidas', to='usuarios.veiculoset')),
            ],
        ),
        migrations.CreateModel(
            name='EntradaSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to=settings.AUTH_USER_MODEL)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to='usuarios.veiculoset')),
            ],
        ),
    ]

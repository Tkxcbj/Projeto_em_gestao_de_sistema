# Generated by Django 4.1.2 on 2022-11-29 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome da Empresa')),
                ('cnpj', models.CharField(max_length=50, unique=True, verbose_name='CNPJ')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255, verbose_name='Senha')),
                ('access_level', models.IntegerField(choices=[(1, 'Nível 1'), (2, 'Nível 2')], default=1, verbose_name='Nível de Aceso')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.firm')),
            ],
        ),
    ]

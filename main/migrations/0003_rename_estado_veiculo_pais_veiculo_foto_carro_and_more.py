# Generated by Django 4.1.2 on 2022-11-02 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_empresa_veiculo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='estado',
            new_name='pais',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='foto_carro',
            field=models.ImageField(null=True, upload_to='main/carros/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(max_length=50, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='modelo',
            field=models.CharField(max_length=50, verbose_name='Modelo do Veículo'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='num_chassi',
            field=models.CharField(max_length=17, unique=True, verbose_name='Número do Chassi'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='utima_localizacao',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
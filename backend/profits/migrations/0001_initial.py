# Generated by Django 3.2.9 on 2021-11-11 15:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.CharField(default=None, max_length=128)),
                ('operacao', models.CharField(choices=[('COMPRA', 'BUY'), ('VENDA', 'SELL')], max_length=6)),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('quantidade', models.PositiveSmallIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('custos', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]

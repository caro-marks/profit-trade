# Generated by Django 3.2.9 on 2021-11-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profits', '0003_alter_trade_quantidade_acumulada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='preco_medio',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
    ]

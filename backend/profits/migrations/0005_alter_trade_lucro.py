# Generated by Django 3.2.9 on 2021-11-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profits', '0004_alter_trade_preco_medio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='lucro',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
    ]

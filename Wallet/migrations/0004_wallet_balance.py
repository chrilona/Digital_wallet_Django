# Generated by Django 4.0.6 on 2022-07-31 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0003_transaction_rename_adress_customer_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='balance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
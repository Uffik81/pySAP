# Generated by Django 3.2.5 on 2021-07-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Наименоание товара', max_length=64)),
                ('gtin', models.CharField(help_text='GTIN', max_length=14)),
                ('sku', models.IntegerField(help_text='Код товара')),
            ],
        ),
    ]

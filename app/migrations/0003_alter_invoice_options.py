# Generated by Django 4.2.13 on 2024-06-18 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_invoice_invoice_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ['creation_date']},
        ),
    ]
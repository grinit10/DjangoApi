# Generated by Django 2.1.2 on 2018-11-15 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20181115_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]

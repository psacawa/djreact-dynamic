# Generated by Django 2.2.6 on 2019-10-16 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='created',
        ),
    ]

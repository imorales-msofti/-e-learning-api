# Generated by Django 3.1 on 2020-08-12 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200810_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='approved',
        ),
    ]

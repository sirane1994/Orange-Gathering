# Generated by Django 2.2.6 on 2019-12-02 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_auto_20191202_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventinfo',
            name='slug',
        ),
    ]

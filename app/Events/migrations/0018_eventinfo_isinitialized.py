# Generated by Django 2.2.6 on 2019-12-16 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0017_auto_20191216_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinfo',
            name='IsInitialized',
            field=models.BooleanField(default=False),
        ),
    ]
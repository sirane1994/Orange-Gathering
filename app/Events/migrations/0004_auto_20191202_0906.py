# Generated by Django 2.2.6 on 2019-12-02 09:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_eventinfo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, max_length=255, unique=True),
        ),
    ]
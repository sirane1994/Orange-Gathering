# Generated by Django 2.2.6 on 2019-12-01 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_remove_profileinfo_dateofbirth'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='dateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profileinfo',
            name='phoneNumber',
            field=models.BigIntegerField(),
        ),
    ]

# Generated by Django 4.2.20 on 2025-05-05 21:16

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contactmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='phone_number',
            field=models.CharField(default=1, max_length=12, validators=[accounts.validators.validate_iranian_cellphone_number]),
            preserve_default=False,
        ),
    ]

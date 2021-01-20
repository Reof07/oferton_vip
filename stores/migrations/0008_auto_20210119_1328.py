# Generated by Django 3.1.5 on 2021-01-19 17:58

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_auto_20210119_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='cell_phone',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='local_phone',
        ),
        migrations.AddField(
            model_name='phone',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='phone',
            name='type_phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='type phone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='url',
            field=models.URLField(blank=True, verbose_name='url'),
        ),
    ]

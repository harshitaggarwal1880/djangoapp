# Generated by Django 4.2.4 on 2023-09-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0011_dosagetime_day_alter_dosagetime_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='custom_frequency',
            field=models.TextField(null=True),
        ),
    ]

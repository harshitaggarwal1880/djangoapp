# Generated by Django 4.2.4 on 2023-09-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0010_eventmedication'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosagetime',
            name='day',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterModelTable(
            name='dosagetime',
            table='DosageTime',
        ),
    ]
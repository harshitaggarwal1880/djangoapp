# Generated by Django 4.2.4 on 2023-08-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0005_medicine_additional_notes_medicine_dosage_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosagetime',
            name='event_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
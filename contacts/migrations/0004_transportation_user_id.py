# Generated by Django 4.1.7 on 2023-03-11 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_transportation_listing_transportation_listing_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportation',
            name='user_id',
            field=models.IntegerField(blank=True, default=2),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('owner_phone_number', models.CharField(max_length=100)),
                ('onwer_address', models.CharField(max_length=255)),
                ('owner_pincode', models.IntegerField()),
                ('no_of_boxes', models.IntegerField()),
                ('truck_requirement', models.CharField(max_length=100)),
            ],
        ),
    ]

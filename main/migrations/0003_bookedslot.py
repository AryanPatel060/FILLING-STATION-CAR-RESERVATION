# Generated by Django 4.1.7 on 2023-08-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_fuelstations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookedslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fuelstations_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('slot_number', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]

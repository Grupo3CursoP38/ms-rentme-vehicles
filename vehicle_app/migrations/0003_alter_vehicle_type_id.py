# Generated by Django 3.2.9 on 2021-11-24 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_app', '0002_alter_vehicle_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_type',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False, unique=True),
        ),
    ]
# Generated by Django 5.1.3 on 2025-02-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='request_type',
            field=models.CharField(choices=[('new', 'New Connection'), ('repair', 'Repair'), ('maintenance', 'Maintenance')], max_length=20),
        ),
    ]

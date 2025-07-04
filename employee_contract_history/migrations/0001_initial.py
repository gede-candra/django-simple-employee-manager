# Generated by Django 5.2.3 on 2025-06-23 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_profile', '0002_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.CharField(max_length=100)),
                ('contract_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('file', models.FileField(blank=True, null=True, upload_to='contracts/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_profile.user')),
            ],
        ),
    ]

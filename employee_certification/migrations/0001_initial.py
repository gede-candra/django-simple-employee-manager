# Generated by Django 5.2.3 on 2025-06-23 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_profile', '0003_remove_user_id_alter_user_id_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_name', models.CharField(max_length=100)),
                ('certification_number', models.CharField(max_length=100)),
                ('date_issued', models.DateField()),
                ('validity_period', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_profile.user')),
            ],
        ),
    ]

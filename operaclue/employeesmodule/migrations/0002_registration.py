# Generated by Django 5.0.2 on 2024-03-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeesmodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
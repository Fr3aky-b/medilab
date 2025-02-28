# Generated by Django 5.1.6 on 2025-02-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0003_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('totalbeds', models.IntegerField()),
                ('availablebeds', models.IntegerField()),
            ],
        ),
    ]

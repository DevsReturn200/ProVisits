# Generated by Django 4.2.7 on 2024-01-30 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=1000)),
                ('date', models.CharField(default=datetime.date(2024, 1, 30), max_length=20)),
                ('time', models.CharField(default='15:15:16', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('cardname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=100)),
                ('phone', models.CharField(default='', max_length=15)),
                ('address', models.CharField(default='', max_length=100)),
                ('whatsaspp', models.CharField(default='', max_length=15)),
                ('email', models.CharField(default='', max_length=50)),
                ('website', models.CharField(default='', max_length=50)),
                ('facebook', models.CharField(default='', max_length=200)),
                ('instagram', models.CharField(default='', max_length=200)),
                ('twitter', models.CharField(default='', max_length=200)),
                ('linkedin', models.CharField(default='', max_length=200)),
                ('youtube', models.CharField(default='', max_length=200)),
                ('about', models.CharField(default='', max_length=1000)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageID', models.CharField(default='', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('cardname', models.CharField(max_length=100)),
                ('date', models.CharField(default=datetime.date(2024, 1, 30), max_length=20)),
                ('time', models.CharField(default='15:15:16', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=1000)),
                ('date', models.CharField(default=datetime.date(2024, 1, 30), max_length=20)),
                ('time', models.CharField(default='15:15:16', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('membership', models.CharField(default='Personal', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.CharField(max_length=20)),
                ('cardname', models.CharField(max_length=100)),
                ('date', models.CharField(default=datetime.date(2024, 1, 30), max_length=20)),
                ('time', models.CharField(default='15:15:16', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=100)),
                ('date', models.CharField(default=datetime.date(2024, 1, 30), max_length=12)),
                ('time', models.CharField(default='15:15', max_length=5)),
                ('host', models.CharField(default='', max_length=50)),
            ],
        ),
    ]

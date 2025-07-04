# Generated by Django 5.1.2 on 2025-05-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('contact', models.CharField(max_length=10)),
                ('name', models.CharField(default='', max_length=100)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]

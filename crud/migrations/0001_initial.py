# Generated by Django 4.1.4 on 2023-07-01 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.CharField(max_length=100)),
                ('eaddress', models.CharField(max_length=100)),
                ('ephone', models.CharField(max_length=100)),
            ],
        ),
    ]

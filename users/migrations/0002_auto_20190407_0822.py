# Generated by Django 2.2 on 2019-04-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
    ]

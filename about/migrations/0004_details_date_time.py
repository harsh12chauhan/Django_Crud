# Generated by Django 4.2.5 on 2023-09-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_details_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='date_Time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

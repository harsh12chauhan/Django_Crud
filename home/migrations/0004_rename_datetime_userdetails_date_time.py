# Generated by Django 4.2.5 on 2023-09-23 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_userdetails_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='dateTime',
            new_name='date_Time',
        ),
    ]

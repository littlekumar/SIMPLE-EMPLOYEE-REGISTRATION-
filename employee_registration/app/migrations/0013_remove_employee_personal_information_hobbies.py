# Generated by Django 2.2.3 on 2019-09-03 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190903_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_personal_information',
            name='HOBBIES',
        ),
    ]

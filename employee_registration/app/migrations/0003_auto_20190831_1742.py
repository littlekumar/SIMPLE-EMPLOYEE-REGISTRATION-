# Generated by Django 2.2.3 on 2019-08-31 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee_registration_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_registration',
            name='image',
            field=models.FileField(upload_to='employees_images/'),
        ),
    ]

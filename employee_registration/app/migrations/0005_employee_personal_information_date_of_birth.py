# Generated by Django 2.2.3 on 2019-09-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190902_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_personal_information',
            name='Date_of_Birth',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]

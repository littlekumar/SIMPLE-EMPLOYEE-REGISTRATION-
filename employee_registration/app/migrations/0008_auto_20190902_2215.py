# Generated by Django 2.2.3 on 2019-09-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_employee_intermediate_education_employee_pg_education_employee_ug_education_employee_x_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_intermediate_education',
            name='ID_NO',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee_pg_education',
            name='ID_NO',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee_ug_education',
            name='ID_NO',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee_x_education',
            name='ID_NO',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

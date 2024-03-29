# Generated by Django 2.2.3 on 2019-09-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190831_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Personal_Information',
            fields=[
                ('ID_NO', models.AutoField(primary_key=True, serialize=False)),
                ('FIRST_NAME', models.CharField(max_length=30)),
                ('LAST_NAME', models.CharField(max_length=30)),
                ('EMAIL_ID', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('MOBILE_NUMBER', models.IntegerField()),
                ('GENDER', models.FileField(upload_to='employees_images/')),
                ('ADDRESS', models.CharField(max_length=200)),
                ('CITY', models.CharField(max_length=30)),
                ('PIN_CODE', models.IntegerField()),
                ('STATE', models.CharField(max_length=30)),
                ('COUNTRY', models.CharField(max_length=30)),
                ('HOBBIES', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee_Registration',
        ),
    ]

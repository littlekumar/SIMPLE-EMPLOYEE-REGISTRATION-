from django.db import models
from datetime import date

class Manager_Login(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=30)
class Employee_Personal_Information(models.Model):
    ID_NO = models.AutoField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=30)
    LAST_NAME = models.CharField(max_length=30)
    EMAIL_ID = models.EmailField(unique=True)
    Date_of_Birth = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    MOBILE_NUMBER = models.IntegerField()
    image = models.FileField(upload_to='employees_images/')
    GENDER = models.CharField(max_length=30)
    ADDRESS = models.CharField(max_length=200)
    CITY = models.CharField(max_length=30)
    PIN_CODE = models.IntegerField()
    STATE = models.CharField(max_length=30)
    COUNTRY = models.CharField(max_length=30)

class Employee_X_Education(models.Model):
    ID_NO = models.IntegerField(primary_key=True)
    Start_Date = models.IntegerField(default=0)
    Completion_Date = models.IntegerField(default=0)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Education_Institution = models.CharField(max_length=30)
    PERCENTAGE = models.IntegerField(default=0)
    Maths_PERCENTAGE = models.IntegerField(default=0)
    Board_or_University = models.CharField(max_length=30)
    Cousre_Type = models.CharField(max_length=30)


class Employee_Intermediate_Education(models.Model):
    ID_NO = models.IntegerField(primary_key=True)
    Start_Date = models.IntegerField(default=0)
    Completion_Date = models.IntegerField(default=0)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Education_Institution = models.CharField(max_length=30)
    Board_or_University = models.CharField(max_length=30)
    PERCENTAGE = models.IntegerField(default=0)
    BRANCH = models.CharField(max_length=30, default="")
    Cousre_Type = models.CharField(max_length=30)


class Employee_UG_Education(models.Model):
    ID_NO = models.IntegerField(primary_key=True)
    Start_Date = models.IntegerField(default=0)
    Completion_Date = models.IntegerField(default=0)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Education_Institution = models.CharField(max_length=30)
    PERCENTAGE = models.IntegerField(default=0)
    BRANCH = models.CharField(max_length=30, default="")
    Board_or_University = models.CharField(max_length=30)
    Cousre_Type = models.CharField(max_length=30)


class Employee_PG_Education(models.Model):
    ID_NO = models.IntegerField(primary_key=True)
    Start_Date = models.IntegerField(default=0)
    Completion_Date = models.IntegerField(default=0)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Education_Institution = models.CharField(max_length=30)
    PERCENTAGE = models.IntegerField(default=0)
    BRANCH = models.CharField(max_length=30,default="")
    Board_or_University = models.CharField(max_length=30)
    Cousre_Type = models.CharField(max_length=30)

class Employee_Experience(models.Model):
    ID_NO = models.IntegerField(primary_key=True,default=0)
    YEAR = models.IntegerField(default=0)
    MONTH = models.IntegerField(default=0)
    OLD_EMPLOYEE = models.CharField(max_length=30)
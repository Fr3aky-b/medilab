from django.db import models

# Create your models here.
class Patient(models.Model):
  fullname=models.CharField(max_length=100)
  age=models.IntegerField()
  email=models.EmailField()
  message=models.TextField()


  def __str__(self):
    return self.fullname



class Doctor(models.Model):
  name=models.CharField(max_length=50)
  department=models.CharField(max_length=75)
  email=models.EmailField()
  status=models.CharField(max_length=60)
  age=models.IntegerField
  qualification=models.CharField(max_length=77)


  def __str__(self):
    return self.name


class Staff(models.Model):
  firstname=models.CharField(max_length=50)
  lastname=models.CharField(max_length=50)
  position=models.CharField(max_length=50)
  phonenumber=models.CharField(max_length=50  )
  email=models.EmailField()
  hiredate=models.DateField()

  def __str__(self):
    return self.firstname ;lastname

class Ward(models.Model):
  name=models.CharField(max_length=50)
  totalbeds=models.IntegerField()
  availablebeds=models.IntegerField()

  def __str__(self):
    return self.name

class Appointment1(models.Model):
  name=models.CharField(max_length=50)
  email=models.EmailField()
  subject = models.CharField(max_length=50)
  message=models.TextField()













from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(null=True,max_length=50)
    models.IntegerField(null=True,max_length=50)
    department =models.CharField(null=True,max_length=50)
    
    
    def __str__(self):
        return self.Name
    
    
class Patient(models.Model):
    Name = models.CharField(null=True,max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.TextField()
    
    def __str__(self):
        return self.Name
    
class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    
    def __str__(self):
        return self.Doctor.Name + "__"+self.Patient.Name

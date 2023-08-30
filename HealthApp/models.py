from django.db import models

# Create your models here.

class Patient(models.Model):
    uid = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1)  # Assuming 'M' or 'F' for Male/Female
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    otp = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Lab(models.Model):
    lab_id = models.CharField(primary_key=True, max_length=12)
    lab_name = models.CharField(max_length=100)
    lab_address = models.CharField(max_length=200)  
    lab_phone = models.CharField(max_length=15) 
    lab_password = models.CharField(max_length=1000, null=True, blank=True)    

    def __str__(self):
        return self.lab_name
    
class Reports(models.Model):
    report_no = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    date = models.DateField()
    test_name = models.CharField(max_length=100)
    report_pdf = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Report {self.report_no} for {self.patient.name} from Lab {self.lab.lab_name}"
    
class Doctor(models.Model):
    doctor_id = models.CharField(primary_key=True, max_length=9)
    doctor_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    doctor_number = models.CharField(max_length=15)
    doctor_password = models.CharField(max_length=1000, null=True, blank=True)    


    def __str__(self):
        return self.doctor_name
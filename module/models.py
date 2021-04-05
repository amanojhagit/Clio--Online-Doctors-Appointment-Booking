from django.db import models

# Create your models here.
class patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    email = models.EmailField()
    gender = models.CharField(max_length=1)
    address = models.TextField()
    mobile = models.BigIntegerField()


class doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    address = models.TextField()
    mobile = models.BigIntegerField()
    specialization = models.TextField()
    def __str__(self):
        return self.name


class receptionist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    hospital = models.TextField()

class appointments(models.Model):
    id =models.AutoField(primary_key=True)
    patient = models.ForeignKey('patient',on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctor',on_delete=models.CASCADE)
    slot_date = models.DateField()
    slot_time = models.TimeField(blank=True,null=True)
    createdAt = models.DateField()
    updatedAt = models.DateField()
    status = models.CharField(max_length=10)
    prescription = models.CharField(max_length=2000,blank=True)

class labReports(models.Model):
    patient = models.ForeignKey('patient',on_delete=models.CASCADE)
    reports = models.FileField(upload_to=None)
    upload_date = models.DateField()
    upload_time = models.TimeField()
    doneBy = models.ForeignKey('laboratory',on_delete=models.CASCADE)

class laboratory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    contact_no  = models.BigIntegerField()

class timeslotGeneral(models.Model):   # ALL Available timeslot 
    id = models.AutoField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    


class timeslotDetails(models.Model):  # particular timeslot choosen by doctor
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey('doctor',on_delete=models.CASCADE)
    timeslot = models.ForeignKey('timeslotGeneral',on_delete=models.CASCADE)
    isActive = models.BooleanField()
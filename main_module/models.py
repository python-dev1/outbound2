from django.db import models

# Create your models here.
class userdata(models.Model):
    # firststate=models.CharField(max_length=100)
    # IssuerName=models.CharField(max_length=100)
    # DelinquencyDate=models.CharField(max_length=100)
    # TotalPayment=models.CharField(max_length=100)
    # Lastpaydate=models.CharField(max_length=100)
    # Lastpayamount=models.CharField(max_length=100)
    # totalpaidsincechargeoff=models.CharField(max_length=100)
    CODate = models.CharField(max_length=100)  # required  charge off date
    AccountOpenDate = models.CharField(max_length=100)  # required
    CurBalance = models.CharField(max_length=100)  # required
    pbirthdate = models.CharField(max_length=100)  # required
    firstcity = models.CharField(max_length=100)  # required
    firstzippostal = models.CharField(max_length=100)  # required
    score = models.CharField(max_length=100)  # it will be predicted


class registration(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    username= models.CharField(max_length=80)
    password= models.CharField(max_length=80)

    def __str__(self):
        return self.name

class login(models.Model):
    email = models.CharField(max_length=80)
    password= models.CharField(max_length=80)

class files(models.Model):
    myfile=models.FileField()



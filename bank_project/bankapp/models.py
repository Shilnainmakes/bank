from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
]

ACCOUNT_CHOICES = [
    ('S', 'Saving Account'),
    ('C', 'Current Account'),
]

class District(models.Model):
    name=models.CharField(max_length=50, default=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,default=True)

    def __str__(self):
        return self.name

class MaterialOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    account_type = models.CharField(max_length=1,choices=ACCOUNT_CHOICES)
    materials_provided = models.ManyToManyField(MaterialOption)



    def __str__(self):
        return self.name

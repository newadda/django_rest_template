from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Person(models.Model):
    registration_number = models.CharField(max_length=13,validators=[RegexValidator(regex="[0-9]+")]) ## 주민번호
    job = models.CharField(max_length=30)


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15,unique=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)



class House(models.Model):
    address = models.CharField(max_length=15,unique=True)
    persons = models.ManyToManyField(Person, through='PersonToHouse')

class PersonToHouse(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)


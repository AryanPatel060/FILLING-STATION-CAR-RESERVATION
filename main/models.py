from django.db import models

class User(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField()
    password = models.TextField("Password")
 # Create your models here.


class Fuelstations(models.Model):
    # station_id = models.BigAutoField('id',primary_key=True)
    station_name =  models.CharField('Station Name',max_length=128)
    city = models.CharField('City',max_length=64)
    state = models.CharField('State',max_length=32)

class Bookedslot(models.Model):
    Fuelstations_id= models.IntegerField()
    # stations_name=models.CharField('stationname',max_length=20)
    user_id=models.IntegerField()
    slot_number=models.IntegerField()
    date =models.DateField()
    # username = models.CharField('username',max_length=20)
    # email = models.EmailField()
    # contactno=models.IntegerField()
     

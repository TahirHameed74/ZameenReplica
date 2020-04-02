from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class houseParameters(models.Model):
	houseSize = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(50), MinValueValidator(0)]
     )
	price = models.BigIntegerField(
        default=0,
        validators=[MaxValueValidator(5000000000000), MinValueValidator(0)]
     )
	town = models.TextField()
	age = models.IntegerField()
	floor = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(3), MinValueValidator(1)]
     )
	isBasement = models.BooleanField()
	isGarden = models.BooleanField()
	servantRooms = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(2), MinValueValidator(0)]
     )
	numberOfBeds= models.IntegerField(
        default=1,
        validators=[MaxValueValidator(20), MinValueValidator(1)]
     )
	distanceFromPark = models.IntegerField(
        default=0,
     )
	distanceFromMosque = models.IntegerField(
        default=0,
     )
	distanceFromSchool = models.IntegerField(
        default=0,
     )
	distanceFromMarket = models.IntegerField(
        default=0,
     )
	distanceFromHospital = models.IntegerField(
        default=0,
     )

class carParameters(models.Model):
	brandType = models.TextField()
	city = models.TextField()
	assemblyType = models.TextField(
		default = 'local')
	price = models.IntegerField(
		default = 0
		)
	engineCapacity = models.IntegerField()
	registrationCity = models.IntegerField()
	yearlyModel = models.TextField()
	brandModel = models.TextField()
	engineType = models.TextField()
	color = models.TextField()
	engineDetail = models.TextField(
		default = 'Petrol'
		)
	Mileage = models.BigIntegerField(
		default = 0
		)
	










































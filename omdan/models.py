from django.db import models
from django.urls import reverse#used to generate URL's by reversing url patterns
import uuid #required for unique properties instances
# Create your models here.
class City (models.Model):
    #model representing the cities in a country
    city = models.CharField(max_length = 35, help_text = "enter name of the city")
    def __str__(self):
        #String for representing the model object(in admin site,etc)
        return self.city
class Neighborhood(models.Model):
    #model representing the neighborhood in a given city
    neighborhood = models.CharField(max_length = 35,help_text = "Enter neighborhood in a given city")
    city = models.ForeignKey('City',on_delete=models.SET_NULL,null=True)
    #Used ForeignKey because of one to many neighborhoods in one city
    class meta:
        ordering=("city_id")
    def __str__(self):
        #string for representing model object
        return self.city
class Property(models.Model):
    #model representing a specific property in file
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Unique id for this particular property in the database")
    city=models.CharField(max_length = 35,default=" ")
    #city=models.ForeignKey('City',on_delete=models.SET_NULL,null=True)
    neighborhood=models.CharField(max_length = 35,default=" ")
    #neighborhood=models.ForeignKey('Neighborhood',on_delete=models.SET_NULL,null=True)
    roomsnumber=models.DecimalField(max_digits=6,decimal_places=2)                      
    builtarea=models.DecimalField(max_digits=8,decimal_places=2)
    yearbuilt=models.IntegerField
    yearsold=models.IntegerField
    price= models.DecimalField(max_digits=10,decimal_places=2)
    class meta:
        ordering=("roomsnumber","builtarea")
    #def __str__(self):
        #string representing the model object
    #    return self.id
class Surfer(models.Model):    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Unique id for this particular property in the database")
    city=models.CharField(max_length = 35,default=" ")
    #city=models.ForeignKey('City',on_delete=models.SET_NULL,null=True)
    neighborhood=models.CharField(max_length = 35,default=" ")
    #neighborhood=models.ForeignKey('Neighborhood',on_delete=models.SET_NULL,null=True)
    roomsnumber=models.DecimalField(max_digits=6,decimal_places=2)                      
    builtarea=models.DecimalField(max_digits=8,decimal_places=2)
    price= models.DecimalField(max_digits=10,decimal_places=2)
    street=models.CharField(max_length=35,help_text="Enter Street")
    streetnumber=models.IntegerField(help_text="Enter Number")
    email=models.EmailField()
    surfingdate=models.DateField()
    class meta:
       ordering=("surfingdate","city")

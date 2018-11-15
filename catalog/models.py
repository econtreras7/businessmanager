from django.db import models
# Create your models here.
#for the reverse url function 
from django.urls import reverse # Used to generate URLs by reversing the URL patterns





class Service(models.Model):
    """Model representing creating a table"""
    name=models.CharField(max_length=100,help_text='Types of services provided/')
    cost=models.FloatField()

    #string representing the name of the service
    def __str__(self):
        return self.name
    #returns url acccess to specific service instance 
    #def get_absolute_url(self):
     #   return reverse('',args=[str(self.id)])
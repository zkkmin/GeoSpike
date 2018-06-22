from django.db import models

class Country(models.Model):
    country = models.TextField(primary_key=True)
    name = models.TextField(unique=True)
    country_code = models.CharField(max_length=5)
    

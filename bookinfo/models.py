from django.db import models

# Create your models here.
class AddressBook(models.Model):
	"""Address book data"""
	contact_address = models.CharField(max_length = 100)
	name = models.CharField(max_length = 100)
	mobile = models.CharField(max_length = 50)

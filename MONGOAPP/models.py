from django.db import models
from djangotoolbox.fields import ListField

class Posts(models.model):
	User = models.CharField()
	text = models.TextField()
	Comments = ListField()

class user(models.model):
	username = models.Charfield('max_length = 15')
	FullName = models.Charfield('max_length = 30')
	password = models.Charfield()
	Following = models.Charfield(15)




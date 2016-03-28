from django.db import models

class UserFeeds(models.Model):

	username = models.CharField(max_length = 15)
	user_post = models.CharField(max_length = 140)	
	date = models.DateField()

	class Meta:
		ordering = ['date']
		

class UserProfile(models.Model):
	UserName = models.CharField(max_length = 15)
	Name = models.CharField(max_length = 25)
	user_followers = models.CharField(max_length = 15,null=True)


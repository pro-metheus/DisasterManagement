from django.db import models
from django.contrib.auth.models import User
from .choices import USER_TYPES, STATES, ERNAKULAM_POST_OFFICES, DISASTER_TYPE, ALERT_TYPE, INSTITUTIONS
# Create your models here.


class Address(models.Model):
	house_name = models.TextField()
	locality = models.TextField(null=True)
	pin = models.CharField(max_length=6)
	state = models.CharField(choices =STATES , max_length=50)
	district = models.TextField()
	landmark = models.TextField(null=True)

	def save(self, *args, **kwargs):
		self.locality = ERNAKULAM_POST_OFFICES[self.pin]
		super().save(*args, **kwargs)

	def __str__(self):
		return self.house_name + self.pin

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	contact = models.CharField(max_length=13)
	user_type = models.CharField(choices=USER_TYPES, max_length=10)
	address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
	verified = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username


class Place(models.Model):
	pincode = models.CharField(max_length=6)
	post = models.TextField(null=True)
	poppulation = models.IntegerField()
	chief = models.OneToOneField(Profile, limit_choices_to = {'user_type':'SUP'}, on_delete=models.CASCADE)

	def __str__(self):
		return self.post

class Institution(models.Model):
	institution = models.CharField(choices=INSTITUTIONS, max_length=30)
	address = models.OneToOneField(Address, on_delete=models.CASCADE)
	contact = models.CharField(max_length=13)
	place = models.OneToOneField(Place, on_delete=models.CASCADE)


class Disaster(models.Model):
	record_date = models.DateField()
	disaster_type = models.CharField(choices=DISASTER_TYPE, max_length=20)
	alert = models.CharField(choices=ALERT_TYPE, max_length=20)
	verified = models.BooleanField(default=False)
	reported_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.place.pincode + self.disaster_type











from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from time import time
from datetime import datetime


def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)



# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=40, blank=False, null=True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return self.email



class Cv(models.Model):
	author = models.ForeignKey('auth.User')
	name = models.CharField(max_length=25, null = True)
	surname = models.CharField(max_length=25, null = True)
	address = models.CharField(max_length=100, blank=True)
	telephone = models.IntegerField()
	birth_date = models.DateField(blank=True, null=True)
	email = models.EmailField(max_length=50, null=True)
	skills = models.TextField(null=True)
	specialization = models.CharField(max_length=30, blank=True, null=True)
	interests = models.TextField(blank=True, null=True)
	summary = models.TextField(blank=True, null=True)
	thumbnail = models.FileField(upload_to=get_upload_file_name, blank=True)


	def zapisz(self):
		self.save()

	def __str__(self):
		return self.surname





class Search(models.Model):

	search_text = models.CharField(max_length=50)

	SORT_CHOICE = (
		('C', '----- Choose -----'),
		('N', 'Name'),
		('S', 'Surname'),
		('E', 'E-mail'),
	)

	sort = models.CharField(max_length=1, default=0, choices=SORT_CHOICE)

	def __str__(self):
		return self.search_text




class UserLink(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=('user'), related_name='links')

	university = models.CharField(max_length = 100)
	grade = models.CharField(max_length = 50)
	field = models.CharField(max_length = 50)
	city_1 = models.CharField(max_length=50)
	description_1 = models.TextField(max_length=350)
	study_1 = models.CharField(max_length=5)
	study_2 = models.CharField(max_length=5)


	def __str__(self):
		return self.university

	def save(self, *args, **kwargs):
		"""
		Attempt to match a user link to a recognised brand (LinkBrand).
		"""
		super(UserLink, self).save(*args, **kwargs)


class UserFirm(models.Model):

	userr = models.ForeignKey(settings.AUTH_USER_MODEL,
							verbose_name=('userr'),
							related_name='linkss')

	firma = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	city_2 = models.CharField(max_length=50)
	description_2 = models.CharField(max_length=350)
	fir_1 = models.CharField(max_length=5)
	fir_2 = models.CharField(max_length=5)



	def __str__(self):
		return self.firma

	def save(self, *args, **kwargs):
		"""
		Attempt to match a user link to a recognised brand (LinkBrand).
		"""
		super(UserFirm, self).save(*args, **kwargs)


class ProfileImage(models.Model):
    f = models.FileField(upload_to='profile/%Y/%m/%d')
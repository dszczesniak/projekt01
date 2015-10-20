from django.db import models

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
	address = models.CharField(max_length=100)
	telephone = models.IntegerField()
	birth_date = models.DateField(blank=True, null=True)
	email = models.EmailField(max_length=50, null=True)
	skills = models.TextField(null=True)
	specialization = models.CharField(max_length=30, blank=True, null=True)

	interests = models.TextField(blank=True, null=True)
	school = models.CharField(max_length=50, blank=True, null=True)
	start_learning_period = models.IntegerField(blank=True, null=True)
	end_learning_period = models.IntegerField(blank=True, null=True)
	title = models.CharField(max_length=20, blank=True, null=True)
	field_of_study = models.CharField(max_length=25, blank=True, null=True)

	firma = models.CharField(max_length=25, blank=True, null=True)
	position = models.CharField(max_length=25, blank=True, null=True)
	location = models.CharField(max_length=25, blank=True, null=True)
	start_work_period = models.IntegerField(blank=True, null=True)
	end_work_period = models.IntegerField(blank=True, null=True)

	summary = models.TextField(blank=True, null=True)



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
from django import forms
from .models import SignUp
from .models import Cv, Search


class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()
	


class SignUpForm(forms.ModelForm):

	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_emial(self):
		email = self.cleaned_data.get('email')
		return email

	def clean_full_name(self):
		full_name= self.cleaned_data.get('full_name')
		return full_name


class CvForm(forms.ModelForm):

	class Meta:
		model = Cv
		fields = ('name', 'surname', 'address', 'telephone', 'birth_date', 'email', 'skills', 'specialization', 'interests', 'school', 'start_learning_period',
			'end_learning_period', 'title',	'field_of_study', 'firma', 'position', 'location', 'start_work_period',	'end_work_period', 'summary', )

class SearchForm(forms.ModelForm):

	class Meta:
		model = Search
		fields = ('sort', 'search_text',)
from django import forms
from .models import SignUp
from .models import Cv, Search, Group, Skill, UserSkill, SkillMod
from django.forms.formsets import BaseFormSet
from datetime import datetime


class SendMessageForm(forms.Form):

	message = forms.CharField(
		widget=forms.Textarea(attrs={'rows': '5', 'cols': '60',}))
	


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
		fields = ('name', 'surname', 'address', 'telephone', 'birth_date', 'email', 'skills', 'specialization', 'interests', 'summary', 'thumbnail',)

class SearchForm(forms.ModelForm):

	class Meta:
		model = Search
		fields = ('sort', 'search_text',)


YEARS_CHOICES = tuple((str(n), str(n)) for n in range(1955, datetime.now().year + 1))

class LinkForm(forms.Form):
	#education

	university = forms.CharField(
		max_length=100,
		widget = forms.TextInput(attrs = {'placeholder': 'University',}), required = False)

	grade = forms.CharField(
		max_length = 50,
		widget = forms.TextInput(attrs = {'placeholder': 'Grade',}), required = False)

	field = forms.CharField(
		max_length = 50,
		widget = forms.TextInput(attrs = {'placeholder': 'Field of study',}), required = False)

	city_1 = forms.CharField(
		max_length = 50,
		widget = forms.TextInput(attrs = {'placeholder': 'City',}), required = False)

	description_1 = forms.CharField(
		max_length = 500,
		widget=forms.Textarea(attrs={'placeholder': ('Add some details about your education...'),'rows': '5', 'cols': '40',}), required=False)


	study_1 = forms.ChoiceField(
		choices=YEARS_CHOICES,
		required=False)

	study_2 = forms.ChoiceField(
		choices=YEARS_CHOICES,
		required=False)


	#experience

	firma = forms.CharField(
		max_length = 50,
		widget = forms.TextInput(attrs = {'placeholder': 'Firma',}), required = False)

	position = forms.CharField(
		max_length = 50,
		widget = forms.TextInput(attrs = {'placeholder': 'Position',}), required = False)

	city_2 = forms.CharField(
		max_length = 50,
		widget = forms.TextInput(attrs = {'placeholder': 'City',}), required = False)

	description_2 = forms.CharField(
		max_length = 500,
		widget=forms.Textarea(attrs={'placeholder': ('Add some details about your eexperience...'),'rows': '5', 'cols': '40',}), required=False)

	fir_1 = forms.ChoiceField(
		choices=YEARS_CHOICES,
		required=False)

	fir_2 = forms.ChoiceField(
		choices=YEARS_CHOICES,
		required=False)

	# skills

	skil = forms.CharField(
		max_length= 50,
		widget = forms.TextInput(attrs = {'placeholder': 'Skill',}), required = False)





class NameForm(forms.Form):
	study1 = forms.ChoiceField(label="Period of study",	choices=YEARS_CHOICES)
	study2 = forms.ChoiceField(label=" ",	choices=YEARS_CHOICES)



class ProfileForm(forms.Form):

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(ProfileForm, self).__init__(*args, **kwargs)

		self.fields['first_name'] = forms.CharField(
			max_length = 30,
			initial = self.user.first_name,
			widget = forms.TextInput(attrs={
			'placeholder': 'First Name',
			}))

		self.fields['last_name'] = forms.CharField(
			max_length = 30,
			initial = self.user.last_name,
			widget = forms.TextInput(attrs={
			'placeholder': 'Last Name',
			}))



class BaseLinkFormSet(BaseFormSet):
	def clean(self):

		if any(self.errors):
			return

		universitys = []
		fields = []
		duplicates = False

		for form in self.forms:
			if form.cleaned_data:
				university = form.cleaned_data['university']
				field = form.cleaned_data['field']
"""
				# Check that no two links have the same anchor or URL
				if university and field:
					if university in universitys:
						duplicates = True
					universitys.append(university)

					if field in fields:
						duplicates = True
					fields.append(field)

				if duplicates:
					raise forms.ValidationError(
						'Links must have unique anchors and URLs.',
						code='duplicate_links'
					)

				# Check that all links have both an anchor and URL
				if field and not university:
					raise forms.ValidationError(
						'All links must have an university.',
						code='missing_university'
					)
				elif university and not field:
					raise forms.ValidationError(
						'All links must have a field.',
						code='missing_field'
					)
"""



class ProfileImageForm(forms.Form):
	f = forms.FileField(label='Select a profile Image')






class GroupForm(forms.ModelForm):

	class Meta:
		model = Group
		fields = ('name',)







class BaseSkillFormSet(BaseFormSet):
	def clean(self):
		"""
		Adds validation to check that no skill is listed twice
		and that all skills have both a name and proficiency.
		"""
		if any(self.errors):
			return

		skills = []

		for form in self.forms:
			if form.cleaned_data:
				skill = form.cleaned_data['skill']
				proficiency = form.cleaned_data['proficiency']

				 # Check that no two skills are the same
				if skill and proficiency:
					if skill in skills:
						raise forms.ValidationError(
							_('Each skill can only be entered once.'),
							code='duplicate_skill'
						)

					skills.append(skill)

				# Check that all skills have both a name and proficiency
				if skill and not proficiency:

					raise forms.ValidationError(
						_('All skills must have a proficiency.'),
						code='missing_proficiency'
					)

				elif proficiency and not skill:
					raise forms.ValidationError(
						_('All skills must have a skill name.'),
						code='missing_skill_name'
					)



class SkillForm(forms.Form):
	"""
	Form for individual user skills
	"""
	skills = Skill.objects.all()
	skill = forms.ModelChoiceField(queryset=skills, required=False)

	proficiency = forms.ChoiceField(choices=UserSkill.PROFICIENCY_CHOICES,
									required=False)
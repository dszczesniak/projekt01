import os
import zipfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from .forms import SendMessageForm, SignUpForm, CvForm, MemberForm
from .forms import LinkForm, BaseLinkFormSet, ProfileForm, BaseSkillFormSet
from .forms import ProfileImageForm, GroupForm, SkillForm
from .models import ProfileImage
from .models import UserLink, UserFirm, UserSkill
from .models import Cv, Person, Group, Membership
from django.views.generic import View, FormView, DetailView, ListView
from datetime import datetime


# Create your views here.
def home(request):

	if request.user.is_authenticated():
		cvs = Cv.objects.filter(author = request.user)

		if cvs:
			con = {
				"cvs": cvs,
			}

			return render(request, "home.html", con)

		else:
			if request.method == "POST":
				form = CvForm(request.POST)
				if form.is_valid():
					cv = form.save(commit=False)
					cv.author = request.user
					cv.zapisz()
					return redirect('proj.views.cv_detail', pk=cv.pk)
			else:
				form = CvForm()
			return render(request, 'new_cv.html', {'form': form})

	else:
		return render(request, "home.html", )





def send_message(request, pk):

	form = SendMessageForm(request.POST or None)
	cv = Cv.objects.filter(author = request.user)
	cvs = get_object_or_404(Cv, pk=pk)

	if form.is_valid():
		
		form_message = form.cleaned_data.get("message")

		subject = 'ITFinder - Message from user' 
		from_emial = settings.EMAIL_HOST_USER
		for c in cv:
			start = 'Message from: '+c.email
			end = c.name+" "+c.surname

		to_email = [cvs.email]

		contact_message = "%s: \n\n%s \n\ngreetings, %s" %(start, form_message, end)

		send_mail(subject, contact_message, from_emial, to_email, fail_silently=False)

		return redirect('proj.views.cv_detail', pk=cvs.pk)

	con = {
		"form": form,
		"cv": cv,
		"cvs": cvs
	}

	return render(request, "send_message.html", con)





@login_required
def new_cv(request):
	if request.method == "POST":
		form = CvForm(request.POST, request.FILES)

		if form.is_valid():
			cv = form.save(commit=False)
			cv.author = request.user
			cv.save()

			return redirect('proj.views.cv_detail', pk=cv.pk)
	else:
		form = CvForm()
	return render(request, 'new_cv.html', {'form': form})





@login_required
def myprofile(request):
	cvs = Cv.objects.filter(author = request.user)
	return render(request, 'myprofile.html', {'cvs': cvs})





@login_required
def edit_cv(request, pk):
	cv = get_object_or_404(Cv, pk=pk)
	if cv.author == request.user:
		if request.method == "POST":
			form = CvForm(request.POST, request.FILES, instance=cv)
			if form.is_valid():
				cv = form.save(commit=False)
				cv.author = request.user
				cv.save()
				return redirect('proj.views.cv_detail', pk=cv.pk)
		else:
			form = CvForm(instance=cv)
		return render(request, 'edit_cv.html', {'form': form})
	else:
		return redirect('proj.views.home')




User = get_user_model()

def cv_detail(request, pk):
	user = request.user

	cv = get_object_or_404(Cv, pk=pk)

	user_links = UserLink.objects.filter()
	user_firms = UserFirm.objects.filter()
	user_skills = UserSkill.objects.filter()


	# listed_users = User.objects.all()

	con = {
			"cv": cv,
			# "listed_users": listed_users,
			"user_links": user_links,
			"user_firms": user_firms,
			"user_skills": user_skills,
			}

	return render(request, 'cv_detail.html', con)







@login_required
def base_cv(request):

	con = {'cvs': Cv.objects.all()}
	return render(request, 'base_cv.html', con)








@login_required
def profile_settings(request):
	user = request.user

	LinkFormSet = formset_factory(LinkForm, formset=BaseLinkFormSet)

	# Get our existing link data for this user.  This is used as initial data.
	user_links = UserLink.objects.filter(user=request.user)


	link_data = [{'university': l.university, 'city_1': l.city_1, 'grade': l.grade, 'field': l.field, 'description_1': l.description_1, 'study_1': l.study_1, 'study_2': l.study_2,}
						for l in user_links]


	if request.method == 'POST':


		link_formset = LinkFormSet(request.POST)


		if link_formset.is_valid():
			
		# Now save the data for each form in the formset
			new_obj = []

			for link_form in link_formset:
				university = link_form.cleaned_data.get('university')
				city_1 = link_form.cleaned_data.get('city_1')
				grade = link_form.cleaned_data.get('grade')
				field = link_form.cleaned_data.get('field')
				description_1 = link_form.cleaned_data.get('description_1')
				study_1 = link_form.cleaned_data.get('study_1')
				study_2 = link_form.cleaned_data.get('study_2')


				if university and field:
					new_obj.append(UserLink(user=user, university=university, city_1=city_1, grade=grade, field=field, description_1 = description_1, study_1 = study_1, study_2 = study_2))

			try:
				with transaction.atomic():
				#Replace the old with the new
					UserLink.objects.filter(user=user).delete()
					UserLink.objects.bulk_create(new_obj)
	
					# And notify our users that it worked
					messages.success(request, 'You have updated your profile.')

			except IntegrityError: #If the transaction failed
				messages.error(request, 'There was an error saving your profile.')
				return redirect(reverse('profile_settings'))

	else:

		link_formset = LinkFormSet(initial=link_data)

	context = {

		'link_formset': link_formset,

	}
			
	return render(request, 'edit_profile.html', context)









@login_required
def update_exp(request):
	user = request.user

	LinkFormSet = formset_factory(LinkForm, formset=BaseLinkFormSet)

	# Get our existing link data for this user.  This is used as initial data.
	user_firms = UserFirm.objects.filter(user=user).order_by('firma')


	link_data = [{'firma': l.firma, 'city_2': l.city_2, 'position': l.position, 'description_2': l.description_2, 'fir_1': l.fir_1, 'fir_2': l.fir_2,}
					for l in user_firms]

	#lfs = formset_factory(NameForm)

	if request.method == 'POST':

		#postedformset = lfs(request.POST)
		#return HttpResponseRedirect('/update_exp/')

		link_formset = LinkFormSet(request.POST)


		if link_formset.is_valid():
			
		# Now save the data for each form in the formset
			new_objj = []

			for link_form in link_formset:
				firma = link_form.cleaned_data.get('firma')
				city_2 = link_form.cleaned_data.get('city_2')
				position = link_form.cleaned_data.get('position')
				description_2 = link_form.cleaned_data.get('description_2')
				fir_1 = link_form.cleaned_data.get('fir_1')
				fir_2 = link_form.cleaned_data.get('fir_2')

				if firma and position:
					new_objj.append(UserFirm(user=user, firma=firma, city_2=city_2, position=position, description_2=description_2, fir_1=fir_1, fir_2=fir_2))

			try:
				with transaction.atomic():
				#Replace the old with the new
					UserFirm.objects.filter(user=user).delete()
					UserFirm.objects.bulk_create(new_objj)
	
					# And notify our users that it worked
					messages.success(request, 'You have updated your profile.')

			except IntegrityError: #If the transaction failed
				messages.error(request, 'There was an error saving your profile.')
				return redirect(reverse('update_exp'))

	else:
		#form = NameForm()
		link_formset = LinkFormSet(initial=link_data)

	context = {

		'link_formset': link_formset,
		#'form':lfs,
	}
			
	return render(request, 'update_exp.html', context)






@login_required
def skill_settings(request):
	user = request.user

	SkillFormSet = formset_factory(SkillForm, formset=BaseSkillFormSet)

	# Get our existing link data for this user.  This is used as initial data.
	user_skills = UserSkill.objects.filter(user=user).order_by('skill_name')


	skill_data = [{'skill_name': l.skill_name,'level': l.level,}
					for l in user_skills]


	if request.method == 'POST':

		skill_formset = SkillFormSet(request.POST)

		if skill_formset.is_valid():
			
		# Now save the data for each form in the formset
			new_obj = []

			for skill_form in skill_formset:
				skill_name = skill_form.cleaned_data.get('skill_name')
				level = skill_form.cleaned_data.get('level')

				if skill_name and level:
					new_obj.append(UserSkill(user=user, skill_name=skill_name, level=level))

			try:
				with transaction.atomic():
				#Replace the old with the new
					UserSkill.objects.filter(user=user).delete()
					UserSkill.objects.bulk_create(new_obj)
	
					# And notify our users that it worked
					messages.success(request, 'You have updated your profile.')

			except IntegrityError: #If the transaction failed
				messages.error(request, 'There was an error saving your profile.')
				return redirect(reverse('skill_settings'))

	else:
		
		skill_formset = SkillFormSet(initial=skill_data)

	context = {

		'skill_formset': skill_formset,
		
	}
			
	return render(request, 'skill_settings.html', context)



@login_required
def groups(request):
	user = request.user
	

	if request.method == "POST" and 'create' in request.POST:  # ukazanie formy do tworzenia grupy oraz wyswietlenie wszystkich dostepnych grup
		cvs = Cv.objects.all()
		cv = Cv.objects.filter(author = request.user)
		form = GroupForm(request.POST)
		if form.is_valid():
			formm = form.save(commit=False)

			for c in cv:
				p = Person.objects.get_or_create(name=request.user, id_person = c.id)[0]

			num_g = Group.objects.filter(name = formm.name).count()

			if num_g >= 1:
				messages.error(request, 'A group with the same name already exists.')
			else:
				g = Group.objects.create(name = formm.name, description = formm.description)
				m = Membership.objects.create(person=p, group=g, leader=True, role="Team Leader")
			


			gr = Group.objects.filter(members__name=request.user) # pokazuje grupy w ktorych Ja uczestnicze (zalogowany user)
			per = Person.objects.all()
			mem = Membership.objects.all()  

			context = {
			'gr': gr,
			'per':per,
			'mem':mem,
			'form': form,
			'cv':cv,
			'cvs':cvs,
		
			}
			return redirect(reverse('groups'), context)



		else:
			for c in cv:
				gr = Group.objects.filter(members__name=request.user, members__id_person=c.id) # pokazuje grupy w ktorych Ja uczestnicze (zalogowany user)
				per = Person.objects.filter(name=request.user, id_person=c.id)
			mem = Membership.objects.filter(group = gr)  

			

			context = {
			'gr': gr,
			'per':per,
			'mem':mem,
			'form': form,
		
			}
			return render(request, 'groups.html', context)






	elif request.method == "POST" and 'leave' in request.POST:

		cvs = Cv.objects.all()
		cv = Cv.objects.filter(author = request.user)
		form = GroupForm()

		gr = Group.objects.filter(members__name=request.user)

		#definiowanie
		p = Person.objects.get(name=request.user)
		gd = Group.objects.get(name=request.POST['leave'])
		#usuwanie
		my = Membership.objects.get(group = gd, person = p)
		if my.leader == False:
			m = Membership.objects.filter(group = gd, person= p, leader = False).delete()  # odejscie z grupy / usuwa jednego uzytkownika - jego poloaczenie - tego zalogowanego


		form = GroupForm()
		context = {
			'gd': gd,
			'cv':cv,
			'cvs':cvs,
			'gr':gr,
			'form': form,
			

			}

		return redirect(reverse('groups'), context)







	elif request.method == "POST" and 'delete' in request.POST:   # usuwanie calej grupy jako leader

		cvs = Cv.objects.all()
		cv = Cv.objects.filter(author = request.user)
		form = GroupForm()
		for c in cv:
			gr = Group.objects.filter(members__name=request.user)

		#definiowanie
		p = Person.objects.filter(name=request.user)
		gd = Group.objects.get(name=request.POST['delete'])
		m = Membership.objects.filter(group = gd, person= p, leader = True)
		#usuwanie
		for z in m:
			if z.leader == False:
				gdd = Group.objects.get(name=request.POST['delete'])
				messages.error(request, 'There was an error saving your profile.')

			else:
				gdd = Group.objects.get(name=request.POST['delete']).delete() 
				
				
				
		

		form = GroupForm()

		context = {
			'gd': gd,
			'cv':cv,
			'cvs':cvs,
			'gr':gr,
			'form': form,
		
			
			}

		return redirect(reverse('groups'), context)




	else:								
		cvs = Cv.objects.all()
		cv = Cv.objects.filter(author = request.user)
		per = Person.objects.all()
		gr = Group.objects.filter(members__name=request.user) # pokazuje grupy w ktorych Ja uczestnicze (zalogowany user)
		perr = Person.objects.filter(name=request.user)
		mem = Membership.objects.filter(group = gr, person = perr)
		mem2 = Membership.objects.filter(group = gr, person = perr)


		form = GroupForm()
		

		context = {
			'gr': gr,
			'per':per,
			'mem':mem,
			'form': form,
			'cvs':cvs,
			'cv':cv,

		}

		return render(request, 'groups.html', context)











@login_required
def choose_group(request, pk):

	if request.method == "POST" and 'group' in request.POST:

		cvs = get_object_or_404(Cv, pk=pk)
		form = MemberForm(request.POST)

		if form.is_valid():
			formm = form.save(commit=False)

			g = Group.objects.get(name=request.POST['group'])
			p = Person.objects.get_or_create(name=cvs.author, id_person = cvs.id)[0]
			m = Membership.objects.get_or_create(person=p, group=g, leader=False, role=formm.role)[0]


			context = {

			'g':g,
			'cvs':cvs,
			'p':p,
			'm':m,
			'form': form,
			}

			return redirect( 'proj.views.cv_detail', pk=cvs.pk )


		else:
		
			mem = Membership.objects.filter(person__name = request.user, leader = True)
			form = MemberForm()

			context = {

			'mem':mem,
			'form':form,
			}

			return render(request, 'choose_group.html', context)




	else:
		cv = Cv.objects.filter(author = request.user)
		cvs = get_object_or_404(Cv, pk=pk)
		
		mem = Membership.objects.filter(person__name = request.user, leader = True)
		form = MemberForm()

		context = {

			'mem':mem,
			'cvs':cvs,
			'cv':cv,
			'form':form,
		}

		return render(request, 'choose_group.html', context)






def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/accounts/invalid')



def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()
	print args
	return render_to_response('register.html', args)


def register_success(request):
	return render_to_response('register_success.html')
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import SendMessageForm, SignUpForm, CvForm, SearchForm
from .forms import LinkForm, BaseLinkFormSet, ProfileForm, NameForm
from .forms import ProfileImageForm, GroupForm
from .models import ProfileImage
from .models import UserLink, UserFirm
from .models import Cv, Person, Group, Membership
from .models import Search
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
		
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")


		subject = 'Friend request from CvFinder' 
		from_emial = settings.EMAIL_HOST_USER
		for c in cv:
			start = 'Message from: '+c.email
			end = c.name+" "+c.surname

		
		

		contact_message = "%s: \n\n%s \n\ngreetings, %s" %(start, form_message, end)


		send_mail(subject, contact_message, from_emial, to_email, fail_silently=False)


	con = {
		"form": form,
		"cv": cv,
		"cvs": cvs,
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


	# listed_users = User.objects.all()

	con = {
			"cv": cv,
			# "listed_users": listed_users,
			"user_links": user_links,
			"user_firms": user_firms,
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
	userr = request.user

	LinkFormSet = formset_factory(LinkForm, formset=BaseLinkFormSet)

	# Get our existing link data for this user.  This is used as initial data.
	user_firms = UserFirm.objects.filter(userr=userr).order_by('firma')


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
					new_objj.append(UserFirm(userr=userr, firma=firma, city_2=city_2, position=position, description_2=description_2, fir_1=fir_1, fir_2=fir_2))

			try:
				with transaction.atomic():
				#Replace the old with the new
					UserFirm.objects.filter(userr=userr).delete()
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
def groups(request):

	if request.method == "POST":
		form = GroupForm(request.POST)
		if form.is_valid():

			grupa = Group.objects.create(name="grupa")
			per = Person.objects.create(name=request.user)
			m1 = Membership(person=per, group=grupa, date_joined=(1999, 8, 8), invite_reason="Needed programmer.")
			form.save()


			return render(request, 'groups.html', {'form':form})

	else:
		form = GroupForm()

	return render(request, 'groups.html', {'form': form})

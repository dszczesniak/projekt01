import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import ContactForm, SignUpForm, CvForm, SearchForm
from .forms import LinkForm, BaseLinkFormSet, ProfileForm, NameForm
from .forms import ProfileImageForm
from .models import ProfileImage
from .models import UserLink, UserFirm
from .models import Cv
from .models import Search
from django.views.generic import View, FormView, DetailView, ListView


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
					cv.save()
					return redirect('proj.views.cv_detail', pk=cv.pk)
			else:
				form = CvForm()
			return render(request, 'new_cv.html', {'form': form})

	else:
		return render(request, "home.html", )





def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")


		subject = 'Site_contact_form' 
		from_emial = settings.EMAIL_HOST_USER
		to_email = [from_emial, 'youtheremail@gmail.com']
		contact_message = "%s: %s via %s" %(full_name, message, email)


		send_mail(subject, contact_message, from_emial, to_email, fail_silently=True)


	con = {
		"form": form,
		"title": title,
	}

	return render(request, "forms.html", con)





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






def cv_detail(request, pk):
	cv = get_object_or_404(Cv, pk=pk)
	return render(request, 'cv_detail.html', {'cv': cv})







@login_required
def base_cv(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			search_text = form.cleaned_data.get("search_text")
			sort = form.cleaned_data.get("sort")

			if sort == "N":
				cvs = Cv.objects.filter(name = search_text)
			elif sort == "S":
				cvs = Cv.objects.filter(surname = search_text)
			elif sort == "E":
				cvs = Cv.objects.filter(email = search_text)
			else:
				pass

			con = {
			"form": form,
			"cvs": cvs,
			}

			return render(request, 'base_cv.html', con)

	else:
		form = SearchForm()
		cvs = Cv.objects.filter()

		con = {
			"cvs": cvs,
			"form": form,
			}

		return render(request, 'base_cv.html', con)

	return render(request, 'base_cv.html', {'form': form})








@login_required
def profile_settings(request):
	user = request.user

	LinkFormSet = formset_factory(LinkForm, formset=BaseLinkFormSet)

	# Get our existing link data for this user.  This is used as initial data.
	user_links = UserLink.objects.filter(user=user)


	link_data = [{'university': l.university, 'city_1': l.city_1, 'grade': l.grade, 'field': l.field, 'description_1': l.description_1,}
						for l in user_links]

	#lfs = formset_factory(NameForm)

	if request.method == 'POST':

		#postedformset = lfs(request.POST)
		#return HttpResponseRedirect('/edit_profile/')

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


				if university and field:
					new_obj.append(UserLink(user=user, university=university, city_1=city_1, grade=grade, field=field, description_1 = description_1))

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
		#form = NameForm()
		link_formset = LinkFormSet(initial=link_data)

	context = {

		'link_formset': link_formset,
		#'form':lfs,
	}
			
	return render(request, 'edit_profile.html', context)









@login_required
def update_exp(request):
	userr = request.user

	LinkFormSet = formset_factory(LinkForm, formset=BaseLinkFormSet)

	# Get our existing link data for this user.  This is used as initial data.
	user_firms = UserFirm.objects.filter(userr=userr).order_by('firma')


	link_data = [{'firma': l.firma, 'city_2': l.city_2, 'position': l.position, 'description_2': l.description_2}
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

				if firma and position:
					new_objj.append(UserFirm(userr=userr, firma=firma, city_2=city_2, position=position, description_2=description_2))

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




class UploadDocumentationFilesView(View):
    template_name = "templates/home"
    form_class = ProfileImageForm
    
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)       
    def post(self, request, *args, **kwargs):
        # Check if there is possiblity for removing files
        error = False
        f = request.FILES.get(u'files[]')

        temp_path = os.path.join(settings.MEDIA_ROOT, DOC_TEMP_FOLDER)
        
        if f.size > MAX_DOC_SIZE:
            error = "maxFileSize"
        response_data = {
            'name': f.name,
            'size': f.size,
            'type': f.content_type
            }
        if error:
            response_data["error"] = error
            return JsonResponse(response_data)
        
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)
        
        name = unicode(uuid.uuid4())
        extension = f.name.split(".")[-1]
        
        filename_file = "{0}.{1}".format(name, extension)
        
        filename = os.path.join(temp_path, filename_file)
        
        destination = open(filename, "wb+")
        
        for chunk in f.chunks():
            destination.write(chunk)
            
        destination.close()
        
        response_data['name'] = filename_file
        response_type = "application/json"
        
        if "text/html" in request.META["HTTP_ACCEPT"]:
            response_type = "text/html"
            
        response_data['type'] = response_type
        return JsonResponse(response_data)


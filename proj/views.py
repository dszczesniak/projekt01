from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import ContactForm, SignUpForm, CvForm, SearchForm
from .models import Cv
from .models import Search


# Create your views here.
def home(request):
	title = "Log in:"
	form = SignUpForm(request.POST or None)
	con = {
		"template_title": title,
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit = False)

		full_name = form.cleaned_data.get("full_name")
		instance.full_name = full_name
		instance.save()
		con = {
			"template_title": "Thank you"
		}


	return render(request, "home.html", con)




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
        form = CvForm(request.POST)
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
			form = CvForm(request.POST, instance=cv)
			if form.is_valid():
				cv = form.save(commit=False)
				cv.author = request.user
				cv.save()
				return redirect('proj.views.myprofile')
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

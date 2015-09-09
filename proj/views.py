from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm

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
		contact_message = "%s: %s via %s" %(
			full_name,
			message,
			email)


		send_mail(
	 		subject,
	 		contact_message,
	 		from_emial,
   	 		to_email,
     		fail_silently=True)


	con = {
		"form": form,
		"title": title,
	}

	return render(request, "forms.html", con)
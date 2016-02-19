from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp
from .models import Cv, UserLink, UserFirm

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	#class Meta:
	#	model = SignUp


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Cv)
admin.site.register(UserLink)
admin.site.register(UserFirm)
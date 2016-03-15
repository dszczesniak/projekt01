from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp
from .models import Cv, UserLink, UserFirm, Group, Person, Membership

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	#class Meta:
	#	model = SignUp


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Cv)
admin.site.register(UserLink)
admin.site.register(UserFirm)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Person)
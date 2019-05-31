from django import forms

from eventapp.models import UserProfileInfo

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
        
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')



class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	class Meta:
		model = User
        fields = ('username', 'email', 'password1', 'password2', )        
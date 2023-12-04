from django import forms
from .models import UserProfile, Major

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    buff_id = forms.CharField(max_length=7)
    major = forms.ModelChoiceField(queryset=Major.objects.all())

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'buff_id', 'major']

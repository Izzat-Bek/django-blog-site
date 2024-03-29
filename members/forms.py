from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control' 
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class UserCreateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('bio', 'image', 'url_website', 'url_instagram', 'url_telegram', 'url_github')
        
        
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'url_website': forms.TextInput(attrs={'class': 'form-control'}),
            'url_instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'url_telegram': forms.TextInput(attrs={'class': 'form-control'}),
            'url_github': forms.TextInput(attrs={'class': 'form-control'}),
        } 
               
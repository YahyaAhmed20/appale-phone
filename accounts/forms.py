from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2'] 
        
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
        # 'first_name','last_name',
        
class ProfileForm(forms.ModelForm):
    # تحقق من أن الإدخال أرقام فقط
    phone_regex = RegexValidator(
        regex=r'^\d{10,15}$',  # أرقام فقط، من 10 إلى 15 رقم
        message="The phone number must contain only numbers (10-15 digits)."
    )

    phone_number = forms.CharField(
        validators=[phone_regex],
        widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
        label="Valid WhatsApp Phone Number"
    )

    class Meta:
        model = Profile
        fields = ['phone_number', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
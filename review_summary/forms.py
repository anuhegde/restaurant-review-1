from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Repeat Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}), required=False)

from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
       
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password does not match")
        return confirm_password
    
    def save(self, commit=True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if not username or not password:
            raise forms.ValidationError("Qiymatlar to'dirilishi shart")
        
        return self.cleaned_data
    

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "photo"]
       
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     # if User.objects.filter(email=email).count() > 1:
    #     #     raise forms.ValidationError("Email already exists")
    #     return email
    
    def save(self, commit=True):
        user = super().save(commit)
       
        
        return user



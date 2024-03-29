# accounts.forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField


from .models import User



class LoginForm(forms.Form):
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-input-field','placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-input-field','placeholder':'Password'}))

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_name','email',)
 
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        username = self.cleaned_data.get('user_name')
           
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-input-field','placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-input-field','placeholder':'Confirm Password'}))
    user_name=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-input-field','placeholder':'Your Username'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-input-field','placeholder':'Your Email'}))

    class Meta:
        model = User
        fields = ('user_name','email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("User with that email already exists ")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        
       
        if commit:
            user.save()
            
        return user

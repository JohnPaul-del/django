from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from authapp.models import ShopUser
import hashlib
from random import random


class ShopUserLogin(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLogin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegistration(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'password1', 'password2', 'age')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegistration, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        user_age = self.cleaned_data['age']
        if user_age < 18:
            raise forms.ValidationError("18+ only")
        return user_age

    def save(self):
        user = super(ShopUserRegistration, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class ShopUserEdit(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(ShopUserEdit, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        user_age = self.cleaned_data['age']
        if user_age < 18:
            raise forms.ValidationError("18+ only")
        return user_age

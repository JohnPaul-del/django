from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from authapp.models import ShopUser


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
        fields = ('username', 'password1', 'password2', 'age')

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

    def check_password(self):
        password_1 = self.cleaned_data['password1']
        password_2 = self.cleaned_data['password2']
        if password_1 != password_2:
            raise forms.ValidationError("Password must match")


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

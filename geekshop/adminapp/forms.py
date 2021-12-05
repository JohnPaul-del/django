from authapp.models import ShopUser
from authapp.forms import ShopUserEdit
from django import forms

from mainapp.models import Product, ProductCategory


class ShopUserAdminEditForm(ShopUserEdit):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(ProductCategoryEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import ShopUserAdminEditForm, ProductEditForm, ProductCategoryEditForm
from authapp.forms import ShopUserRegistration
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        return context

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegistration
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')


class UserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin_staff:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


def categories(request):
    title = 'Category Admin Panel'
    categories_list = ProductCategory.objects.all()
    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')
    fields = '__all__'

# def category_create(request):
#     title = 'Create Category'
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         category_form = ProductCategoryEditForm()
#     context = {
#         'title': title,
#         'new_category': category_form,
#     }
#     return render(request, 'adminapp/category_update.html', context)


def category_update(request, pk):
    title = 'Edit category'
    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)
    context = {
        'title': title,
        'edit_form': edit_form,
    }
    return render(request, 'adminapp/category_update.html', context)


def category_delete(request, pk):
    title = 'Delete Category'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin_staff:categories'))
    context = {
        'title': title,
        'category_to_del': category
    }
    return render(request, 'adminapp/category_delete.html', context)


def products(request, pk):
    title = 'Product Admin Panel'
    category = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category__pk=pk).order_by('name')
    context = {
        'title': title,
        'category': category,
        'objects': product_list,
    }
    return render(request, 'adminapp/products.html', context)


def product_create(request, pk):
    title = 'Create Product'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})
    context = {
        'title': title,
        'product_form': product_form,
        'category': category,
    }
    return render(request, 'adminapp/product_update.html', context)


def product_read(request, pk):
    title = 'Product info'
    product = get_object_or_404(Product, pk=pk)
    context = {
        'title': title,
        'object': product,
    }
    return render(request, 'adminapp/product_read.html', context)


def product_update(request, pk):
    title = 'Edit Product'
    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return render(request, 'admin_staff:product_update', args=[edit_product.pk])
    else:
        edit_form = ProductEditForm(instance=edit_product)
    context = {
        'title': title,
        'product_form': edit_form,
        'category': edit_product.category,
    }
    return render(request, 'adminapp/product_update.html', context)


def product_delete(request, pk):
    title = 'Delete Product'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
    context = {
        'title': title,
        'product_to_del': product,
    }
    return render(request, 'adminapp/product_delete.html', context)

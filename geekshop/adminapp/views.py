from django.shortcuts import render, get_object_or_404, reverse
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import ShopUserAdminEditForm, ProductEditForm, ProductCategoryEditForm
from authapp.forms import ShopUserRegistration
from django.http import HttpResponseRedirect


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'User Admin Panel'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    context = {
        'title': title,
        'objects': users_list,
    }
    return render(request, 'adminapp/users.html', context)


def user_create(request):
    title = "User Create"
    if request.method == 'POST':
        user_form = ShopUserRegistration(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        user_form = ShopUserRegistration()

    context = {
        'title': title,
        'user_form': user_form,
    }
    return render(request, 'adminapp/user_update.html', context)


def user_update(request, pk):
    title = 'Update User Profile'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)
    context = {
        'title': title,
        'user_form': edit_form,
    }
    return render(request, 'adminapp/user_update.html', context)


def user_delete(request, pk):
    title = 'Delete user'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin_staff:users'))
    context = {
        'title': title,
        'user_to_del': user,
    }
    return render(request, 'adminapp/user_delete.html', context)


def categories(request):
    title = 'Category Admin Panel'
    categories_list = ProductCategory.objects.all()
    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    title = 'Create Category'
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin_staff:categories'))
    else:
        category_form = ProductCategoryEditForm()
    context = {
        'title': title,
        'new_category': category_form,
    }
    return render(request, 'adminapp/category_update.html', context)


def category_update(request, pk):
    title = 'Edit category'
    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:categories'))
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
    product_list = Product.objects.filter(category__pk=pk).orderby('name')
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
            return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
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
    }
    return render(request, 'adminapp/product_update.html', context)


def product_delete(request, pk):
    title = 'Delete Product'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin_staff:product_delete', args=[product.category.pk]))
    context = {
        'title': title,
        'product_to_del': product,
    }
    return render(request, 'adminapp/product_delete.html', context)

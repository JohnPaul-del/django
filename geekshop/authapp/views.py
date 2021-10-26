from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from authapp.forms import ShopUserRegistration, ShopUserEdit, ShopUserLogin


def login(request):
    title = 'Login'
    login_form = ShopUserLogin(data=request.POST)
    next = request.GET['next'] if 'next' is request.GET.keys() else ''
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if ('next') in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main'))
    context = {
        'title': title,
        'login_form': login_form,
        'next': next,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    title = 'registration'
    if request.method == 'POST':
        register_form = ShopUserRegistration(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegistration()
    context = {
        'title': title,
        'register_form': register_form,
    }
    return render(request, 'authapp/register.html', context)


def edit(request):
    title = 'edit'
    if request.method == 'POST':
        edit_form = ShopUserEdit(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEdit(instance=request.user)
    context = {
        'title': title,
        'edit_form': edit_form
    }
    return render(request, 'authapp/edit.html', context)

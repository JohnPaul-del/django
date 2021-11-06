from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from authapp.forms import ShopUserRegistration, ShopUserEdit, ShopUserLogin, ShopUserProfileEditForm
from geekshop import settings
from django.core.mail import send_mail
from authapp.models import ShopUser
from django.db import transaction


def login(request):
    title = 'Login'
    login_form = ShopUserLogin(data=request.POST)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
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
            user = register_form.save()
            if send_verification(user):
                messages.add_message(request, messages.SUCCESS, "Link was sent by email. "
                                                                "Confirm account using the link from the email")
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegistration()
    context = {
        'title': title,
        'register_form': register_form,
    }
    return render(request, 'authapp/register.html', context)


@transaction.atomic
def edit(request):
    title = 'edit'
    if request.method == 'POST':
        edit_form = ShopUserEdit(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEdit(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)
    context = {
        'title': title,
        'edit_form': edit_form,
        'profile_form': profile_form,
    }
    return render(request, 'authapp/edit.html', context)


def send_verification(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    title = 'Verification'
    message = f'Confirm account {user.username}' \
              f'Follow {settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'authapp/verification.html')
        else:
            return render(request, 'authapp/verification.html')
    except Exception as e:
        return HttpResponseRedirect(reverse('main'))

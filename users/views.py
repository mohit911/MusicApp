"""Views file, for all business logic."""
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from users.models import UserProfileInfo


def register(request):
    """Function to register users."""
    context = {}
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password2 == password1:
                User.objects.create_user(
                    password=password1,
                    username=username,
                    email=email)
                print("user created")

                context = {'success': True, 'message': 'Successfully saved. Please Login to continue'}
                return render(request, "register.html", context)

        except:
            context = {'success': False, 'message': 'NOT saved! Please try again later!'}
            return render(request, "register.html", context)

    return render(request, "register.html", context)


def login(request):
    """Login method for registered users."""
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        user = auth.authenticate(username=u, password=p)
        context = {}
        if request.user.is_authenticated():
            context = {'login': 'already LoggedIn'}
            context['username'] = request.user.username
            return render(request, "login.html", context)
        else:
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    context['login'] = 'login successfull'
                    context['username'] = request.user.username
                    return HttpResponseRedirect('/')
                else:
                    context = {}
                    context['login'] = 'Account deactivated'
                    return render(request, "login.html", context)

            else:
                context = {}
                context['login'] = 'Invalid Login'
                return render(request, "login.html", context)

    else:
        context = {}

        template = "login.html"
        return render(request, template, context)


@login_required(login_url='/users/login/')
def logout(request):
    """Logout method for LoggedIn Users."""
    if request.user.is_authenticated():
        auth.logout(request)
        context = {}
        context['login'] = 'Logout sucessfull'

        return login(request)
    else:
        pass


@login_required(login_url='/users/login/')
def account(request):
    """User Information store."""
    context = {}
    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            profile_picture = request.FILES.get('profile_picture')
            gender = request.POST.get('sex')

            user_info = request.user.username
            user_info = User.objects.get(username=user_info)

            try:
                user_info_collect = UserProfileInfo.objects.get(user=user_info)
                if first_name != "":
                    user_info_collect.first_name = first_name
                if last_name != "":
                    user_info_collect.last_name = last_name
                if gender != "":
                    user_info_collect.gender = gender
                if profile_picture:
                    user_info_collect.profile_picture = profile_picture

            except UserProfileInfo.DoesNotExist:
                user_info_collect = UserProfileInfo(
                    user=user_info,
                    first_name=first_name,
                    last_name=last_name,
                    profile_picture=profile_picture,
                    gender=gender)

            user_info_collect.save()
            context = {'success': True, 'message': 'Successfully saved'}
            return HttpResponseRedirect(reverse('account'))

        except:
            context = {'success': False, 'message': 'Saving failed'}

    else:
        try:
            user_info = request.user.username
            user_info = User.objects.get(username=user_info)
            user_info = UserProfileInfo.objects.get(user=user_info)
            context = {'account': user_info, 'request': request}
        except:
            print('User Info Not Found')
        return render(request, 'account.html', context)

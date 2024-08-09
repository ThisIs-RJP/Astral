from django.shortcuts import *
from django.http import HttpResponse
from templates.forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import *
from .config import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'create.html', {'form': form})
    return render(request, 'create.html', {'form': form}) 
    
class UserLoginView(LoginView):
    template_name='login.html'

def log_out(request):
    logout(request)
    return redirect("/")

def account(request):
    user = request.user

    # Check if the UserInfo and UserIcon instances exist
    user_exists = UserInfo.objects.filter(originalName=user.username).exists()

    if not user_exists:
        # Create UserInfo and UserIcon if they don't exist
        user_info = UserInfo.objects.create(
            username=user.username,
            fname=user.first_name,
            lname=user.last_name,
            email=user.email,
            originalName=user.username
        )
        user_icon = UserIcon.objects.create(
            originalName=user.username,
            pfp='icons/default.png'  # Use a default image if desired
        )
    else:
        user_info = UserInfo.objects.get(originalName=user.username)
        user_icon = UserIcon.objects.get(originalName=user.username)

    if request.method == 'POST':
        # Use POST data and FILES for the forms
        user_info_form = UserInfoForm(request.POST, instance=user_info)
        user_icon_form = UserIconForm(request.POST, request.FILES, instance=user_icon)

        # Validate forms
        if user_info_form.is_valid() and user_icon_form.is_valid():
            user_info_form.save()
            user_icon_form.save()
            return redirect('/account')
    else:
        user_info_form = UserInfoForm(instance=user_info)
        user_icon_form = UserIconForm(instance=user_icon)

    return render(request, 'account.html', {
        "username": user_info.username,
        "form": user_info_form,
        "icon": user_icon.pfp.url if user_icon.pfp else None,
        "iconForm": user_icon_form
    })

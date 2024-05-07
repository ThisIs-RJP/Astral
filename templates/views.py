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
    otherForm = UserInfoForm()

    userExists = UserInfo.objects.all().filter(originalName=request.user)

    if not userExists:
        details = otherForm.save(commit=False)
        details.username = request.user 
        details.originalName = request.user
        details.email = request.user.email
        details.save()

    if otherForm.is_valid():
        otherForm.save()

    userUser = UserInfo.objects.get(originalName=request.user)

    if request.method == 'POST':
        otherForm = UserInfoForm(request.POST, instance=userUser)
        if otherForm.is_valid():
            otherForm.save()
            return redirect('/account')
    else:
        otherForm = UserInfoForm(request.POST)

        return render(request, 'account.html', {"username": userUser.username, 'form': otherForm})
    return render(request, 'account.html', {"username": userUser.username, 'form': otherForm})
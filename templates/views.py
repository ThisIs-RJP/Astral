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

    returnDictionary = {}
    userInformation = []
    tempList = []
    i = 0

    userInformation.append(user)
    userInformation.append(user.email)

    # print("User information")
    # print(userInformation)
    # print()

    for k, v in PROFILE_SETTINGS.items():
        tempList.append(v)
        tempList.append(userInformation[i])
        returnDictionary[k] = tempList
        i = i + 1
        tempList = []

    print(returnDictionary)

    form = UserInfo(request.POST)

    return render(
        request,
        'account.html',
        {
            "content" : returnDictionary,
            "form" : form
        }
        )
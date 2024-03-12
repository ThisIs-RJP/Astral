from django.shortcuts import *
from django.http import HttpResponse
from templates.forms import *

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
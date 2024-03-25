from django.urls import path
from . import views
from .forms import *

urlpatterns = [
   path('', views.index, name="index"),
   path('signup', views.signup, name="signup"),
   path('login', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
   path('logout/', views.log_out, name="logout"),
   path('account', views.account, name="account"),
]
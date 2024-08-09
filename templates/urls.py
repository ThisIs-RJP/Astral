from django.urls import path
from . import views
from .forms import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.index, name="index"),
   path('signup', views.signup, name="signup"),
   path('login', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
   path('logout/', views.log_out, name="logout"),
   path('account', views.account, name="account"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
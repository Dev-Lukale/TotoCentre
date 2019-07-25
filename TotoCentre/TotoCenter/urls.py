"""TotoCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from accounts.views import RegisterView,LoginView
from accounts import views as accounts_views
from django.conf.urls import include,url
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    url('register/',RegisterView.as_view(),name='register'),
    url('login/',LoginView.as_view(),name='login'),
    path('home/', accounts_views.home,name='home'),
    path('contact/', accounts_views.contact,name='contact'),
    path('', include('posts.urls')),
    path('content/', include('content.urls')),
    path('profile/', accounts_views.View_profile,name='View_Profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
   ]
if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


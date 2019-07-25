from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        url('about/',views.about,name='about'),
        url('getting pregnant/',views.getting_pregnant,name='getting_pregnant'),
        url('pregnancy/',views.pregnancy,name='pregnancy'),
        url('baby/',views.baby,name='baby'),
        url('health/',views.health,name='health'),


    ]
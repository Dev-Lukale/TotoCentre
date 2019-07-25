from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from django.views.generic import CreateView,FormView
from .forms import LoginForm,RegisterForm
from django.utils.http import is_safe_url
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.contrib.messages.views import SuccessMessageMixin

class LoginView(FormView):
	form_class=LoginForm
	template_name='accounts/login.html'
	success_url='/home/'

	def form_valid(self,form):
		request=self.request
		next_=request.GET.get('next')
		next_post=request.POST.get('next')
		redirect_path=next_ or next_post or None
		email=form.cleaned_data.get("email")
		password=form.cleaned_data.get("password")
		user=authenticate(request,username=email,password=password)
		if user is not None:
			login(request,user)
			try:
				del request.session['  ']
			except:
				pass
			if is_safe_url(redirect_path,request.get_host()):
				return redirect(redirect_path)
			else:
				return redirect("home")
		return super(LoginView,self).form_invalid(form)


class RegisterView(SuccessMessageMixin,CreateView):
	form_class=RegisterForm
	template_name='accounts/register.html'
	success_url='/login/'
	sucess_message="success registration"

	

def home(request):
    return render(request, 'accounts/home.html')


@login_required
def contact(request):
    return render(request, 'accounts/contact.html')


@login_required
def View_profile(request):
	return render(request,'accounts/Profile.html')
	
	
	



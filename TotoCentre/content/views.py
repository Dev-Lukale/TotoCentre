from django.shortcuts import render

# Create your views here.
def about(request):
	return render(request,'content/about.html')
def getting_pregnant(request):
	return render(request,'content/getting_pregnant/getting_pregnant.html')
def pregnancy(request):
	return render(request,'content/pregnancy/pregnancy.html')
def baby(request):
	return render(request,'content/baby/baby.html')
def health(request):
	return render(request,'content/health/health.html')

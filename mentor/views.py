from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from forms import RegistrationForm




def index(request):
    return HttpResponse("Hello, world. You're at the Mentor index.")



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/success")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {
        'form': form,
	})

def lostpass(request):
	return HttpResponse("lostpass.")

def success(request):
	return HttpResponse("Successful registration.")

	

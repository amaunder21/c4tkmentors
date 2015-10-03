from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return HttpResponse("Hello, world. You're at the Mentor index.")



def register(request):
	return HttpResponse("register.")
	#
    #if request.method == 'POST':
    #    form = UserCreationForm(request.POST)
    #    if form.is_valid():
    #        new_user = form.save()
    #        return HttpResponseRedirect("/books/")
    #else:
    #    form = UserCreationForm()
    #return render(request, "registration/register.html", {
    #    'form': form,
    #})

# Create your views here.

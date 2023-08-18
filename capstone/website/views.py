from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Endorser
from .forms import EndorserForm

def user_login(request):
    return render(request, 'login.html')

def authenticatation(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('website:user_login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('website:homepage')
        )

def homepage(request):
    return render (request, "homepage.html")

def area_serviced(request):
    return render (request, "area_serviced.html")

def biography(request):
    return render (request, "biography.html")

def endorsements(request):
    latest_endorser_list = Endorser.objects.all()
    context = {'latest_endorser_list': latest_endorser_list}
    return render (request, "endorsements.html", context)

def add_endorser(request):
    form = EndorserForm

    if request.method == "POST":
        form = EndorserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('website:homepage'))
        
    context= {'form': form}
    return render(request, 'add_endorser.html', context)
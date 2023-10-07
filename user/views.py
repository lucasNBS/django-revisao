from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm

# Create your views here.
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("reservas")
    else:
        form = LoginForm()
    
    context = { "form": form }
    return render(request, "user/login.html", context)

def logout_user(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.is_staff = True
            user.save()
            return redirect("login")
    else:
        form = UserForm()

    context = { "form": form }
    return render(request, "user/register.html", context)
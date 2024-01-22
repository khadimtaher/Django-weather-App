from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import urllib.request
import json


@login_required(login_url="login")
def Home(request):
    if request.method == "POST":
        key = "43702884440918ec4b388f04fb8dd39d"
        city = request.POST.get("city", "")

        if not city:
            return render(request, "home.html")

        try:
            source = urllib.request.urlopen(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
            ).read()
            data = json.loads(source)

            # Check if the API response contains valid data for the city
            if "main" in data:
                return render(
                    request, "home.html", {"data": data["main"], "city": city}
                )
            else:
                error_message = f"City '{city}' not found. Please enter a valid city."
                return render(
                    request, "home.html", {"error_message": error_message, "city": city}
                )

        except Exception as e:
            error_message = f"Please Enter The Valid Name:😑 {str(e)}"
            return render(
                request, "home.html", {"error_message": error_message, "city": city}
            )
    else:
        return render(request, "home.html")


def Signup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        if pass1 != pass2:
            return HttpResponse("Please Confirm your password")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("login")

    return render(request, "signup.html")


def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass1")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Username or Password is Incorrect.")

    return render(request, "login.html")


def Logout(request):
    logout(request)
    return redirect("login")

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .forms import RegistrationForm

# Create your views here.
class LoginView(View):
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return HttpResponseRedirect("/admin")
        if user is not None and not user.is_staff:
            login(request, user)
            return HttpResponseRedirect("/")
        return render(request, "account/login.html")

    def get(self, request):
        return render(request, "account/login.html")


class CreateUserAccountView(View):
    def post(self, request):
        User = get_user_model()
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            username = registration_form.cleaned_data["username"]
            password = registration_form.cleaned_data["password"]
            first_name = registration_form.cleaned_data["first_name"]
            last_name = registration_form.cleaned_data["last_name"]
            email = registration_form.cleaned_data["email"]
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.password2 = password
            user.save()
            return redirect("logs-list")
        else:
            registration_form = RegistrationForm()
            
    def get(self, request):
        registration_form = RegistrationForm()
        return render(request, "account/registration.html", {"registration_form": registration_form,})
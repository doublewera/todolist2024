from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):
    user = None
    if request.user.is_authenticated:
         user = request.user
    context = {
        'user': user
    }  
    return render(
        request,                # Запрос
	    'mainpage/index.html',  # путь к шаблону
        context                 # подстановки
    )

from .forms import UserRegistrationForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'mainpage/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        'mainpage/register.html',
        {
            'user_form': user_form
        })


from django.contrib import auth
def loginme(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = auth.authenticate(
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                return redirect('/')
            else:
                return redirect('login')
    else:
        user_form = UserLoginForm()
    return render(
        request,
        'mainpage/user_login.html',
        {
            'user_form': user_form
        })

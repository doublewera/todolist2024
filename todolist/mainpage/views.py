from django.shortcuts import render

def index(request):
    context = {}  
    return render(
        request,                # Запрос
	    'mainpage/index.html',  # путь к шаблону
        context                 # подстановки
    )

from .forms import UserRegistrationForm  #, LoginForm

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
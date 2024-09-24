from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        labels = {
            "username": "Будущий логин",
            "first_name": "Как вас зовут:",
            "email": "Электронная почта"
        }
        help_texts = {
            "username": "Обязательное поле. Буквы, цифры, символ подчеркивания."
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
    
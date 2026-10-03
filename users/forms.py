from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
)

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "auth-form__input"
        })
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Email",
            "class": "auth-form__input",
        })
    )

    password1 = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "auth-form__input",
        })
    )

    password2 = forms.CharField(
        label="Confirm Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirm Password",
            "class": "auth-form__input",
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs.setdefault("class", "auth-form__input")

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "auth-form__input",
            "placeholder": "Username",
        })

        self.fields["password"].widget.attrs.update({
            "class": "auth-form__input",
            "placeholder": "Password",
        })

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["old_password"].widget.attrs.update({
            "class": "auth-form__input",
            "placeholder": "Current Password",
        })

        self.fields["new_password1"].widget.attrs.update({
            "class": "auth-form__input",
            "placeholder": "New Password",
        })

        self.fields["new_password2"].widget.attrs.update({
            "class": "auth-form__input",
            "placeholder": "Confirm New Password",
        })
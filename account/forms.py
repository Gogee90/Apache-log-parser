from django.forms import (
    CharField,
    EmailField,
    Form,
    PasswordInput,
)


class RegistrationForm(Form):
    username = CharField(label="Username", max_length=100)
    password = CharField(label="Password", widget=PasswordInput)
    password2 = CharField(label="Password again", widget=PasswordInput)
    email = EmailField(max_length=50)
    first_name = CharField(label="First name", max_length=30)
    last_name = CharField(label="Last name", max_length=50)
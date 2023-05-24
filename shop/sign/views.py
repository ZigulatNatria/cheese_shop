from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = '/auth/'

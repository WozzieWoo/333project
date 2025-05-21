from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # O el nombre correcto del archivo HTML
def catalog(request):
    return render(request, 'catalog.html')

def comunity(request):
    return render(request, 'comunity.html')

def cart(request):
    return render(request, 'cart.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'registro.html')

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class RegistroView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

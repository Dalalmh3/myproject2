from django.shortcuts import render,redirect
from .models import Product
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .forms import ProductForm
# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout as django_logout




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Add_Product')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })



def index(request):
    context= {
        "all_products": Product.objects.all(),
        "isLogged": True,
    }

    if request.session.is_empty():
        context['isLogged'] = False
    return render(request, "MarketPlaceApp/index.html", context ) 



 
@login_required()
def Add_Product(request):
    if request.session.is_empty():
        request.session['user'] = request.user
    if request.method == "POST":
        form = ProductForm (request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect("/")

    form = ProductForm()
    return render(request, 'MarketPlaceApp/add_product.html',{'form':form})

def logout(request):
    request.session.clear()
    django_logout(request)
    return redirect('/')
  


def login(request):
    form = UserCreationForm()
    return redirect('/accounts/login')


   

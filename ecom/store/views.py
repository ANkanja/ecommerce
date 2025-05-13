from django.shortcuts import redirect, render
from . models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from . forms import SignUpForm

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})


def index(request):
    return render(request, 'index.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})


def official(request):
    my_awesome_official_collection = Product.objects.filter(category__name='Official')
    return render(request, 'official.html', {'products': my_awesome_official_collection})

def sports(request):
    my_awesome_sports_collection = Product.objects.filter(category__name='Sports')
    return render(request, 'sports.html', {'products': my_awesome_sports_collection})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if the user exists
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
        
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out. Thanks for stopping by!")
    return redirect('index')
    

def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticate the user(Log in the user)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('index')
        else:
            messages.error(request, "Registration failed. Please try again.")
            return redirect('register') 
    else:
        return render(request, 'register.html', {'form': form})
    




















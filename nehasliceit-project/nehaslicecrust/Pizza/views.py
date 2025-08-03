from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Pizza , OrderPizza
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


# Authentication Functions
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Password Doesn't match")
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# Main Functions
def index(request):
    note = "Welcome To Neha's SliceCrust"
    return HttpResponse(note)

def home(request):
    return render(request, 'pizza/home.html')

def about(request):
    return render(request, 'pizza/about.html')

def contact(request):
    return render(request, 'pizza/contact.html')

def pizza_menu(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza/menu.html', {'pizzas':pizzas})

@login_required
def order_pizza(request, pk):
    pizza = Pizza.objects.get(id=pk)
    pizza_tax = 200
    if request.method == 'POST':
        size = request.POST['size']
        quantity = int(request.POST['quantity'])

        if size == 'small':
           price = pizza.small_price

        elif size == 'medium':
            price = pizza.medium_price

        else:
            price = pizza.large_price

        total_price = (price * quantity) + pizza_tax

        order = OrderPizza.objects.create(
                user = request.user,
                size = size,
                pizza = pizza,
                quantity = quantity,
                total_price = total_price
        )
        # Message send when user click OK button
        try:
            subject = 'Pizza Order Confirmation'
            message = f"""
                    Dear {request.user.username},
                    
                    Thank you for your order! 
                    Here are your order details:
                    
                    Order ID : #{order.id}
                    Pizza : {pizza.name}
                    Size : {size.title()}
                    Quantity : {quantity}
                    Total Price : ${total_price}
                    
                    Your delicious pizza is being prepared and will be delivered soon! Thank you for choosing our pizza service!
                    
                    Best regards,
                    Neha's SliceCrust
                    """

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False,
            )
            messages.success(request, f'Order Placed Successfully, Confirmation email sent to {request.user.email}')
        except Exception as e:
            messages.success(request, 'Order Placed Successfully')
            messages.warning(request, 'Unable to send confirmation email, Please check your email setting')

        return redirect('/')

    return render(request, 'pizza/order_pizza.html', {'pizza':pizza})
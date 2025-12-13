from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import DeliveryForm
from .forms import UserForm
from .models import Profile

# Create your views here.
from django.http import HttpResponse
import random
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.db import models
from django.contrib.auth.decorators import login_required
# технічно представлення - це функції, які приймають
# запит (request) та формують відповідь (response)
def hello(request) :
    return HttpResponse("Hello, world!")


def home(request):
    return render(request, "home.html")


def about(request):
    return HttpResponse("<h1>Сторінка Про нас</h1>")

def privacy(request):
    return HttpResponse("<h1>Політика конфіденційності</h1>")


def lottery(request):
    number = random.randint(1, 100)
    load_time = timezone.now()

    return render(request, 'lottery.html', {
        'number': number,
        'load_time': load_time
    })

def statics_page(request):
    return render(request, "statics.html")

@csrf_exempt
def http_help(request):
    post_data = None

    if request.method == "POST":
        post_data = request.POST

    elif request.method in ["PUT", "PATCH"]:
        body = request.body.decode("utf-8")
        try:
            post_data = json.loads(body)
        except:
            post_data = body

    elif request.method == "DELETE":
        post_data = "DELETE запит отримано"

    return render(request, "http_help.html", {
        "post_data": post_data
    })



def product_add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")

        login = request.POST.get("login")
        email = request.POST.get("email")
        birth_date_str = request.POST.get("birth_date")
        phone = request.POST.get("phone")
        if ":" in login:
            return render(request, "product_form.html", {
                "error": "Логін не повинен містити символ ':'!"
            })

        if "@" not in email or "." not in email:
            return render(request, "product_form.html", {
                "error": "Некоректна e-mail адреса!"
            })
        try:
            birth_date = date.fromisoformat(birth_date_str)
        except:
            return render(request, "product_form.html", {
                "error": "Некоректна дата народження!"
            })

        if birth_date >= date.today():
            return render(request, "product_form.html", {
                "error": "Дата народження має бути у минулому!"
            })

        age = (date.today() - birth_date).days // 365
        if age < 18:
            return render(request, "product_form.html", {
                "error": "Мінімальний вік — 18 років!"
            })
        if len(phone) != 10 or not phone.isdigit():
            return render(request, "product_form.html", {
                "error": "Телефон повинен містити рівно 10 цифр!"
            })

        return render(request, "product_success.html", {
            "name": name,
            "price": price,
            "description": description,
            "login": login,
            "email": email,
            "birth_date": birth_date_str,
            "phone": phone,
        })

    return render(request, "product_form.html")

def delivery(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            return render(request, "delivery_success.html", {
                "data": form.cleaned_data
            })
    else:
        form = DeliveryForm()

    return render(request, "delivery_form.html", {"form": form})

def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            return render(request, "user_success.html", {"data": form.cleaned_data})
    else:
        form = UserForm()

    return render(request, "user_form.html", {"form": form})


def seed_page(request):
    return render(request, "seed_page.html")


@csrf_exempt
def seed(request):
    if request.method != "PATCH":
        return JsonResponse({"error": "PATCH required"}, status=405)

    username = "guest"
    password = "guest123"

    user, created = User.objects.get_or_create(username=username)

    if created:
        user.set_password(password)
        user.save()
        return JsonResponse({"status": "created", "user": username})

    user.set_password(password)
    user.save()
    return JsonResponse({"status": "updated", "user": username})

def login_view(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("profile")

        context["login_error"] = "Невірний логін або пароль"

    return render(request, "base.html", context)



def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, "base.html", {
                "register_error": "Паролі не співпадають"
            })

        if User.objects.filter(username=username).exists():
            return render(request, "base.html", {
                "register_error": "Користувач вже існує"
            })

        if User.objects.filter(email=email).exists():
            return render(request, "base.html", {
                "register_error": "Email вже використовується"
            })

        if not phone or len(phone) != 10 or not phone.isdigit():
            return render(request, "base.html", {
                "register_error": "Телефон має містити рівно 10 цифр"
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        profile = user.profile
        profile.phone = phone
        profile.save()

        login(request, user)
        return redirect("profile")

    return redirect("/")


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, "profile.html", {
        "profile": profile
    })
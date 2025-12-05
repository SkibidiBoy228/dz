from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from django.http import HttpResponse
import random
from django.utils import timezone


# технічно представлення - це функції, які приймають
# запит (request) та формують відповідь (response)
def hello(request) :
    return HttpResponse("Hello, world!")


def home(request):
    return HttpResponse("""
        <h1>Головна сторінка</h1>
        <a href='/about'>Про нас</a><br>
        <a href='/privacy'>Політика конфіденційності</a>
        <a href='/lottery'>Лотерея 6 з 42</a>
        <a href='/statics'>Статичні файли</a>
        <a href='/http-help'>Посилання-підказки</a>
        <a href='/product/add/'>Форм</a>
    """)

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
        phone = request.POST.get("phone")
        if len(phone) != 12 or not phone.isdigit():
            return render(request, "product_form.html", {
                "error": "Телефон повинен містити рівно 12 цифр!"
            })
        return render(request, "product_success.html", {
            "name": name,
            "price": price,
            "description": description,
            "phone": phone,
        })

    return render(request, "product_form.html")


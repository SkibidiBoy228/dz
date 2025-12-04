from django.shortcuts import render

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
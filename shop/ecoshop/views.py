from django.shortcuts import render
from django.http import HttpResponse
import datetime

GOODS = {
    'apple': {
        "cost": 3.24,
        "count": 435,
        "delive": ["Belarus", "Russia", "Poland"]
    },
    'orange': {
        "cost": 2.35,
        "count": 312,
        "delive": ["SAR", "Egypt", "Spain"]
    },
    'grape': {
        "cost": 12.64,
        "count": 214,
        "delive": ["Spain", "France", "Georgia"]
    },
}


def index(request):
    return render(request, "index.html")
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    #
    # return HttpResponse(html)


def info_ecoshop(request, ecoshop, street, number):
    context = {
        "ecoshop": ecoshop,
        "street": street,
        "number": number
    }
    return render(request, "info.html", context=context)


# return HttpResponse(f"{ecoshop} on adress {street} {number}")


def regular_views(request, year):
    return HttpResponse(f"year build is {year}")


def data_views(request):
    return HttpResponse(f"<h1> hello Tag h1</h1>")


def goods_catalog(request):
    context = {
        "goods": GOODS
    }
    return render(request, "goods_catalog.html", context=context)


def products(request):
    return render(request, "products.html")


def blog(request):
    return render(request, "blog.html")


def checkout(request):
    return render(request, "checkout.html")


def cart(request):
    return render(request, "cart.html")


def order_complete(request):
    return render(request, "order_complete.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def faq(request):
    return render(request, "faq.html")


def about_us(request):
    return render(request, "about_us.html")

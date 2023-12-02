from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)


def info_ecoshop(request, ecoshop, street, number):
    return HttpResponse(f"{ecoshop} on adress {street} {number}")


def regular_views(request, year):
    return HttpResponse(f"year build is {year}")


def data_views(request):
    return HttpResponse(f"<h1> hello Tag h1</h1>")

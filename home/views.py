from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>This is homepage</h1>")


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>This is contact</h1>")

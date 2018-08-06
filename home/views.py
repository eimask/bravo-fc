from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is home page",
        "my_number": 123,
        "my_list": [123, 132, 432]
    }
    return render(request, "home/index.html", my_context)


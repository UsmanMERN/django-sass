# import pathlib
from django.shortcuts import render
from django.http import HttpResponse


# this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request):
    my_title = "This is my Home page oo yeah !"
    my_context = {"page_title": my_title}
    return render(request, "home.html", my_context)

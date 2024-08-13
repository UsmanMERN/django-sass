# import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVists
# this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request):
    qs = PageVists.objects.all()
    page_qs = PageVists.objects.filter(path=request.path)
    my_title = "This is my Home page oo yeah !"
    my_context = {
        "page_title": my_title,
        "page_vist_count": page_qs.count(),
        "total_visit_count": qs.count(),
    }
    PageVists.objects.create(path=request.path)
    return render(request, "home.html", my_context)

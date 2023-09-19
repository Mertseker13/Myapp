from django.shortcuts import render
from .models import Destination


# Create your views here.

def main(request):
    dests = Destination.objects.all()
    return render(request, "main.html", {'dests': dests})

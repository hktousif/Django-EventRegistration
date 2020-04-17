from django.shortcuts import render, HttpResponse, redirect
from .models import *


# Create your views here.
def home_view(request):
    # obj = HomeSlidesModel.objects.all()
    # context = {'slides': obj}
    return render(request, "index.html")


def protocols_view(request):
    # obj = ProtocolsModel.objects.all()
    # context = {'prot': obj.values, }
    return render(request, "protocols.html")


def events_view(request):
    # obj = EventsModel.objects.all()
    # context = {"events": obj}
    return render(request, "events.html")


def about_view(request):
    # obj = AboutModel.objects.all()
    return render(request, "about_ibmr.html")


def gallery_view(request):
    # obj = GalleryModel.objects.all()
    # context = {'gallery': obj}
    return render(request, "gallery.html")


def support_view(request):
    return render(request, "support.html")


def register_view(request):

    context = {}
    return render(request, "register.html", context)

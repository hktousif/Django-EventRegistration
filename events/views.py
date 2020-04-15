from django.shortcuts import render, HttpResponse, redirect
from .models import *


# Create your views here.
def home_view(request):
    # obj = HomeSlidesModel.objects.all()
    # context = {'slides': obj}
    return render(request, "home.html")


def protocols_view(request):
    obj = ProtocolsModel.objects.all()
    context = {'prot': obj.values, }
    return render(request, "protocols.html", context)


def events_view(request):
    obj = EventsModel.objects.all()
    context = {"events": obj}
    return render(request, "events.html", context)


def about_view(request):
    obj = AboutModel.objects.all()
    return render(request, "about_ibmr.html", {"obj": obj})


def gallery_view(request):
    obj = GalleryModel.objects.all()
    context = {'gallery': obj}
    return render(request, "gallery.html", context)


def contact_view(request):
    obj = ContactModel.objects.all()
    context = {'contacts': obj}
    return render(request, "contact.html", context)

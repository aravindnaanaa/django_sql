from django.shortcuts import render

from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'flights/index.html',{
        "flights": models.Flight.objects.all(),
        "airports": models.Airport.objects.all(),
        "citys": models.Airport.objects.filter(city="New York"),
    } )

def flight(request,flight_id):
    flight = models.Flight.objects.get(pk=flight_id)
    return render (request, "flights/flights.html",{
        "flight":flight,
        "passangers": flight.passangers.all(),
        "not_passanger": models.Passanger.objects.exclude(flights=flight).all(),

    })

def book(request,flight_id):
    if request.method=="POST":
        flight = models.Flight.objects.get(pk=flight_id)
        passanger = models.Passanger.objects.get(pk=int(request.POST["passanger"]))
        passanger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args = [flight_id]))


""" Platzigram Views """

# Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime("%b %dth, %Y - %H: %M hrs")
    return HttpResponse("Oh, hi! Current server time is {now}".format(now=str(now)))

def sort_integers(request):
    """Return a JSON response whith sorted integers."""
    numbers = [int (i) for i in request.GET["numbers"].split(",")]
    sorted_ints = sorted(numbers)
    data = {
        "status": "ok",
        "numbers": sorted_ints,
        "message": "Integers sorted successfully."
    }
    #import pdb; pdb.set_trace()
    return HttpResponse(json.dumps(data), content_type="aplication/json")

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message= "Sorry, {}, you are not allowed her".format(name)
    else:
        message= "Hello, {}! Welcome to Platzigram".format(name)
    return HttpResponse(message)
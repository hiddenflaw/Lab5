from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person



people = []


class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def add_person(request):
    
    return HttpResponse("This is the add_person view.")



from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
import random

def index(request):
        numbers = ("one", "two", "three", "George", "Fred", "Wilma",) 
        y = random.choice(numbers)
        print(y)
        return render(request, 'index.html')


from django.shortcuts import render
from django.http import JsonResponse
import random

laJokes = [

    "Why don't scientists trust atoms? Because they make up everything!",
    "I'm reading a book on anti-gravity. It's impossible to put down.",
    "What do you call a fake noodle? An impasta!",
    "The other jokes here are chatgpt generated so if you see this you are lucky."
]

def exposeARandomJoke(request):
    theJoke = random.choice(laJokes)
    return JsonResponse({"theJoke": theJoke})

def index(request):
    return JsonResponse({"message": "Welcome to the Joke API! Go to /laughs to get a random joke."})

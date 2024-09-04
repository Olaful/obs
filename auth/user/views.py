from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.

def signup(request):
    print(type(request))
    return JsonResponse({"id": 123, "email": "test@test.com"})


def signin(request: WSGIRequest):
    if request.method == "POST":
        print(request.body)
        return JsonResponse({"access_token": "abdfdf123", ", refresh_token": "dfsdf3434"})


def me(request):
    return JsonResponse({"access_token": "abdfdf123", ", refresh_token": "dfsdf3434"})
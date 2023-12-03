from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def home(response):
    return render(response, "home.html", {})

def chatbox(request):
    if request.is_ajax():
        return JsonResponse({''})
    return render(request, "chatbox.html", {})
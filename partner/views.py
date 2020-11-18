from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {}
    return render(request, "index.html", ctx)

def signup(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        content = request.POST.get("content")


    ctx = {}
    return render(request, "signup.html", ctx)

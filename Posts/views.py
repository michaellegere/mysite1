from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.

def posts(request, *args, **kwargs):
    return HttpResponse("Hello, world. You're at the posts index.")
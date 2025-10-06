import os
from django.shortcuts import render

def index(request):
  context = {
    'some_exposed_secret': os.environ.get('FIREBASE_API_KEY')
  }
  return render(request, "index.html", context)

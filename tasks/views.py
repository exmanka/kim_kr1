from django.shortcuts import render

def index(request):
  context = {
    'some_exposed_secret': 'test_secret_12345'
  }
  return render(request, "index.html", context)

from django.shortcuts import render


def index(request):
  context = {
      'some_exposed_secret': 'FIREBASE_API_KEY'  # Добавлен тестовый секрет
  }
  return render(request, "index.html",
                context)  # Теперь передаём context в шаблон

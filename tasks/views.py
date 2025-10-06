import os
from django.shortcuts import render


def index(request):
  # Прочитать определенную строку из файла
  with open('tasks/templates/kim.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # Например, взять 3-ю строку (индекс 2)
    text_from_file = lines[5].strip() if len(lines) > 2 else ''
    text_from_file2 = lines[435].strip() if len(lines) > 2 else ''

  context = {
      'some_exposed_secret': os.environ.get('FIREBASE_API_KEY'),
      'text_from_file': text_from_file,
      'text_from_file2': text_from_file2,
  }
  return render(request, "index.html", context)

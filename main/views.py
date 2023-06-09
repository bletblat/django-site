from django.shortcuts import render
import datetime
 

def index(request):
    title = "Главная страница"
    date = datetime.datetime.today().strftime("%Y%m%d%M%S")
    return render(request, 'main/index.html', {'title': title, 'date': date})

def contacts(request):
    title = "Контакты"
    date = datetime.datetime.today().strftime("%Y%m%d%M%S")
    return render(request, 'main/contacts.html', {'title': title, 'date': date})

def clothers(request):
    title = "Одежда"
    date = datetime.datetime.today().strftime("%Y%m%d%M%S")
    return render(request, 'main/clothers.html', {'title': title, 'date': date})

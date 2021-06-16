from django.shortcuts import render, HttpResponse
from .models import Pessoa, Agenda

def home(request):
    return render(request, 'principal.html')

def cliente(request):
    allAulas = Agenda.objects.all()
    context = {'cliente': allAulas}
    return render(request, 'cliente.html', context)

def login(request):
    return render(request, 'login.html')

def adm(request):
    context = {'success': False}
    try:  
        if request.method=="POST":
            nome = request.POST['name']
            data = request.POST['date']
            hora = request.POST['hour']
            name1 = Pessoa.objects.get(name = nome)
            aula = Agenda.objects.create(name = name1, date = data, hour = hora)  
            context = {'success': True}
    except Pessoa.DoesNotExist:
        context = {'failure': True}
        return render(request, 'adm.html', context) 
    allAulas = Agenda.objects.all()
    context = {'cliente': allAulas}
    return render(request, 'adm.html', context)
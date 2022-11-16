from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa


def home(request):
    pessoas = Pessoa.objects.all()
    context= {
        "pessoas": pessoas
    }
    return render(request, 'index.html', context)

def salvar(request):
    vnome = request.POST.get("nome")
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()
    context= {
        "pessoas": pessoas
    }
    return render(request, 'index.html', context)

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})


def update(request, id):
    vnome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.save()
    return redirect(home)
    
def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)

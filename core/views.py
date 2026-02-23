from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Alunos
from .form import AlunosForm


def read(request):
    alunos = Alunos.objects.all()

    return render(request, 'core/read.html', {'alunos': alunos})


def create(request):
    form = AlunosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('read')

    return render(request, 'core/create.html', {'form': form})


def update(request, id):
    aluno = get_object_or_404(Alunos, id=id)

    form = AlunosForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('read')

    return render(request, 'core/update.html', {'form': form})


def delete(request, id):
   aluno = get_object_or_404(Alunos, id=id)
   if request.method == 'POST':
      aluno.delete()
      return redirect('read')
   return render(request, 'core/delete.html', {'aluno': aluno})
 
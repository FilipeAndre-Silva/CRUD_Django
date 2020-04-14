from django.shortcuts import render, redirect
from .models import Aluno
from .form import AlunoForm


# Create your views here.
def cadastrarAluno(request):
    form = AlunoForm(request.POST or None)# joga o formulario do form.py para a variavel form

    if form.is_valid():
        form.save()
        return redirect('listagem')

    return  render(request,'ControleAluno/cadastrar.html', {'form':form})# envia o form para o cadastrar.html

def listarAluno(request):
    listagem = {}#variavel para receber a lista de alunos
    listagem['alunos'] = Aluno.objects.all()# joga todos os Objetos registrados em listagem
    return render(request, 'ControleAluno/listar.html', listagem)

def editarAluno(request, pk):
    data = {} #variavel para guardar dados para o form.py
    aluno =  Aluno.objects.get(pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form #Passa o formulario preenchido com o objeto
    data['idAluno'] = aluno #Passa o ID do Aluno para o formulario de Edição
    return  render(request,'ControleAluno/cadastrar.html', data)

def deletarAluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
    return redirect('listagem')
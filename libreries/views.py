from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Document
from .forms import DocumentForm

# Create your views here.


def inicio(request):
    return render(request, 'pages/inicio.html')


def documents(request):
    documents = Document.objects.all()
    return render(request, 'documents/index.html', {'documents': documents})


def create(request):
    form = DocumentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('documents')
    return render(request, 'documents/create.html', {'form': form})


def edit(request, id):
    document = Document.objects.get(id=id)
    form = DocumentForm(request.POST or None,
                        request.FILES or None, instance=document)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('documents')
    return render(request, 'documents/edit.html', {'form': form})


def delete(request, id):
    document = Document.objects.get(id=id)
    document.delete()
    return redirect('documents')

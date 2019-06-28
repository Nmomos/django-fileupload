from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from upload.models import Document
from upload.forms import DocumentForm

def index(request):
    documents = Document.objects.all()
    return render(request, 'index.html', { 'documents': documents })

def basic_upload(request):
    if request.method == 'POST' and request.FILES['testfile']:
        myfile = request.FILES['testfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'basic_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'basic_upload.html')

def modelform_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'modelform_upload.html', {
        'form': form
    })
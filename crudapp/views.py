from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .forms import basic_form
from  . models import name

# Create your views here.

def index(request):
    context_dir={
        'request':request,
        'page':'This is the index page',
        'name':name.objects.raw('select * from crudapp_name')
    }
    return render(request, 'index.html', context=context_dir)
    
def basic_forms(request):
    form=basic_form()
    context_dir={
        'form':form,
        'request':request,
        'page':'This is the form page',
        'name':name.objects.raw('select * from crudapp_name')
    }
    if request.method == 'POST':
        #Simple html form
        context_dir.update({'html_form_data':{'name':request.POST.get('name'),'age':request.POST.get('age'),'gender':request.POST.get('gender')}})
        
        #Django form
        form=basic_form(request.POST)    
        if form.is_valid():
            #get form's data at once
            all_data=form.cleaned_data
            context_dir.update({'all_data':all_data})
            #get form data one by one
            form_details={'form_details':{'name':form.cleaned_data['name'],'age':form.cleaned_data['age'],'gender':form.cleaned_data['gender']}}
            context_dir.update(form_details)
            
        else:
            print("Form is not valid")
    return render(request, 'basic_form.html', context=context_dir)

    
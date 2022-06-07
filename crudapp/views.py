from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import basic_form,model_form,update
from  . models import info

# Create your views here.

def index(request):
    context_dir={
        'request':request,
        'page':'This is the index page',
        'form':info.objects.all(),
    }
    return render(request, 'index.html', context=context_dir)
    
def basic_forms(request):
    form=basic_form()
    context_dir={
        'form':form,
        'request':request,
        'page':'This is the form page',
        'form1':info.objects.all(),
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


def model_forms(request):
    modelform=model_form()
    
    context_dir={
        'modelform':modelform,
        'form':info.objects.all(),
        'request':request,
        'page':'This is the model_form page',
    }
    if request.method == 'POST':
        modelform=model_form(request.POST)
        if modelform.is_valid():
            modelform.save(commit=True)
            return redirect('crud')
    
    return render(request, 'model_form.html',context=context_dir)
    
    
def crud(request):
    context_dir={
        'info':info.objects.values()
    }
    return render(request, 'crud.html',context=context_dir)


def delete(request):
    id=request.GET.get('id')
    a=info.objects.get(id=id)
    a.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def update1(request):
    o=info.objects.get(id=request.GET.get('id'))
    updateform=update()
    context_dir={'form':updateform}
    if request.method == 'POST':
        updateform=update(request.POST)
        
        if updateform.is_valid():
            data=updateform.cleaned_data
            
            if len(data['name'])>0:
                o.name=data['name']
                o.save()
    
            if len(str(data['age']))>0:
                o.age=data['age']
                o.save()
                
            if len(data['gender'])>0:
                o.gender=data['gender']
                o.save()
        return redirect('crud')
    
    return render(request, 'update.html',context=context_dir)
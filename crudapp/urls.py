import re
from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'index$',views.index,name='index'),
    re_path(r'basic_form$',views.basic_forms,name='form'),
    re_path(r'model_form$',views.model_forms,name='model_form'),
    re_path(r'crud$',views.crud,name='crud'),   
    re_path(r'delete',views.delete,name='delete'),
    re_path(r'update',views.update1,name='update'),
]
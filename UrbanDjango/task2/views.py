from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class ClassStr(TemplateView):
    template_name = 'secondtask/class_template.html'


def func_str(request):
    return render(request, 'secondtask/func_template.html')


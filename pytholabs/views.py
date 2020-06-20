from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def course(request):
    module = Module.objects.first()
    context = {'m': module}
    return render(request, 'pytholabs/course.html', context)


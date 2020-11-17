from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .tasks import eml,go_to_sleep,add,mul
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"example/index.html")

def do_task(request):
    task_type=request.GET.get('task_type')
    x_num=request.GET.get('input_x')
    y_num=request.GET.get('input_y')
    if(task_type=='ADD'):
        result=add.delay(int(x_num),int(y_num))
    elif(task_type=='MUL'):
        result=mul.delay(int(x_num),int(y_num))
    elif(task_type=='EML'):
        result=eml.delay(x_num,y_num)
    data={
        'task_result':result.get()
    }
    return JsonResponse(data)

from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import TuduForm
from .models import Tudus


# Create your views here.

def index(request):
	tasks = Tudus.objects.all()
	form = TuduForm()
	print(tasks,'taskkkkk')
	if request.method =='POST':
		form = TuduForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	context = {'tasks':tasks, 'form':form}
	return render(request, 'index.html', context)

def deleteTask(request,pk):
    task = Tudus.objects.get(id=pk)
    if task:
        task.delete()
        return redirect('/')
    return redirect('/')


def updateTask(request, pk):
	task = Tudus.objects.get(id=pk)
	form = TuduForm(instance=task)
	if request.method == 'POST':
		form = TuduForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'update_task.html', context)



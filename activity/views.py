from django import forms
from .models import DailyPlan
from django.shortcuts import redirect, render
from .forms import DailyPlanForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, 'activity/index.html')

@login_required
def home(request):
    return render(request, 'activity/home.html')



"""views for plans"""
@login_required
def plans(request):
    tasks = DailyPlan.objects.filter(owner=request.user).order_by("-time_created")

    context = {'tasks':tasks}
    return render(request, 'activity/plans.html', context)




"""views for individual plans"""
@login_required
def plan(request, pk):

    tasks = DailyPlan.objects.all()
    task = DailyPlan.objects.get(id=pk)
    if task.owner != request.user:
        raise Http404

    context = {'tasks':tasks, 'task':task }
    return render(request, 'activity/plan.html', context )



"""views for adding a new plan"""
@login_required
def addplan(request):
    form = DailyPlanForm()
    

    if request.method == 'POST':
         form = DailyPlanForm(request.POST)
         if form.is_valid:
            new_plan = form.save(commit=False)
            new_plan.owner = request.user
            new_plan.save()
            form.save()
            return redirect('plans')

    context = {'form':form}
    return render(request, 'activity/addplan.html', context)



"""views for updating plan"""
@login_required
def update(request, pk):
    task = DailyPlan.objects.get(id=pk)
    form = DailyPlanForm(instance=task)
    

    if request.method == 'POST':
         form = DailyPlanForm(request.POST, instance=task)
         if form.is_valid:
             form.save()
             return redirect('plans')

    context = {'task':task, 'form':form}
    return render(request, 'activity/update.html', context )


@login_required
def delete(request, pk):
    task = DailyPlan.objects.get(id=pk)
    form = DailyPlanForm(instance=task)

    if request.method == 'POST':
        task.delete()
        return redirect('plans')


    context = {'task':task, 'form':form}
    return render(request, 'activity/delete.html', context )

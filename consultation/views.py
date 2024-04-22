from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Schedule
from .forms import ScheduleForm

@login_required
def schedule_input(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.save()
            return redirect('schedule_input')
    else:
        form = ScheduleForm()
    return render(request, 'input.html', {'form': form})

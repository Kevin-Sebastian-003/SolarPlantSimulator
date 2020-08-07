from .models import Plant, Device
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PlantForm
from .utils import Tasks, start_plant_sim_process
from django.urls import reverse


def index(request):
    plant_list = Plant.objects.order_by('-updated_at')
    context = {
        'plant_list': plant_list,
    }
    for plant in plant_list:
        if plant.plant_id in Tasks.tasks.keys():
            plant.status = "RUNNING"
        else:
            plant.status = "STOPPED"
    return render(request, 'plant/index.html', context)


def detail(request, name):
    plant_info = get_object_or_404(Plant, pk=name)
    devices = Device.objects.filter(plant_id=plant_info.plant_id)
    status = 'RUNNING' if plant_info.plant_id in Tasks.tasks.keys() else 'STOPPED'
    return render(request, 'plant/detail.html', {'plant_info': plant_info, 'devices': devices, 'status': status})


def create(request):
    return render(request, 'plant/create.html')


def create_plant(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlantForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('plant:plant_detail', args=(form.cleaned_data['plant_id'],)))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlantForm()

    return render(request, 'plant/create.html', {'form': form, 'button_text': 'Create'})


def edit_plant(request, plant_id):
    # if this is a PUT request we need to process the form data
    # check whether it's valid:
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('plant:plant_detail', args=(form.cleaned_data['plant_id'],)))
    else:
        form = PlantForm(instance=plant)

    return render(request, 'plant/create.html', {'form': form, 'button_text': 'Update'})
    
    
def start_plant_simulation(request, plant_id):
    if plant_id in Tasks.tasks:
        print("Already plant simulation is running, need to restart")
        Tasks.tasks[plant_id]["process"].terminate()
        Tasks.tasks[plant_id]["process"].is_alive()
        del Tasks.tasks[plant_id]

    print("Plant Simulation started")
    plant_interval = Plant.objects.filter(plant_id=plant_id)[0].interval
    p1 = start_plant_sim_process(plant_id, plant_interval)
    Tasks.tasks[plant_id] = {"process": p1, "action": "start", "pid": p1.pid}
    print(Tasks.tasks)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def stop_plant_simulation(request, plant_id):
    if plant_id not in Tasks.tasks:
        print("Plant simulation is not running")
    else:
        Tasks.tasks[plant_id]["process"].terminate()
        Tasks.tasks[plant_id]["process"].is_alive()
        del Tasks.tasks[plant_id]
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def delete_plant(request, plant_id):
    if plant_id in Tasks.tasks:
        Tasks.tasks[plant_id]["process"].terminate()
        Tasks.tasks[plant_id]["process"].is_alive()
        del Tasks.tasks[plant_id]
    Plant.objects.filter(pk=plant_id).delete()
    return HttpResponseRedirect(reverse('plant:plant_index'))

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from plant.models import Device
from plant.forms import DeviceForm
from django.urls import reverse


def index(request):
    device_list = Device.objects.order_by('-updated_at')
    context = {
        'device_list': device_list,
    }
    return render(request, 'devices/index.html', context)


def detail(request, name):
    device_info = get_object_or_404(Device, pk=name)
    return render(request, 'devices/detail.html', {'device_info': device_info})


def create(request):
    return render(request, 'devices/create.html')


def create_device(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DeviceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('plant:plant_detail', args=(form.cleaned_data['plant_id'].plant_id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DeviceForm()

    return render(request, 'devices/create.html', {'form': form, 'button_text': 'Create'})


def edit_device(request, name):
    dev_obj = get_object_or_404(Device, pk=name)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=dev_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('plant:plant_detail', args=(dev_obj.plant_id_id,)))
    else:
        form = DeviceForm(instance=dev_obj)

    return render(request, 'devices/create.html', {'form': form, 'button_text': 'Update'})


def delete_device(request, name):
    dev_obj = get_object_or_404(Device, pk=name)
    plant_id = dev_obj.plant_id_id
    dev_obj.delete()
    return HttpResponseRedirect(reverse('plant:plant_detail', args=(plant_id,)))


def start_device(request, name):
    dev_obj = get_object_or_404(Device, pk=name)
    dev_obj.status = "RUNNING"
    dev_obj.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def stop_device(request, name):
    dev_obj = get_object_or_404(Device, pk=name)
    dev_obj.status = "STOPPED"
    dev_obj.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
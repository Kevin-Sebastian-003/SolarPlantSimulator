import threading
import time
import requests
from .models import Device, Plant, EndPoint, TargetUri
from devices.inverter import Inverter
from devices.weather_station import Weather_Station
from multiprocessing import Process


class Tasks:
    tasks = {}


def start_plant_sim_process(plant_id, interval):
    p1 = Process(target=pump_data, args=(plant_id, interval))
    p1.start()
    return p1


def pump_data(plant_id, interval=60):
    while True:

        # repeat this for different device types
        inverter_devices = Device.objects.filter(plant_id=plant_id, type=1, status='RUNNING')
        inverter_data = {"plant_id": plant_id, "inverter_list": []}
        for device in inverter_devices:
            inverter_data['inverter_list'].append(
                Inverter(
                    plant_id=plant_id,
                    block_id=device.block_id,
                    room_id=device.room_id,
                    inverter_id=device.device_id,
                ).generate_random_data())
        inverter_cloud_url = "http://%s%s" % (
                        EndPoint.objects.filter(type=1)[0].endpoint,
                        TargetUri.objects.filter(pk=1)[0].uri)

        inverter_local_url = "http://%s%s" %(
                    EndPoint.objects.filter(type=2)[0].endpoint,
                    TargetUri.objects.filter(pk=1)[0].uri)

        try:
            r = requests.post(url=inverter_cloud_url, json=inverter_data, timeout=1)
            r = requests.post(url=inverter_local_url, json=inverter_data, timeout=1)
        except Exception:
            pass

        # Till here the processing for inverters is done
        #  Repeat this block for other device types
        #  TargetUri type value differs for each type
        ws_devices = Device.objects.filter(plant_id=plant_id, type=1, status='RUNNING')
        ws_data = {"plant_id": plant_id, "ws_list": []}
        for device in ws_devices:
            ws_data['ws_list'].append(
                Weather_station(
                    plant_id=plant_id,
                    block_id=device.block_id,
                    room_id=device.room_id,
                    ws_id=device.device_id,
                ).generate_random_data())
        ws_cloud_url = "http://%s%s" % (
                        EndPoint.objects.filter(type=1)[0].endpoint,
                        TargetUri.objects.filter(pk=1)[0].uri)

        ws_local_url = "http://%s%s" %(
                    EndPoint.objects.filter(type=2)[0].endpoint,
                    TargetUri.objects.filter(pk=1)[0].uri)

        try:
            r = requests.post(url=ws_cloud_url, json=ws_data, timeout=1)
            r = requests.post(url=ws_local_url, json=ws_data, timeout=1)
        except Exception:
            pass
        time.sleep(interval)

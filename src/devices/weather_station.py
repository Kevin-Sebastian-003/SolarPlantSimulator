
from .utils import Field, RangeField, MultiField
from .utils import get_default_data, get_random_data
import time

class Weather_Station():
    def __init__(self, plant_id, block_id, room_id, ws_id, **kwargs):
        self.block_id = block_id
        self.ws_id = ws_id
        self.sensor_time =  Field(sensor_time, int, 0, 5, 10)
        self.sensor_time_min =  Field(sensor_time_min, int, 0, 5, 10)
        self.wind_speed =  Field(wind_speed, float, 1, 50, 100)
        self.direction =  Field(direction, int, 0, 0, 7)
        self.temperature =  Field(temperature, float, 1, 50, 100)
        self.humidity =  Field(humidity, float, 1, 50, 100)
        self.pressure =  Field(pressure, float, 1, 50, 100)
        self.irradiance_horizontal =  Field(irradiance_horizontal, float, 1, 50, 100)
        self.irradiance_vertical =  Field(irradiance_vertical, float, 1, 50, 100)
        self.radiation =  Field(radiation, float, 1, 50, 100)
        self.module_temp =  Field(module_temp, float, 1, 50, 100)
        self.aux_supply_voltage =  Field(aux_supply_voltage, float, 1, 50, 100)
        self.rain_gauge =  Field(rain_gauge, float, 1, 50, 100)
        self.ambient_temp =  Field(ambient_temp, float, 1, 50, 100)
        self.ignore_status =  Field(ignore_status, int, 0, 0, 0)
        self.pk_status =  Field(pk_status, int, 0, 0, 0)


    def generate_random_data(self):
        data = get_random_data(self)
        data["ws_room"] = self.ws_room
        data["ws_id"] = self.ws_id
        data["block_id"] = self.block_id
        data["sensor_time"] = int(time.time())

        return data

    def generate_default_data(self):
        data = get_default_data(self)
        data["ws_room"] = self.ws_room
        data["ws_id"] = self.ws_id
        data["block_id"] = self.block_id
        data["sensor_time"] = int(time.time())
        return data 

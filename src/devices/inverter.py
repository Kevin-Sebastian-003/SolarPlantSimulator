
from .utils import Field, RangeField, MultiField
from .utils import get_default_data, get_random_data
import time

class MPPT(MultiField):
    def __init__(self, name):
        self.name = name
        self.power = RangeField('power', float, (21000,22000), (24000, 25000), (24214.0,27300.0))
        self.voltage = RangeField('voltage', float, (51000,52000), (54000, 55000), (54214.0,53300.0))
        self.current = RangeField('current', float, (400,450), (500, 600), (460.0,530.0))
        self.energy = RangeField('energy', float, (0,0), (0, 1), (0,0))


class Inverter():
    def __init__(self, plant_id, block_id, room_id, inverter_id, **kwargs):
        self.block_id = block_id
        self.inverter_room = room_id
        self.inverter_id = inverter_id
        self.l1_ac_vlg = Field('l1_ac_vlg', float, 100, 500, 200)
        self.l2_ac_vlg = Field('l2_ac_vlg', float, 100, 500, 200)
        self.l3_ac_vlg = Field('l3_ac_vlg', float, 100, 500, 200)
        self.l1_ac_current = Field('l1_ac_current', float, 5, 10, 7)
        self.l2_ac_current = Field('l2_ac_current', float, 5, 10, 7)
        self.ac_power_l1 = Field("ac_power_l1", int, 0, 1, 0)
        self.ac_power_l2 = Field("ac_power_l2", int, 0, 1, 0)
        self.ac_power_l3 = Field("ac_power_l3", int, 0, 1, 0)
        self.dc_voltage = RangeField("dc_voltage", float, (0,0), (1,1), (0,1))
        self.dc_current = RangeField("dc_current", float, (0,0), (1,1), (0,1))
        self.dc_power = RangeField('dc_power', float, (0,0), (5,10), (5.22,0.0))
        self.dc_energy = RangeField('dc_power', float, (0,0), (5,10), (5.22,0.0))
        self.leakage_current = Field('leakage_current', int, 0, 10, 0)
        self.rdy_ref = Field('rdy_ref', int, 0, 0, 0)
        self.rdy_run = Field('rdy_run', int, 0, 0, 0)
        self.pk_status = Field('pk_status', int, 0, 0, 0)
        self.power_factor = Field('power_factor', int, 0, 0, 0)
        self.energy = Field('energy', float, 17000, 18000, 17524.37)
        self.energy_today = Field('energy_today', float, 0, 1000, 0.0)
        self.efficiency = Field('efficiency', int, 0, 1, 0)
        self.ac_frequency = Field('ac_frequency', float, 45, 55, 49.99)
        self.inverter_temp = Field('inverter_temp', float, 0.0, 20.0, 0.0)
        self.ac_power = Field('ac_power', float, 4, 10, 4.99)
        self.inverter_status = Field('inverter_status', float, 3, 10, 4.0)
        self.net_ok = Field('net_ok', int, 0, 1, 0)
        self.reactive_power = Field('reactive_power', int, 0, 1, 0)
        self.grid_lost = Field('grid_lost', int, 0, 1, 0)
        self.ignore_status = Field('ignore_status', int, 0, 1, 0)
        self.generation_status = Field('generation_status', int, 0, 1, 0)
        self.mppt = MPPT('mppt')

    def generate_random_data(self):
        data = get_random_data(self)
        data["inverter_room"] = self.inverter_room
        data["inverter_id"] = self.inverter_id
        data["block_id"] = self.block_id
        data["sensor_time"] = int(time.time())

        return data

    def generate_default_data(self):
        data = get_default_data(self)
        data["inverter_room"] = self.inverter_room
        data["inverter_id"] = self.inverter_id
        data["block_id"] = self.block_id
        data["sensor_time"] = int(time.time())
        return data 

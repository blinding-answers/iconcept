import logging

logger = logging.getLogger(__name__)
from typing import List, Union

from iconcept.enums.fitness_device_type import FitnessDeviceType
from iconcept.enums.fitness_device_unit import FitnessDeviceUnit
from iconcept.enums.fitness_devices_status import FitnessDeviceStatus


class FitnessDevice:

    def __init__(self):
        self.__device_name = None
        self.__device_speed = None
        self.__device_pulse = None
        self.__device_incline = None
        self.__device_unit = None
        self.__device_type = None
        self.__connection_state = 0
        self.__device_status = None

    @property
    def device_name(self):
        return self.__device_name

    @device_name.setter
    def device_name(self, value):
        self.__device_name = value

    @property
    def device_speed(self):
        return self.__device_speed

    @device_speed.setter
    def device_speed(self, value):
        self.__device_speed = value

    @property
    def device_pulse(self):
        return self.__device_pulse

    @device_pulse.setter
    def device_pulse(self, value):
        self.__device_pulse = value

    @property
    def device_incline(self):
        return self.__device_incline

    @device_incline.setter
    def device_incline(self, value):
        self.__device_incline = value

    @property
    def device_unit(self):
        return self.__device_unit

    @device_unit.setter
    def device_unit(self, value):
        self.__device_unit = value

    @property
    def device_type(self):
        return self.__device_type

    @device_type.setter
    def device_type(self, value):
        self.__device_type = value

    @property
    def device_status(self):
        return self.__device_status

    @device_status.setter
    def device_status(self, value):
        self.__device_status = value

    @property
    def connection_state(self):
        return self.__connection_state

    @connection_state.setter
    def connection_state(self, value: int):
        self.__connection_state = value

    def is_bike(self):
        return self.device_type == FitnessDeviceType.BIKE

    def is_elliptical(self):
        return self.device_type == FitnessDeviceType.ELLIPTICAL

    def is_treadmill(self):
        return self.device_type == FitnessDeviceType.TREADMILL

    def is_bike_or_elliptical(self):
        return self.is_bike() or self.is_elliptical()

    def is_offline(self):
        return self.device_status == FitnessDeviceStatus.OFFLINE

    def is_standby(self):
        return self.device_status == FitnessDeviceStatus.STANDBY

    def is_running(self):
        return self.device_status == FitnessDeviceStatus.RUNNING

    def is_paused(self):
        return self.device_status == FitnessDeviceStatus.PAUSED

    def is_connected(self):
        return self.device_status != FitnessDeviceStatus.OFFLINE

    def is_metric(self):
        return self.device_unit == FitnessDeviceUnit.METRIC

    def is_imperial(self):
        return self.device_unit != FitnessDeviceUnit.METRIC

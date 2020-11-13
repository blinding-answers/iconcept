import logging

logger = logging.getLogger(__name__)
from typing import List, Union
from multiprocessing import Queue
from iconcept import UnitUtil

from iconcept import FitnessDeviceListenerBase


class FitnessDevice:
    COMMAND_QUERY_MANUFACTURER = [85, -75, 1, -1]  # 55b41ff
    COMMAND_RESET = [85, 10, 1, 2]  # 550a0102
    COMMAND_START = [85, 10, 1, 1]  # 550a0101
    COMMAND_PAUSE = [85, 10, 1]  # 550a01
    COMMAND_STOP = [85, 10, 1, 3]  # 550a0103
    COMMAND_ENABLE_START_KEY = [85, 8, 1, 1]  # 55080101

    DEVICE_TYPE_BIKE = 0
    DEVICE_TYPE_ELLIPTICAL = 1
    DEVICE_TYPE_TREADMILL = 2

    DEVICE_STATUS_OFFLINE = 0
    DEVICE_STATUS_STANDBY = 1
    DEVICE_STATUS_RUNNING = 2
    DEVICE_STATUS_PAUSED = 3

    DEVICE_UNIT_METRIC = 0

    def __init__(self, command_q: Queue):
        self.__device_name = None
        self.__device_speed = None
        self.__device_pulse = None
        self.__device_incline = None
        self.__device_unit = None
        self.__device_type = None
        self.__connection_state = 0
        self.__device_status = None
        self.command_q = command_q
        self.device_listerners: Union[List[FitnessDeviceListenerBase], None] = None

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

    # def connect(self, hardware_address):
    #     self.chat_service.connect(hardware_address=hardware_address)
    #     self.chat_service.start_communication()

    def send_command(self, command):
        logger.debug(f"Sending command:  {command}")
        self.command_q.put(command)

    def init_device(self):
        commands = [
            [85, 12, 1, -1],  # 0  - 550c01ff
            [85, -69, 1, -1],  # 1 - 55BB01ff
            [85, 36, 1, -1],  # 2 - 552401ff
            [85, 37, 1, -1],  # 3 - 552501ff
            [85, 38, 1, -1],  # 4 - 552601ff
            [85, 39, 1, -1],  # 5 - 552701ff
            [85, 2, 1, -1],  # 6 - 550201ff
            [85, 3, 1, -1],  # 7 - 550301ff
            [85, 4, 1, -1],  # 8 - 550401ff
            [85, 6, 1, -1],  # 9 - 550601ff
            [85, 31, 1, -1],  # 10 - 551f01ff
            [85, -96, 1, -1],  # 11 - 55a001ff
            [85, -80, 1, -1],  # 12 - 55b001ff
            [85, -78, 1, -1],  # 13 - 55b201ff
            [85, -77, 1, -1],  # 14 - 55b301ff
            [85, -76, 1, -1],  # 15 - 55b401ff
            [85, -75, 1, -1],  # 16 - 55b501ff
            [85, -74, 1, -1],  # 17 - 55b601ff
            [85, -73, 1, -1],  # 18 - 55b701ff
            [85, -72, 1, -1],  # 19 - 55b801ff
            [85, -71, 1, -1],  # 20 - 55b901ff
            [85, -70, 1, -1],  # 21 - 55ba01ff
            [85, 11, 1, -1],  # 22 - 550b01ff
            [85, 24, 1, -1],  # 23 - 551801ff
            [85, 25, 1, -1],  # 24 - 551901ff
            [85, 26, 1, -1],  # 25 - 551a01ff
            [85, 27, 1, -1],  # 26 - 551b01ff
        ]

        # join into single command..
        command_to_send = []
        for command in commands:
            logger.debug(f"adding  {command}")
            command_to_send += command
        self.send_command(command_to_send)

    def set_action_mode(self, mode: int):
        logger.debug(f"SET ACTION MODE: {mode}")
        command = [85, 21, 1, mode]
        self.send_command(command)

    def queryManufacturer(self):
        logger.debug("QUERY MANUFACTURER")
        self.send_command(self.COMMAND_QUERY_MANUFACTURER)

    def reset(self):
        logger.debug("RESET")
        self.send_command(self.COMMAND_RESET)

    def start(self):
        logger.debug("START")
        self.send_command(self.COMMAND_START)

    def pause(self):
        logger.debug("PAUSE")
        self.send_command(self.COMMAND_PAUSE)

    def stop(self):
        logger.debug("STOP")
        self.send_command(self.COMMAND_STOP)

    def is_bike(self):
        return self.device_type == self.DEVICE_TYPE_BIKE

    def is_elliptical(self):
        return self.device_type == self.DEVICE_TYPE_ELLIPTICAL

    def is_treadmill(self):
        return self.device_type == self.DEVICE_TYPE_TREADMILL

    def is_bike_or_elliptical(self):
        return self.is_bike() or self.is_elliptical()

    def is_offline(self):
        return self.device_status == self.DEVICE_STATUS_OFFLINE

    def is_standby(self):
        return self.device_status == self.DEVICE_STATUS_STANDBY

    def is_running(self):
        return self.device_status == self.DEVICE_STATUS_RUNNING

    def is_paused(self):
        return self.device_status == self.DEVICE_STATUS_PAUSED

    def is_connected(self):
        return self.device_status != self.DEVICE_STATUS_OFFLINE

    def is_metric(self):
        return self.device_unit == self.DEVICE_UNIT_METRIC

    def is_imperial(self):
        return self.device_unit != self.DEVICE_UNIT_METRIC

    #  TODO figure out the unit of speed
    def set_target_speed(self, speed: float):
        logger.debug(f"SET TARGET SPEED: {speed}")
        speed = float(speed)
        if not self.is_metric():
            speed = UnitUtil.mile2km(speed)
        # byte[] command = { 85, 15, 2, speedByte1, speedByte2 };
        speed_whole = int(speed)
        speed_dec = int(round((speed - float(speed_whole)), 1) * 100)
        command = [85, 15, 2, speed_whole, speed_dec]
        self.send_command(command)

    def set_target_time_distance_and_calorie(self, time: int, distance: float, calorie: float):

        if not self.is_metric():
            distance = UnitUtil.mile2km(distance)

        distance_whole = int(distance)
        distance_dec = int(round((distance - float(distance_whole)), 1) * 100)

        calorie_div_mod = divmod(calorie, 256)
        command = [85, 14, 5, time, distance_whole, distance_dec, calorie_div_mod[0], calorie_div_mod[1]]
        self.send_command(command)

    def set_incline(self, incline: int):
        logger.debug(f"SET INCLINE: {incline}")
        command = [85, 17, 1, incline]
        self.send_command(command)

    def enable_start_key(self):
        logger.debug("ENABLE START KEY")
        self.send_command(self.COMMAND_ENABLE_START_KEY)

    def notify_brand(self):
        pass

    def notify_device_connect_failed(self):
        pass

    def notify_device_connected(self):
        pass

    def notify_device_disconnected(self):
        pass

    def notify_device_paused(self):
        pass

    def notify_device_resumed(self):
        pass

    def notify_device_started(self):
        pass

    def notify_device_stopped(self):
        pass

    def notify_device_update(self):
        pass

    def notify_manufacturer(self, value):
        pass

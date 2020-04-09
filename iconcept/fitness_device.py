import logging

logger = logging.getLogger(__name__)
from typing import List, Union
from iconcept.bluetooth import ChatListener, ChatService
from multiprocessing.managers import BaseProxy
from multiprocessing import Queue

"""
use python3 sockets and asyncio

"""

def fitness_device_factory(command_q):
    return FitnessDevice(command_q=command_q)

class FitnessDeviceProxy(BaseProxy):

    def init_device(self):
        self._callmethod("init_device")

    def set_connection_state(self, value):
        self._callmethod("set_connection_state",[value])
    
    def get_connection_state(self):
        return self._callmethod("get_connection_state")

    def start(self):
        self._callmethod("start")
        
    def set_target_speed(self, value):
        self._callmethod("set_target_speed",[value])
    
    def set_device_speed(self,value):
        self._callmethod("__set_device_speed",[value])

    def set_device_pulse(self, value):
        self._callmethod("__set_device_pulse",[value])

    def set_device_incline(self, value):
        self._callmethod("__set_device_inline",[value])

    
    


class FitnessDevice:
    COMMAND_QUERY_MANUFACTURER = [85, -75, 1, -1]
    COMMAND_RESET = [85, 10, 1, 2]
    COMMAND_START = [85, 10, 1, 1]
    COMMAND_PAUSE = [85, 10, 1]
    COMMAND_STOP = [85, 10, 1, 3]

    def __init__(self, command_q:Queue):
        """
            this.mListeners = new ConcurrentLinkedQueue<FitnessHwApiDeviceListener>();
            this.mChatService = new BluetoothChatService();
            this.mChatService.setListener(this.mBluetoothChatListener);
        """

        self.__speed=None
        self.__pulse=None
        self.__incline=None
        self.__connection_state=0
        self.command_q=command_q
        self.device_listerners = None


    def set_connection_state(self, value:int):
        self.__connection_state=value

    def get_connection_state(self):
        return self.__connection_state

    # def connect(self, hardware_address):
    #     self.chat_service.connect(hardware_address=hardware_address)
    #     self.chat_service.start_communication()

    def send_command(self, command):
        logger.debug(f"Sending command:  {command}")
        self.command_q.put(command)

    def init_device(self):
        commands = [
            [85, 12, 1, -1],
            [85, -69, 1, -1],
            [85, 36, 1, -1],
            [85, 37, 1, -1],
            [85, 38, 1, -1],
            [85, 39, 1, -1],
            [85, 2, 1, -1],
            [85, 3, 1, -1],
            [85, 4, 1, -1],
            [85, 6, 1, -1],
            [85, 31, 1, -1],
            [85, -96, 1, -1],
            [85, -80, 1, -1],
            [85, -78, 1, -1],
            [85, -77, 1, -1],
            [85, -76, 1, -1],
            [85, -75, 1, -1],
            [85, -74, 1, -1],
            [85, -73, 1, -1],
            [85, -72, 1, -1],
            [85, -71, 1, -1],
            [85, -70, 1, -1],
            [85, 11, 1, -1],
            [85, 24, 1, -1],
            [85, 25, 1, -1],
            [85, 26, 1, -1],
            [85, 27, 1, -1],
        ]

        # join into single command..
        command_to_send = []
        for command in commands:
            logger.debug(f"adding  {command}")
            command_to_send += command
        self.send_command(command_to_send)

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

    def set_target_speed(self, speed: float):
        logger.debug(f"Set speed to {speed}")
        speed = float(speed)
        # Double speedToCode = Double.valueOf(speed);
        # if (!isMetric()) speedToCode = Double.valueOf(UnitUtil.km2mile(speedToCode.doubleValue()));
        # byte speedByte1 = (byte)speedToCode.intValue();
        # speedToCode = Double.valueOf((speedToCode.doubleValue() - speedToCode.intValue()) * 100.0D);
        # byte speedByte2 = (byte)speedToCode.intValue();

        # byte[] command = { 85, 15, 2, speedByte1, speedByte2 };
        speed_whole = int(speed)
        speed_dec = int((speed - float(speed_whole)) * 100)
        command = [85, 15, 2, speed_whole, speed_dec]
        self.send_command(command)

    def set_incline(self, incline: int):
        logger.debug(f"Set incline to {incline}")
        command = [85, 17, 1, incline]
        self.send_command(command)

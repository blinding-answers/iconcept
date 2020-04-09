import logging

logger = logging.getLogger(__name__)

from multiprocessing.managers import BaseProxy

from abc import ABCMeta, abstractmethod


class ChatListernerABC(metaclass=ABCMeta):
    @abstractmethod
    def on_connect_success(self, param_string: str):
        pass

    @abstractmethod
    def on_connect_failed(self, exception: Exception):
        pass

    @abstractmethod
    def on_connect_lost(self):
        pass

    @abstractmethod
    def on_data_read(self, parram_bytes: bytes):
        pass

    @abstractmethod
    def on_data_write(self, parram_bytes: bytes):
        pass

    @abstractmethod
    def on_state_changed(self, param_int: int):
        pass


class ChatListener(ChatListernerABC):
    def __init__(self, device):
        self.device = device

    def on_connect_success(self, param_string: str):
        logger.debug(f"on_connect_success: {param_string}")
        self.device.init_device()

        # init device
        # FitnessHwApiDevice.this.mDeviceName = name;
        # FitnessHwApiDevice.this.initRemoteDevice();
        # FitnessHwApiDevice.this.startKeepAlive();
        pass

    def on_connect_failed(self, exception: Exception):
        #  FitnessHwApiDevice.this.notifyDeviceConnectFailed();
        logger.exception(exception)
        raise exception

    def on_connect_lost(self):
        # FitnessHwApiDevice.this.stopKeepAlive();
        # FitnessHwApiDevice.this.notifyDeviceDisconnected();
        pass

    def on_data_read(self, message):
        # all the magic happens here
        logger.debug(f"on_data_read: {message}")
        pass

    def on_data_write(self, parram_bytes: bytes):
        pass

    def on_state_changed(self, param_int: int):
        logger.debug(f"on_state_changed: {param_int}")
        self.device.set_connection_state(param_int)

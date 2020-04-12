from abc import ABCMeta, abstractmethod


class FitnessDeviceListenerBase(metaclass=ABCMeta):
    @abstractmethod
    def on_brand(self, value: str):
        pass

    @abstractmethod
    def on_device_connect_failed(self):
        pass

    @abstractmethod
    def on_device_connected(self, value: str):
        pass

    @abstractmethod
    def on_device_disconnected(self):
        pass

    @abstractmethod
    def on_manufacturer(self, value):
        pass

    @abstractmethod
    def on_device_paused(self):
        pass

    @abstractmethod
    def on_device_resumed(self):
        pass

    @abstractmethod
    def on_device_speed_limit(self, value1, value2):
        pass

    @abstractmethod
    def on_device_started(self):
        pass

    @abstractmethod
    def on_device_stopped(self, value):
        pass

    @abstractmethod
    def on_dvice_update(self, value):
        pass

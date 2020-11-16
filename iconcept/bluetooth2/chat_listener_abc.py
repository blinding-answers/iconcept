from abc import ABCMeta, abstractmethod
import logging

logger = logging.getLogger(__name__)


class ChatListenerABC(metaclass=ABCMeta):
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
    def on_data_read(self, data: bytes):
        pass

    @abstractmethod
    def on_data_write(self, data: bytes):
        pass

    @abstractmethod
    def on_state_changed(self, param_int: int):
        pass

from abc import ABCMeta, abstractmethod


class AbstractChannel(metaclass=ABCMeta):

    @abstractmethod
    def send(self, command: str):
        pass



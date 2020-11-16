from abc import ABCMeta, abstractmethod


class AbstractDatagram(metaclass=ABCMeta):

    @abstractmethod
    def ingest_data(self, data: str) -> None:
        pass

    @abstractmethod
    def get_header_pattern(self) -> str:
        pass

    @abstractmethod
    def get_header_length(self) -> int:
        pass

    @abstractmethod
    def get_message_length(self) -> int:
        pass

    def get_total_length(self) -> int:
        return self.get_header_length() + self.get_message_length()

    @abstractmethod
    def is_valid(self) -> bool:
        pass

    def __str__(self):
        return self.__class__.__name__

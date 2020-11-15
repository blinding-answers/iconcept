from abc import ABCMeta, abstractmethod


class AbstractMessage(metaclass=ABCMeta):
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

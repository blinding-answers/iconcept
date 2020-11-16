from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram
from iconcept.exceptions.invalid_datagram_exception import InvalidDatagramException


class DeviceType(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        return '55BB01'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 2

    def is_valid(self) -> bool:
        if self.message is None:
            return False

        if self.__extract_type() in [1, 2, 3]:
            return True

        return False

    def get_type(self) -> int:
        if not self.is_valid():
            raise InvalidDatagramException(__name__)

        return self.__extract_type()

    def __extract_type(self) -> int:
        start = self.get_header_length()
        end = start + self.get_message_length()
        hex_string = self.message[start: end]
        return int(hex_string, 16)

    def __str__(self):
        return f"{self.__class__.__name__}: type={self.get_type()}"

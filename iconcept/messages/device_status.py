from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram
from iconcept.exceptions.invalid_datagram import InvalidDatagram

class DeviceStatus(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        return '550901'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 2

    def is_valid(self) -> bool:
        if self.message is None:
            return False
        # validate data
        if self.__extract_status() in [0, 1, 2]:
            return True

        return False

    def get_status(self) -> int:
        if not self.is_valid():
            raise InvalidDatagram(__name__)

        return self.__extract_status()

    def __extract_status(self) -> int:
        start = self.get_header_length()
        end = start + self.get_message_length()
        status_hex = self.message[start: end]
        return int(status_hex, 16)

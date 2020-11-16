from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram


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
        return self.message is not None

    def get_type(self) -> int:
        if not self.is_valid():
            return 0

        type_hex = self.message[6: 6 + 2]
        return int(type_hex, 16)

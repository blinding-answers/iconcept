from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram


class DevicePulseTypeQuery(AbstractDatagram):
    # 55070100
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        return '550701FF'

    def get_header_length(self) -> int:
        return 8

    def get_message_length(self) -> int:
        return 0

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"

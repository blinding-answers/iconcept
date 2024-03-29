from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram


class DeviceManufacturer(AbstractDatagram):
    # 55B40C 313230374D20202020202020

    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        return '55B40C'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 24

    def is_valid(self) -> bool:
        return self.message is not None

    def get_manufacturer(self) -> str:
        if not self.is_valid():
            return ''

        manufacturer_hex = self.message[6: 6 + self.get_message_length()]
        return bytearray.fromhex(manufacturer_hex).decode()

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}: manufacturer={self.get_manufacturer()}"

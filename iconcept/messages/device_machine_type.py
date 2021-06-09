from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram


class DeviceMachineType(AbstractDatagram):
    # 55BA14 4455414C4B495420545245414420202020202020 (DUALKIT TREAD       )
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        return '55BA14'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 40

    def is_valid(self) -> bool:
        return self.message is not None

    def get_model(self) -> str:
        if not self.is_valid():
            return ''

        model_hex = self.message[6: 6 + self.get_message_length()]
        return bytearray.fromhex(model_hex).decode()

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}: model={self.get_model()}"

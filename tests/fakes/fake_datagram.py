from iconcept.messages.abstract_datagram import AbstractDatagram


class FakeDatagram(AbstractDatagram):
    header_pattern: str = ''
    header_length: int = 0
    message_length: int = 0

    def __init__(self, header_pattern: str, header_length: int, message_length: int):
        self.header_pattern = header_pattern
        self.header_length = header_length
        self.message_length = message_length
        self.message = None

    def ingest_data(self, data: str) -> None:
        self.message = data

    def get_header_pattern(self) -> str:
        return self.header_pattern

    def get_header_length(self) -> int:
        return self.header_length

    def get_message_length(self) -> int:
        return self.message_length

    def is_valid(self) -> bool:
        return self.message is not None

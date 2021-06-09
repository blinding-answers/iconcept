from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram


class DeviceTargetSpeedCommand(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        return '550F02'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 4

    def is_valid(self) -> bool:
        return self.message is not None

    def get_speed(self) -> float:
        if not self.is_valid():
            return 0

        speed_left_part = int(self.message[6: 6 + 2], 16)
        speed_right_part = int(self.message[8: 8 + 2], 16)
        speed = speed_left_part + speed_right_part / 100
        return speed

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}: DeviceTargetSpeedCommand: {self.get_speed()}"

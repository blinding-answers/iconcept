from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram
import json


class DeviceFeedback(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        return '550D'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 20

    def is_valid(self) -> bool:
        return self.message is not None

    def get_time(self) -> int:
        if not self.is_valid():
            return 0

        time_hex = self.message[6: 6 + 4]
        return int(time_hex, 16)

    def get_distance(self) -> float:
        if not self.is_valid():
            return 0.0

        distance_integer_hex = self.message[10: 10 + 2]
        distance_integer = int(distance_integer_hex, 16)

        distance_fraction_hex = self.message[12: 12 + 2]
        distance_fraction = int(distance_fraction_hex, 16)

        return distance_integer + distance_fraction / 100

    def get_calorie(self) -> int:
        if not self.is_valid():
            return 0

        calorie_hex = self.message[14: 14 + 4]
        return int(calorie_hex, 16)

    def get_speed(self) -> float:
        if not self.is_valid():
            return 0.0

        speed_integer_hex = self.message[18: 18 + 2]
        speed_integer = int(speed_integer_hex, 16)
        speed_fraction_hex = self.message[20: 20 + 2]
        speed_fraction = int(speed_fraction_hex, 16)
        return speed_integer + speed_fraction / 100

    def get_incline(self) -> int:
        if not self.is_valid():
            return 0
        incline_hex = self.message[22: 22 + 2]
        return int(incline_hex, 16)

    def get_pulse(self) -> int:
        if not self.is_valid():
            return 0
        pulse_hex = self.message[24: 24 + 2]
        return int(pulse_hex, 16)

    def __str__(self):
        return json.dumps({
            self.__class__.__name__: {
                "message": self.message,
                "time": self.get_time(),
                "distance": self.get_distance(),
                "calorie": self.get_distance(),
                "speed": self.get_speed(),
                "incline": self.get_incline(),
                "pulse": self.get_pulse(),
            }
        }, indent=4)

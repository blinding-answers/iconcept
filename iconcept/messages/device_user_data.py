from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram


class DeviceUserData(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        return '550106'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 12

    def is_valid(self) -> bool:
        return self.message is not None

    def get_age(self) -> int:
        if not self.is_valid():
            return 0

        unit_hex = self.message[6: 6 + 2]
        return int(unit_hex, 16)

    def get_is_male(self) -> bool:
        if not self.is_valid():
            return True

        unit_hex = self.message[8: 8 + 2]
        return int(unit_hex, 16) == 0

    def get_weight(self) -> float:
        if not self.is_valid():
            return 0

        weight_left = int(self.message[10: 10 + 2], 16)  # left
        weight_right = int(self.message[12: 12 + 2], 16) / 100  # right

        if self.get_is_metric():
            weight = weight_left + weight_right
        else:
            weight = self.kg_to_pound(weight_left + weight_right)

        return round(weight, 2)

    def get_height(self) -> float:
        if not self.is_valid():
            return 0

        height_left = int(self.message[14: 14 + 2], 16)  # left
        height_right = int(self.message[16: 16 + 2], 16) / 100  # right

        if self.get_is_metric():
            height = height_left + height_right
        else:
            height = self.cm_to_inch(height_left + height_right)

        return round(height, 2)

    def get_is_metric(self):
        if not self.is_valid():
            return 0

        unit_hex = self.message[14: 14 + 2]
        return int(unit_hex, 16)

    def cm_to_inch(self, cm: float) -> float:
        return cm * 0.3937

    def kg_to_pound(self, kg: float) -> float:
        return kg * 2.20462

    def __str__(self):
        return " ".join([
            self.__class__.__name__,
            "(",
            "message =", self.message,
            "age =", str(self.get_age()),
            "isMale =", "Yes" if self.get_is_male() else "No",
            "weight =", str(self.get_weight()),
            "height =", str(self.get_height()),
            "isMetric =", "Yes" if self.get_is_metric() else "No",
            ")"
        ])

from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram


class DeviceFeedback(AbstractDatagram):

    def __init__(self, message: str):
        self.message = extract_datagram(message, self.get_header_pattern(), self.get_total_length())

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

    '''
                bptr += 3;
            ByteBuffer bb = ByteBuffer.wrap(buffer, bptr, 10);
            
            FitnessHwApiDeviceFeedback statistic = new FitnessHwApiDeviceFeedback();
            
            start 6
            statistic.time = bb.getShort(); //2bytes = 4 positions
            start 6+4=10
            byte distanceX = bb.get(); // 1 byte = 2 positions
            start 10+2=12
            byte distanceY = bb.get();// 1 byte = 2 positions
            start 12+2=14
            statistic.calorie = bb.getShort();//2bytes = 4 positions
            start 14+4=18
            byte speedX = bb.get();// 1 byte = 2 positions
            start 18+2=20
            byte speedY = bb.get();// 1 byte = 2 positions
            start 20+2=22
            statistic.incline = bb.get();// 1 byte = 2 positions
            start 22+2=24
            statistic.pulse = bb.get() & 0xFF; // 1 byte = 2 positions
            
            statistic.distance = (distanceX & 0xFF) + 1.0D * distanceY / 100.0D;
            statistic.speed = (speedX & 0xFF) + 1.0D * speedY / 100.0D;
            
            FitnessHwApiDevice.this.notifyDeviceUpdate(statistic);
    '''

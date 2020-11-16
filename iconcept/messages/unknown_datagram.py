from iconcept.message_extractor import extract_datagram
from iconcept.messages.abstract_datagram import AbstractDatagram
import json


class UnknownMessage1(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55C002 24E1
        # 55C002 25E1
        # 55C002 26E1
        # 55C002 06C2
        # 55C002 A0E1
        # 55C002 B0C2
        # 55C002 B2C2
        # 55C002 B3C2
        # 55C002 B4C2
        # 55C002 B9C2
        # 55C002 BAC2
        # 55C002 18C2
        # 55C002 19C2
        # 55C002 1AC2
        # 55C002 1BC2
        # 55C002 18E1
        # 55C002 19E1
        # 55C002 1AE1
        # 55C002 1BC2
        # 55C002 18E1
        # 55C002 19E1
        # 55C002 1AE1
        return '55C002'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 4

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage2(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55270101
        return '552701'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 2

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage3(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55020100
        return '550201'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 2

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage4(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55030100
        return '550301'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 2

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage5(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55040204E1
        return '550402'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 4

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage6(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 550602005A
        return '550602'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 4

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage7(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 551F0416000100
        return '551F04'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 8

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage8(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55B0023234

        return '55B002'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 4

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage9(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55B208 544D30314B322020

        return '55B208'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 16

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage10(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55B308544D303120202020 (TM01    )
        return '55B308'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 16

    def is_valid(self) -> bool:
        return self.message is not None

    def __extract_data(self):
        start = self.get_header_length()
        end = start + self.get_message_length()
        hex_string = self.message[start:end]
        return hex_string

    def __str__(self):
        return f"{self.__class__.__name__}:{bytearray.fromhex(self.__extract_data()).decode()}"


class UnknownMessage11(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55B40C 313230374D20202020202020(1207M       )
        return '55B40C'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 24

    def is_valid(self) -> bool:
        return self.message is not None

    def __extract_data(self):
        start = self.get_header_length()
        end = start + self.get_message_length()
        hex_string = self.message[start:end]
        return hex_string

    def __str__(self):
        return f"{self.__class__.__name__}:{bytearray.fromhex(self.__extract_data()).decode()}"


class UnknownMessage12(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55B508 0000000000000000
        return '55B508'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 16

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage13(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55B60A 00000000000000000000
        return '55B60A'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 20

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage14(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55B708 0000000000000000
        return '55B708'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 16

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage15(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55B80A 00000000000000000000
        return '55B80A'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 20

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage18(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 550B0101
        return '550B01'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 2

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage19(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 551805 000003082F
        return '551805'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 10

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage20(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 55190400001849
        return '551904'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 8

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage21(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 551A04 00000752
        return '551A04'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 8

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage22(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 551B01B9
        return '551B01'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 2

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"


class UnknownMessage23(AbstractDatagram):
    message: str = None

    def ingest_data(self, data: str) -> None:
        self.message = extract_datagram(data, self.get_header_pattern(), self.get_total_length())

    def get_header_pattern(self) -> str:
        # 551E0101
        return '551E01'

    def get_header_length(self) -> int:
        return 6

    def get_message_length(self) -> int:
        return 2

    def is_valid(self) -> bool:
        return self.message is not None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"

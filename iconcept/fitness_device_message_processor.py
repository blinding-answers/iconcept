from iconcept.messages.device_status import DeviceStatus
from iconcept.messages.device_unit import DeviceUnit
from iconcept.messages.device_type import DeviceType
from iconcept.messages.device_feedback import DeviceFeedback
from iconcept.messages.abstract_datagram import AbstractDatagram
from iconcept.exceptions.unknown_datagram import UnknownDatagram
from typing import Generator, List, Union


class FitnessDeviceMessageProcessor:

    def __init__(self, datagrams: Union[List[AbstractDatagram], None] = None):
        if datagrams:
            self.__datagrams = datagrams
        else:
            self.__datagrams = [
                DeviceStatus(),
                DeviceUnit(),
                DeviceType(),
                DeviceFeedback()
            ]

    def get_datagrams(self, data: str) -> List[Union[None, AbstractDatagram]]:
        datagrams = []
        position = 0
        while position < len(data):
            data_section = data[position:]
            for datagram in self.__datagrams:
                if data_section.startswith(datagram.get_header_pattern()):
                    datagram.ingest_data(data_section)
                    if datagram.is_valid():
                        datagrams.append(datagram)
                        position += datagram.get_total_length()
                        break

            else:
                raise UnknownDatagram(f'Unknown datagram starting with {data[position:position + 6]}')
        return datagrams

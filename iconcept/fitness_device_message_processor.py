from iconcept.messages.device_status import DeviceStatus
from iconcept.messages.device_unit import DeviceUnit
from iconcept.messages.device_type import DeviceType
from iconcept.messages.device_feedback import DeviceFeedback
from iconcept.messages.device_manufacturer import DeviceManufacturer
from iconcept.messages.device_model import DeviceModel
from iconcept.messages.abstract_datagram import AbstractDatagram
from iconcept.exceptions.unknown_datagram import UnknownDatagram
from iconcept.messages.unknown_datagram import UnknownMessage1, UnknownMessage2, UnknownMessage3, UnknownMessage4, \
    UnknownMessage5, UnknownMessage6, UnknownMessage7, UnknownMessage8, UnknownMessage9, UnknownMessage10, \
    UnknownMessage11, UnknownMessage12, UnknownMessage13, UnknownMessage14, UnknownMessage15, \
    UnknownMessage18, UnknownMessage19, UnknownMessage20, UnknownMessage21, UnknownMessage22, \
    UnknownMessage23
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
                DeviceFeedback(),
                DeviceManufacturer(),
                DeviceModel(),
                UnknownMessage1(),
                UnknownMessage2(),
                UnknownMessage3(),
                UnknownMessage4(),
                UnknownMessage5(),
                UnknownMessage6(),
                UnknownMessage7(),
                UnknownMessage8(),
                UnknownMessage9(),
                UnknownMessage10(),
                UnknownMessage11(),
                UnknownMessage12(),
                UnknownMessage13(),
                UnknownMessage14(),
                UnknownMessage15(),

                UnknownMessage18(),
                UnknownMessage19(),
                UnknownMessage20(),
                UnknownMessage21(),
                UnknownMessage22(),
                UnknownMessage23(),
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
                raise UnknownDatagram(f'Unknown datagram starting with {data[position:]}')
        return datagrams

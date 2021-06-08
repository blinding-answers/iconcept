from iconcept.messages.device_status import DeviceStatus
from iconcept.messages.device_unit import DeviceUnit
from iconcept.messages.device_type import DeviceType
from iconcept.messages.device_feedback import DeviceFeedback
from iconcept.messages.device_manufacturer import DeviceManufacturer
from iconcept.messages.device_model import DeviceModel
from iconcept.messages.device_stop import DeviceStop
from iconcept.messages.device_pulse_type import DevicePulseType
from iconcept.messages.abstract_datagram import AbstractDatagram
from iconcept.exceptions.unknown_datagram_exception import UnknownDatagramException
from iconcept.messages.unknown_datagram import UnknownMessage1, UnknownMessage2, UnknownMessage3, UnknownMessage4, \
    UnknownMessage5, UnknownMessage6, UnknownMessage7, UnknownMessage8, UnknownMessage9, UnknownMessage10, \
    UnknownMessage11, UnknownMessage12, UnknownMessage13, UnknownMessage14, UnknownMessage15, \
    UnknownMessage19, UnknownMessage20, UnknownMessage21, UnknownMessage22, \
    UnknownMessage23, UnknownMessage24
from typing import Generator, List, Union
import copy


class FitnessDeviceMessageProcessor:
    data_carry_over: str = ''

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
                DeviceStop(),
                DevicePulseType(),
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
                UnknownMessage19(),
                UnknownMessage20(),
                UnknownMessage21(),
                UnknownMessage22(),
                UnknownMessage23(),
                UnknownMessage24(),
            ]

    def get_datagrams(self, data: str) -> List[Union[None, AbstractDatagram]]:
        datagrams = []
        position = 0
        data = ''.join([self.data_carry_over, data])
        while position < len(data):
            data_section = data[position:]
            for datagram in self.__datagrams:
                if data_section.startswith(datagram.get_header_pattern()):
                    datagram.ingest_data(data_section)
                    if datagram.is_valid():
                        datagrams.append(copy.copy(datagram))
                        position += datagram.get_total_length()
                        break
                    if datagram.get_total_length() < len(data_section):
                        # last part probably incomplete and need aditional packets..
                        self.data_carry_over = data_section
                        break

            else:
                raise UnknownDatagramException(f'Unknown datagram starting with {data[position:]}')
        return datagrams

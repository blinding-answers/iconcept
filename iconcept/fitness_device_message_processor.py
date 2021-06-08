from iconcept.messages.device_init_2 import DeviceInit2
from iconcept.messages.device_init_3 import DeviceInit3
from iconcept.messages.device_init_4 import DeviceInit4
from iconcept.messages.device_init_5 import DeviceInit5
from iconcept.messages.device_init_6 import DeviceInit6
from iconcept.messages.device_init_7 import DeviceInit7
from iconcept.messages.device_init_8 import DeviceInit8
from iconcept.messages.device_init_9 import DeviceInit9
from iconcept.messages.device_init_10 import DeviceInit10
from iconcept.messages.device_init_11 import DeviceInit11
from iconcept.messages.device_init_12 import DeviceInit12
from iconcept.messages.device_init_13 import DeviceInit13
from iconcept.messages.device_init_14 import DeviceInit14
from iconcept.messages.device_init_15 import DeviceInit15
from iconcept.messages.device_init_16 import DeviceInit16
from iconcept.messages.device_init_17 import DeviceInit17
from iconcept.messages.device_init_18 import DeviceInit18
from iconcept.messages.device_init_19 import DeviceInit19
from iconcept.messages.device_init_20 import DeviceInit20
from iconcept.messages.device_init_21 import DeviceInit21
from iconcept.messages.device_init_22 import DeviceInit22
from iconcept.messages.device_init_24 import DeviceInit24
from iconcept.messages.device_init_25 import DeviceInit25
from iconcept.messages.device_init_26 import DeviceInit26
from iconcept.messages.device_init_27 import DeviceInit27
from iconcept.messages.device_keep_alive import DeviceKeepAlive

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
from iconcept.messages.unknown_datagram import UnknownMessage1, \
    UnknownMessage5, UnknownMessage6, UnknownMessage7, UnknownMessage8, UnknownMessage9, UnknownMessage10, \
    UnknownMessage11, UnknownMessage12, UnknownMessage13, UnknownMessage14, UnknownMessage15, \
    UnknownMessage19, UnknownMessage20, UnknownMessage21, \
    UnknownMessage23, UnknownMessage24, UnknownMessage25, UnknownMessage27, UnknownMessage28, \
    UnknownMessage29, UnknownMessage30, UnknownMessage31
from typing import Generator, List, Union
import copy

from sniffer.rfcomm_packet import RfcommPacket


class FitnessDeviceMessageProcessor:
    data_carry_over: str = ''

    def __init__(self, datagrams: Union[List[AbstractDatagram], None] = None):
        if datagrams:
            self.__datagrams = datagrams
        else:
            self.__datagrams = [

                DeviceInit2(),
                DeviceInit3(),
                DeviceInit4(),
                DeviceInit5(),
                DeviceInit6(),
                DeviceInit7(),
                DeviceInit8(),
                DeviceInit9(),
                DeviceInit10(),
                DeviceInit11(),
                DeviceInit12(),
                DeviceInit13(),
                DeviceInit14(),
                DeviceInit15(),
                DeviceInit16(),
                DeviceInit17(),
                DeviceInit18(),
                DeviceInit19(),
                DeviceInit20(),
                DeviceInit21(),
                DeviceInit22(),
                DeviceInit24(),
                DeviceInit25(),
                DeviceInit26(),
                DeviceInit27(),

                DeviceStatus(),
                DeviceUnit(),
                DeviceType(),
                DeviceFeedback(),
                DeviceManufacturer(),
                DeviceModel(),
                DeviceStop(),
                DevicePulseType(),
                UnknownMessage1(),

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
                UnknownMessage23(),
                UnknownMessage24(),
                UnknownMessage25(),
                UnknownMessage27(),
                UnknownMessage28(),
                UnknownMessage29(),
                UnknownMessage30(),
                UnknownMessage31(),
                DeviceKeepAlive()
            ]

    def get_datagrams(self, rfcomm_packet: RfcommPacket) -> List[Union[None, AbstractDatagram]]:
        datagrams = []
        position = 0

        data = ''.join([self.data_carry_over, rfcomm_packet.data.as_hex()])
        while position < len(data):
            data_section = data[position:]
            for datagram in self.__datagrams:
                if data_section.startswith(datagram.get_header_pattern()):
                    datagram.ingest_data(data_section)
                    if datagram.is_valid():
                        datagrams.append(copy.copy(datagram))
                        position += datagram.get_total_length()
                        break
                    if datagram.get_total_length() > len(data_section):
                        # last part probably incomplete and need aditional packets..
                        self.data_carry_over = data_section
                        break

            else:
                raise UnknownDatagramException(f'Unknown datagram starting with {data[position:]}')
        return datagrams

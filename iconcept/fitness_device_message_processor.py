from iconcept.messages.device_type import DeviceType
from iconcept.messages.device_init_1 import DeviceInit1
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
from iconcept.messages.device_init_23 import DeviceInit23
from iconcept.messages.device_init_24 import DeviceInit24
from iconcept.messages.device_init_25 import DeviceInit25
from iconcept.messages.device_init_26 import DeviceInit26
from iconcept.messages.device_init_27 import DeviceInit27
from iconcept.messages.device_keep_alive import DeviceKeepAlive
from iconcept.messages.device_keep_alive_response import DeviceKeepAliveResponse
from iconcept.messages.device_enable_start_key import DeviceEnableStartKey
from iconcept.messages.device_reset_command import DeviceResetCommand
from iconcept.messages.device_start_command import DeviceStartCommand
from iconcept.messages.device_stop_command import DeviceStopCommand
from iconcept.messages.device_manufacturer import DeviceManufacturer
from iconcept.messages.device_target_speed_command import DeviceTargetSpeedCommand
from iconcept.messages.device_user_data import DeviceUserData

from iconcept.messages.device_status import DeviceStatus
from iconcept.messages.device_unit import DeviceUnit
from iconcept.messages.device_type import DeviceType
from iconcept.messages.device_feedback import DeviceFeedback
from iconcept.messages.device_brand import DeviceBrand
from iconcept.messages.device_machine_type import DeviceMachineType
from iconcept.messages.device_stop import DeviceStop
from iconcept.messages.device_pulse_type_query import DevicePulseTypeQuery
from iconcept.messages.abstract_datagram import AbstractDatagram
from iconcept.exceptions.unknown_datagram_exception import UnknownDatagramException
from iconcept.messages.unknown_datagram import UnknownMessage1, \
    UnknownMessage5, UnknownMessage6, UnknownMessage7, UnknownMessage8, UnknownMessage9, UnknownMessage10, \
    UnknownMessage12, UnknownMessage13, UnknownMessage14, UnknownMessage15, \
    UnknownMessage19, UnknownMessage20, UnknownMessage21, \
    UnknownMessage25, \
    UnknownMessage29, UnknownMessage30, UnknownMessage31, UnknownMessage32, UnknownMessage33
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
                DeviceInit1(),
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
                DeviceInit23(),
                DeviceInit24(),
                DeviceInit25(),
                DeviceInit26(),
                DeviceInit27(),

                DeviceStatus(),
                DeviceUnit(),
                DeviceType(),
                DeviceFeedback(),
                DeviceBrand(),
                DeviceMachineType(),
                DeviceStop(),
                DevicePulseTypeQuery(),
                UnknownMessage1(),

                UnknownMessage5(),
                UnknownMessage6(),
                UnknownMessage7(),
                UnknownMessage8(),
                UnknownMessage9(),
                UnknownMessage10(),
                UnknownMessage12(),
                UnknownMessage13(),
                UnknownMessage14(),
                UnknownMessage15(),
                UnknownMessage19(),
                UnknownMessage20(),
                UnknownMessage21(),
                UnknownMessage25(),
                UnknownMessage29(),
                UnknownMessage30(),
                UnknownMessage31(),
                UnknownMessage32(),
                UnknownMessage33(),

                DeviceKeepAlive(),
                DeviceEnableStartKey(),
                DeviceKeepAliveResponse(),
                DeviceType(),
                DeviceResetCommand(),
                DeviceStartCommand(),
                DeviceStopCommand(),
                DeviceManufacturer(),
                DeviceTargetSpeedCommand(),
                DeviceUserData(),
            ]

    def get_datagrams(self, rfcomm_packet: RfcommPacket) -> List[Union[None, AbstractDatagram]]:
        datagrams = []
        position = 0
        was_last_section = False

        data = ''.join([self.data_carry_over, rfcomm_packet.data.as_hex()])
        self.data_carry_over = ''
        while position < len(data) and not was_last_section:
            data_section = data[position:]
            for datagram in self.__datagrams:
                if data_section.startswith(datagram.get_header_pattern()):
                    datagram.ingest_data(data_section)
                    if datagram.is_valid():
                        datagrams.append(copy.copy(datagram))
                        position += datagram.get_total_length()
                        break
                    if datagram.get_total_length() > len(data_section):
                        # last part probably incomplete and need additional packets..
                        self.data_carry_over = data_section
                        was_last_section = True
                        break

            else:
                raise UnknownDatagramException(f'Unknown datagram starting with {data[position:]}')

        return datagrams

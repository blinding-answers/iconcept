from iconcept.contracts.abstract_channel import AbstractChannel
from iconcept.util.hex_conversion import integer_to_hex_string
import logging

logger = logging.getLogger(__name__)


class FitnessDeviceCommander:

    def __init__(self, channel: AbstractChannel):
        self.channel = channel

    def init(self):
        logger.debug("INIT")
        commands = [
            "550C01FF",
            "55BB01FF",
            "552401FF",
            "552501FF",
            "552601FF",
            "552701FF",
            "550201FF",
            "550301FF",
            "550401FF",
            "550601FF",
            "551F01FF",
            "55A001FF",
            "55B001FF",
            "55B201FF",
            "55B301FF",
            "55B401FF",
            "55B501FF",
            "55B601FF",
            "55B701FF",
            "55B801FF",
            "55B901FF",
            "55BA01FF",
            "550B01FF",
            "551801FF",
            "551901FF",
            "551A01FF",
            "551B01FF",
        ]

        self.channel.send(''.join(commands))

    def reset(self):
        logger.debug("RESET")
        # COMMAND_RESET = [85, 10, 1, 2]  # 550a0102
        command = "550A0102"
        self.channel.send(command)

    def start(self):
        logger.debug("START")
        # COMMAND_START = [85, 10, 1, 1]  # 550a0101
        command = "550A0101"
        self.channel.send(command)

    def pause(self):
        logger.debug("PAUSE")
        # COMMAND_PAUSE = [85, 10, 1]  # 550a01
        command = "550A0100"
        self.channel.send(command)

    def stop(self):
        logger.debug("STOP")
        # COMMAND_STOP = [85, 10, 1, 3]  # 550a0103
        command = "550A0103"
        self.channel.send(command)

    def enable_start_key(self):
        logger.debug("ENABLE START KEY")
        # COMMAND_ENABLE_START_KEY = [85, 8, 1, 1]  # 55080101
        command = "55080101"
        self.channel.send(command)

    def set_speed(self, speed: float):
        logger.debug(f"SET TARGET SPEED: {speed}")
        speed = float(speed)
        # byte[] command = { 85, 15, 2, speedByte1, speedByte2 };
        speed_integer = int(speed)
        speed_integer_hex = integer_to_hex_string(speed_integer)
        speed_fractional = int((speed * 100) - int(speed) * 100)
        speed_fractional_hex = integer_to_hex_string(speed_fractional)

        command = f"552102{speed_integer_hex}{speed_fractional_hex}"
        self.channel.send(command)

    def set_incline(self, incline: int):
        logger.debug(f"SET INCLINE: {incline}")
        incline_hex = integer_to_hex_string(incline)

        command = f"551101{incline_hex}"
        self.channel.send(command)

    def set_action_mode(self, mode: int):
        logger.debug(f"SET ACTION MODE: {mode}")
        mode_hex = integer_to_hex_string(mode)
        command = f"551501{mode_hex}"  # 551501
        self.channel.send(command)

    def query_manufacturer(self):
        logger.debug("QUERY MANUFACTURER")
        # COMMAND_QUERY_MANUFACTURER = [85, -75, 1, -1]  # 55b401ff
        command = "55B401FF"
        self.channel.send(command)

    def query_pulse_type(self):
        # 550701ff
        logger.debug("QUERY PULSE TYPE")
        # COMMAND_QUERY_PULSE_TYPE = [85, 7, 1, -1]  # 550701ff
        command = "550701FF"
        self.channel.send(command)

    def keep_alive(self, keep_alive: bool):
        logger.debug("KEEP ALIVE")
        # COMMAND_KEEP_ALIVE = [85, 23, 1]  # 551701
        if keep_alive:
            key = 1
        else:
            key = 0
        key_hex = integer_to_hex_string(key)
        command = f"551701{key_hex}"
        self.channel.send(command)

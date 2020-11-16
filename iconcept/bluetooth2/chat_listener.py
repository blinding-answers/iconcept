import logging

from iconcept.bluetooth.chat_listener_abc import ChatListenerABC

logger = logging.getLogger(__name__)

from multiprocessing.managers import BaseProxy
from iconcept import FitnessDeviceFeedback
from iconcept import UnitUtil


class ChatListener(ChatListenerABC):
    def __init__(self, device):
        self.device = device

    def on_connect_success(self, param_string: str):
        logger.debug(f"on_connect_success: {param_string}")
        self.device.init_device()

        # init device
        # FitnessHwApiDevice.this.mDeviceName = name;
        # FitnessHwApiDevice.this.initRemoteDevice();
        # FitnessHwApiDevice.this.startKeepAlive();
        pass

    def on_connect_failed(self, exception: Exception):
        logger.debug(f"on_connect_failed")
        #  FitnessHwApiDevice.this.notifyDeviceConnectFailed();
        logger.exception(exception)
        raise exception

    def on_connect_lost(self):
        # FitnessHwApiDevice.this.stopKeepAlive();
        # FitnessHwApiDevice.this.notifyDeviceDisconnected();
        logger.debug(f"on_connect_lost")
        pass

    def on_data_read(self, data: bytes):
        # all the magic happens here
        message = str(data.hex()).upper()
        logger.debug(f"on_data_read HEX: {message}")
        # Play by play from java class

        code1 = "550D"
        # e.g 550D0A00000000000000000000
        # Always zero ??
        if code1 in message:
            ptr = message.index(code1)
            header_size = 6
            message_size = 20
            len1 = len(message)
            bb = None
            if len1 >= (ptr + message_size + header_size):
                ptr += header_size
                bb = message[ptr: ptr + message_size]
                statistic = FitnessDeviceFeedback(bb)

                # notify device change

        code2 = "551D"
        # update self and simulator ?
        if code2 in message:
            ptr = message.index(code2)
            header_size = 6
            message_size = 20
            len1 = len(message)
            bb = None
            if len1 >= (ptr + message_size + header_size):
                ptr += header_size
                bb = message[ptr: ptr + message_size]
                statistic = FitnessDeviceFeedback(bb)
                self.device.set_speed(statistic.speed)
                self.device.set_incline(statistic.incline)
                self.device.set_pule(statistic.pulse)

        # device unit
        code3 = "550C01"
        if code3 in message:
            ptr = message.index(code3)
            header_size = 6
            message_size = 2
            bb = None
            len1 = len(message)
            if len1 >= (ptr + message_size + header_size):
                ptr += header_size
                bb = message[ptr: ptr + message_size]
                logger.debug(f"Set set_device_unit {int(bb)}")
                self.device.device_unit = int(bb)
                pass

        code4 = "55BB01"
        if code4 in message:
            ptr = message.index(code4)
            header_size = 6
            message_size = 2
            len1 = len(message)
            bb = None
            if len1 >= (ptr + message_size + header_size):
                ptr += header_size
                bb = message[ptr: ptr + message_size]
                logger.debug(f"Set set_device_type {bb}")
                self.device.device_type = bb
                logger.debug(f"Set set_device_status 'STANDBY'")
                self.device.device_status = self.devive.DEVICE_STATUS_STANDBY
                # TODO
                logger.debug(f"Notify device connection 'Treadmill'")

        # device ready and connected
        code5 = "551F04"
        if code5 in message:
            ptr = message.index(code5)
            header_size = 6
            message_size = 8
            len1 = len(message)
            bb = None
            if len1 >= (ptr + message_size + header_size):
                ptr += header_size
                bb = message[ptr: ptr + message_size]
                speed_limit_array = [bb[i: i + 2] for i in range(0, len(bb), 2)]

                max_speed = speed_limit_array[0]
                max_speed_decimal = speed_limit_array[1]
                min_speed = speed_limit_array[2]
                min_speed_decimal = speed_limit_array[3]

                logger.debug(f"max_speed:{max_speed}")

                # TODO
                # if not self.device.is_metric then convert to metric
                # speed_limit
                # self.device.set_device_status("STANDBY")
                # self.device.notify_device_connected(self.device.name)
                logger.debug(f"Set set_device_type {bb}")
                self.device.device_type = bb
                logger.debug(f"Set set_device_status 'STANDBY'")
                self.device.device_status = self.device.DEVICE_STATUS_STANDBY
                # TODO
                logger.debug(f"Notify device connected 'Treadmill'")

        # After INIT..
        # 55BA144455414C4B495420545245414420202020202020
        # Device Name
        code6 = "55BA14"
        if code6 in message:
            ptr = message.index(code6)
            header_size = 6
            message_size = 20
            len1 = len(message)
            bb = None
            if len1 >= (ptr + message_size + header_size):
                ptr += header_size
                bb = message[ptr: ptr + message_size]
                # device_name=str(bytes.fromhex(message).decode('utf8')).strip()
                # self.device.device_name=device_name
                # pass

            code7 = "55B914"
            if code7 in message:
                ptr = message.index(code6)
                header_size = 6
                message_size = 28
                len1 = len(message)
                bb = None
                if len1 >= (ptr + message_size + header_size):
                    ptr += header_size
                    bb = message[ptr: ptr + message_size]
            # if (i != -1) {
            #   String str1 = (new String(param1ArrayOfbyte, i / 2 + 3, 14)).replaceAll("[^\\x20-\\x7f]", "").toUpperCase(Locale.US).trim();
            #   Log.d("Trace", "brand=" + str1 + "(eof)");
            #   FitnessHwApiDevice.this.notifyBrand(str1);
            # }

    def on_data_write(self, param_bytes: bytes):

        logger.debug(f"on_data_write: {param_bytes}")
        # logger.debug(f"on_data_write: string {repr(parram_bytes.decode('utf-8'))}")
        # logger.debug(f"on_data_write:HEX  {parram_bytes.hex().upper()}")
        pass

    def on_state_changed(self, param_int: int):
        logger.debug(f"on_state_changed: {param_int}")
        self.device.connection_state = param_int

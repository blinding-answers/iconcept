from iconcept.contracts.abstract_channel import AbstractChannel
import logging

logger = logging.getLogger(__name__)


class Channel(AbstractChannel):
    def __init__(self, socket):
        self.socket = socket

    def send(self, command: str):
        logger.debug(f"Sending {command}")
        bin_data = bytes.fromhex(command)
        self.socket.send(bin_data)

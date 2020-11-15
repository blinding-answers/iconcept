from iconcept.contracts.abstract_channel import AbstractChannel


class Channel(AbstractChannel):
    def __init__(self):
        self.last_command = None

    def send(self, command: str):
        self.last_command = command

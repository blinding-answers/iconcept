import unittest
from iconcept import FitnessDevice
from iconcept.bluetooth import ChatListener
from . import FakeQueue



class test_chat_listener(unittest.TestCase):
    def setUp(self):
        queue=FakeQueue()
        self.device=FitnessDevice(command_q=queue)
        self.chat_listener=ChatListener(device=self.device)
import unittest
from iconcept.fitness_device_message_processor import FitnessDeviceMessageProcessor
from iconcept.messages.abstract_datagram import AbstractDatagram
from .fakes.fake_datagram import FakeDatagram


class FitnessDeviceMessageProcessorTest(unittest.TestCase):
    def create_datagram(self, header_pattern, header_length, message_length):
        return FakeDatagram(header_pattern=header_pattern, header_length=header_length, message_length=message_length)

    def test_process(self):
        fake_datagram1 = self.create_datagram('abd', 3, 2)
        fake_datagram2 = self.create_datagram('cde', 3, 2)

        self.assertEqual('abd', fake_datagram1.get_header_pattern())
        processor = FitnessDeviceMessageProcessor(
            [
                fake_datagram1,
                fake_datagram2
            ]
        )
        data_for_datagram1 = 'abdcd'
        data_for_datagram2 = 'cde12'
        datagrams1 = processor.get_datagrams(''.join([data_for_datagram1, data_for_datagram2]))
        self.assertEqual([fake_datagram1, fake_datagram2], datagrams1)

        datagrams2 = processor.get_datagrams(''.join([data_for_datagram2, data_for_datagram1]))
        self.assertEqual([fake_datagram2, fake_datagram1], datagrams2)


if __name__ == '__main__':
    unittest.main()

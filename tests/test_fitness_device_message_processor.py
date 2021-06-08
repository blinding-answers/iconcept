import unittest
from iconcept.fitness_device_message_processor import FitnessDeviceMessageProcessor
from .fakes.fake_datagram import FakeDatagram
from iconcept.exceptions.unknown_datagram_exception import UnknownDatagramException


class FitnessDeviceMessageProcessorTest(unittest.TestCase):
    def create_datagram(self, header_pattern, header_length, message_length):
        return FakeDatagram(header_pattern=header_pattern, header_length=header_length, message_length=message_length)

    def test_process_with_valid_data(self):
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
        self.assertEqual(fake_datagram1.get_header_pattern(), datagrams1[0].get_header_pattern())
        self.assertEqual(fake_datagram2.get_header_pattern(), datagrams1[1].get_header_pattern())

        datagrams2 = processor.get_datagrams(''.join([data_for_datagram2, data_for_datagram1]))

        self.assertEqual(fake_datagram2.get_header_pattern(), datagrams2[0].get_header_pattern())
        self.assertEqual(fake_datagram1.get_header_pattern(), datagrams2[1].get_header_pattern())

    def test_process_throws_exception_with_invalid_data(self):
        fake_datagram = self.create_datagram('abd', 3, 2)

        self.assertEqual('abd', fake_datagram.get_header_pattern())
        processor = FitnessDeviceMessageProcessor(
            [
                fake_datagram,
            ]
        )
        data_for_datagram = 'abc'
        with self.assertRaises(UnknownDatagramException):
            processor.get_datagrams(''.join([data_for_datagram]))

        data_for_datagram = 'abde'
        with self.assertRaises(UnknownDatagramException):
            processor.get_datagrams(''.join([data_for_datagram]))


if __name__ == '__main__':
    unittest.main()

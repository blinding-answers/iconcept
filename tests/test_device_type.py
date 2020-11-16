import unittest
from iconcept.messages.device_type import DeviceType
from iconcept.exceptions.invalid_datagram_exception import InvalidDatagramException


class DeviceTypeTest(unittest.TestCase):

    def test_is_valid_with_valid_datagram_is_true(self):
        datagram = "55bb0102"
        device_type = DeviceType()
        device_type.ingest_data(datagram)
        self.assertTrue(device_type.is_valid())

    def test_is_valid_with_invalid_datagram_is_false(self):
        datagram = "invalid"
        device_type = DeviceType()
        device_type.ingest_data(datagram)

        self.assertFalse(device_type.is_valid())

    def test_get_type_gives_valid_values_with_valid_datagram(self):
        datagram = "55bb0101"
        device_type = DeviceType()
        device_type.ingest_data(datagram)

        self.assertEqual(1, device_type.get_type())

        datagram = "55bb0102"
        device_type = DeviceType()
        device_type.ingest_data(datagram)

        self.assertEqual(2, device_type.get_type())

        datagram = "55bb0103"
        device_type = DeviceType()
        device_type.ingest_data(datagram)

        self.assertEqual(3, device_type.get_type())

    def test_get_type_raises_exception_on_invalid_datagram(self):
        datagram = "55bb0104"
        device_type = DeviceType()
        device_type.ingest_data(datagram)
        with self.assertRaises(InvalidDatagramException):
            device_type.get_type()

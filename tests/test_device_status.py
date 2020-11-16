import unittest
from iconcept.messages.device_status import DeviceStatus
from iconcept.exceptions.invalid_datagram import InvalidDatagram


class DeviceStatusTest(unittest.TestCase):

    def test_is_valid_with_valid_datagram_is_true(self):
        datagram = "55090101"

        device_status = DeviceStatus()
        device_status.ingest_data(datagram)
        self.assertTrue(device_status.is_valid())

    def test_is_valid_with_invalid_datagram_is_false(self):
        datagram = "invalid"
        device_status = DeviceStatus()
        device_status.ingest_data(datagram)
        self.assertFalse(device_status.is_valid())

    def test_get_status_gives_valid_values_with_valid_datagram(self):
        datagram = "55090100"
        device_status = DeviceStatus()
        device_status.ingest_data(datagram)
        self.assertEqual(0, device_status.get_status())

        datagram = "55090101"
        device_status = DeviceStatus()
        device_status.ingest_data(datagram)
        self.assertEqual(1, device_status.get_status())

        datagram = "55090102"
        device_status = DeviceStatus()
        device_status.ingest_data(datagram)
        self.assertEqual(2, device_status.get_status())

    def test_get_status_raises_exception_on_invalid_datagram(self):
        datagram = "55090103"
        device_status = DeviceStatus()
        device_status.ingest_data(datagram)
        with self.assertRaises(InvalidDatagram):
            device_status.get_status()

from iconcept.messages.device_status import DeviceStatus


def test_is_valid_with_valid_datagram_is_true():
    datagram = "55090101"
    device_status = DeviceStatus(datagram)
    assert True == device_status.is_valid()


def test_is_valid_with_invalid_datagram_is_false():
    datagram = "invalid"
    device_status = DeviceStatus(datagram)
    assert False == device_status.is_valid()


def test_get_type_gives_valid_values_with_valid_datagram():
    datagram = "55090100"
    device_status = DeviceStatus(datagram)
    assert 0 == device_status.get_status()

    datagram = "55090101"
    device_status = DeviceStatus(datagram)
    assert 1 == device_status.get_status()

    datagram = "55090102"
    device_status = DeviceStatus(datagram)
    assert 2 == device_status.get_status()

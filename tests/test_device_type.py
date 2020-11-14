from iconcept.messages.device_type import DeviceType


def test_is_valid_with_valid_datagram_is_true():
    datagram = "55bb0102"
    device_type = DeviceType(datagram)
    assert True == device_type.is_valid()


def test_is_valid_with_invalid_datagram_is_false():
    datagram = "invalid"
    device_type = DeviceType(datagram)
    assert False == device_type.is_valid()


def test_get_type_gives_valid_values_with_valid_datagram():
    datagram = "55bb0101"
    device_type = DeviceType(datagram)
    assert 1 == device_type.get_type()

    datagram = "55bb0102"
    device_type = DeviceType(datagram)
    assert 2 == device_type.get_type()


    datagram = "55bb0103"
    device_type = DeviceType(datagram)
    assert 3 == device_type.get_type()


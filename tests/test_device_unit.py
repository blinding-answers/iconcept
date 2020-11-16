from iconcept.messages.device_unit import DeviceUnit


def test_is_valid_with_valid_datagram_is_true():
    datagram = "550c0100"
    device_unit = DeviceUnit()
    device_unit.ingest_data(datagram)

    assert True == device_unit.is_valid()


def test_is_valid_with_invalid_datagram_is_false():
    datagram = "invalid"
    device_unit = DeviceUnit()
    device_unit.ingest_data(datagram)
    assert False == device_unit.is_valid()


def test_get_unit_gives_valid_values_with_valid_datagram():
    datagram = "550c0100"
    device_unit = DeviceUnit()
    device_unit.ingest_data(datagram)
    assert 0 == device_unit.get_unit()

    datagram = "550c0101"
    device_unit = DeviceUnit()
    device_unit.ingest_data(datagram)
    assert 1 == device_unit.get_unit()

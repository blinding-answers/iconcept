from iconcept.messages.device_feedback import DeviceFeedback


def test_is_valid_with_valid_datagram_is_true():
    datagram = "550d0a00000000000000000000"
    device_feedback = DeviceFeedback(datagram)
    assert True == device_feedback.is_valid()


def test_is_valid_with_invalid_datagram_is_false():
    datagram = "invalid"
    device_feedback = DeviceFeedback(datagram)
    assert False == device_feedback.is_valid()


def test_invalid_datagram_give_zeros():
    datagram = "invalid"
    device_feedback = DeviceFeedback(datagram)
    assert 0 == device_feedback.get_time()
    assert float == type(device_feedback.get_distance())
    assert 0.0 == device_feedback.get_distance()
    assert 0 == device_feedback.get_calorie()
    assert float == type(device_feedback.get_speed())
    assert 0.0 == device_feedback.get_speed()
    assert 0 == device_feedback.get_incline()
    assert 0 == device_feedback.get_pulse()


def test_valid_datagram_give_correct_values_all_zeros():
    datagram = "550d0a00000000000000000000"
    device_feedback = DeviceFeedback(datagram)
    assert 0 == device_feedback.get_time()
    assert 0.0 == device_feedback.get_distance()
    assert 0 == device_feedback.get_calorie()
    assert 0.0 == device_feedback.get_speed()
    assert 0 == device_feedback.get_incline()
    assert 0 == device_feedback.get_pulse()

def test_valid_datagram_give_correct_values():
    datagram = "550d0a005511190140111405A0"
    device_feedback = DeviceFeedback(datagram)
    assert 85 == device_feedback.get_time()
    assert 17.25 == device_feedback.get_distance()
    assert 320 == device_feedback.get_calorie()
    assert 17.2 == device_feedback.get_speed()
    assert 5 == device_feedback.get_incline()
    assert 160 == device_feedback.get_pulse()
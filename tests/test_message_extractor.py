from iconcept.message_extractor import extract_datagram


def test_extract_message_with_valid_message():
    header_pattern = "KEY"
    header_length = 5
    message_length = 10
    message = "ASDKEYXX1234567890"
    expected_message = "KEYXX1234567890"
    extracted_message = extract_datagram(message, header_pattern, header_length + message_length)

    assert expected_message == extracted_message


def test_extract_message_with_invalid_message_return_none():
    header_pattern = "KEY"
    header_length = 5
    message_length = 10
    message = "ABC"
    expected_message = None
    extracted_message = extract_datagram(message, header_pattern, header_length + message_length)
    assert expected_message == extracted_message

def test_extract_message_where_header_exists_with_too_short_message_return_none():
    header_pattern = "KEY"
    header_length = 5
    message_length = 10
    message = "ASDKEYXX1234567"
    expected_message = None
    extracted_message = extract_datagram(message, header_pattern, header_length + message_length)
    assert expected_message == extracted_message
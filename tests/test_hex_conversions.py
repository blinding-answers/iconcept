from iconcept.util.hex_conversion import integer_to_hex_string


def test_int_to_hex_string():
    integer = int(17)
    expected_hex_string = '11'

    assert expected_hex_string == integer_to_hex_string(integer)

# def test_hex_string_template:

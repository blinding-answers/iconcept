def test_binary_conversion():
    # COMMAND_START = [85, 10, 1, 1]  # 550a0101
    command_from_int = [85, 10, 1, 1]
    bin_data_from_int = ''.join(map(lambda x: chr(x % 256), command_from_int)).encode('utf-8')
    command_from_hex = "550A0101"
    bin_data_from_hex = bytes.fromhex(command_from_hex)
    assert bin_data_from_int == bin_data_from_hex

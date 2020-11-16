#!/usr/bin/env python

#
# ack = "55170101"
# print(f'ack:{ack}')
# print(bytes.fromhex(ack))
#
# hex_string = "550A0101"
#
# print(bytes.fromhex(hex_string))
#
# s = b"U\027\001\001"
#
# for x in s:
#     print('ord(x)')
#     print(ord(x))
#
# print([ord(c) for c in s])
#

def command_to_binary(command: list):
    return ''.join(map(lambda x: chr(x % 256), command)).encode('utf-8')


def binary_to_hex(command: bytes):
    return command.hex()


def hex_to_binary(command: str):
    return bytes.fromhex(command)


if __name__ == '__main__':
    commands = [
        [85, 12, 1, -1],  # 0
        # [85, -69, 1, -1],  # 1
        # [85, 36, 1, -1],  # 2
        # [85, 37, 1, -1],  # 3
        # [85, 38, 1, -1],  # 4
        # [85, 39, 1, -1],  # 5
        # [85, 2, 1, -1],  # 6
        # [85, 3, 1, -1],  # 7
        # [85, 4, 1, -1],  # 8
        # [85, 6, 1, -1],  # 9
        # [85, 31, 1, -1],  # 10
        # [85, -96, 1, -1],  # 11
        # [85, -80, 1, -1],  # 12
        # [85, -78, 1, -1],  # 13
        # [85, -77, 1, -1],  # 14
        # [85, -76, 1, -1],  # 15
        # [85, -75, 1, -1],  # 16
        # [85, -74, 1, -1],  # 17
        # [85, -73, 1, -1],  # 18
        # [85, -72, 1, -1],  # 19
        # [85, -71, 1, -1],  # 20
        # [85, -70, 1, -1],  # 21
        # [85, 11, 1, -1],  # 22
        # [85, 24, 1, -1],  # 23
        # [85, 25, 1, -1],  # 24
        # [85, 26, 1, -1],  # 25
        # [85, 27, 1, -1],  # 26
    ]
    command_to_send = []
    for command in commands:
        command_to_send += command

    bin = command_to_binary(command_to_send)
    print(bin)
    print(binary_to_hex(bin))

    print('reverse....')
    hex = '551b01ff'

    print(hex_to_binary(hex))

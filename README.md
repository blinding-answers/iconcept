# iConcept pyhton driver
Interface and controle iConcept pafers


# PROTOCOL

    START COMMAND
    DEBUG:iconcept.bluetooth.chat_service:Got command from command_q:[85, 10, 1, 1]
    DEBUG:iconcept.bluetooth.chat_listener:on_data_write: b'U\n\x01\x01'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_write: string 'U\n\x01\x01'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_write:HEX  550A0101

    START RESPONSE
    DEBUG:iconcept.bluetooth.chat_service:Received: b'U\xc0\x02\n\xc2U\xc0\x02\n\xc1'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_read: 55C0020AC255C0020AC1

    RESET COMMAND
    DEBUG:iconcept.bluetooth.chat_service:Got command from command_q:[85, 10, 1, 2]
    DEBUG:iconcept.bluetooth.chat_listener:on_data_write: b'U\n\x01\x02'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_write: string 'U\n\x01\x02'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_write:HEX  550A0102

    RESET RESPONSE
    DEBUG:iconcept.bluetooth.chat_service:Received: b'U\xc0\x02\n\xc2U\xc0\x02\n\xc2U\xc0\x02\n\xc1U\xc0\x02\n\xc1'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_read: 55C0020AC255C0020AC255C0020AC155C0020AC1

    KEEP ALIVE ???
    DEBUG:iconcept.bluetooth.chat_service:Received: b'U\r\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\t\x01\x02U\xc0\x02\n\xc1'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_read: 550D0A00000000000000000000 5509010255C0020AC1
    DEBUG:iconcept.bluetooth.chat_service:Received: b'U\r\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_read: 550D0A00000000000000000000


    What is the ACK Byte ?


    action, command, response
    reset,[85, 10, 1, 2 ],
    start,[85, 10, 1, 1],55C0020AC2 55C0020AC1
    speed(value 5.0), [85, 15, 2, 5, 0], 55C0020FC2 55C0020FC1
    speed(value 5.6), [85, 15, 2, 5, 60], 55C0020FC2 55C0020FC1
    speed(value 7.3), [85, 15, 2, 7, 30], 55C0020FC2 55C0020FC1
    incline(value 4),[85, 17, 1, 4],55C00211C255C00211C1
    incline(value 8),[85, 17, 1, 8],55C00211C255C00211C1

55C0020AC255C0020AC255C0020AC155C0020AC1

# INIT Sequence

    [85, 12, 1, -1],
    [85, -69, 1, -1],
    [85, 36, 1, -1],
    [85, 37, 1, -1],
    [85, 38, 1, -1],
    [85, 39, 1, -1],
    [85, 2, 1, -1],
    [85, 3, 1, -1],
    [85, 4, 1, -1],
    [85, 6, 1, -1],
    [85, 31, 1, -1],
    [85, -96, 1, -1],
    [85, -80, 1, -1],
    [85, -78, 1, -1],
    [85, -77, 1, -1],
    [85, -76, 1, -1],
    [85, -75, 1, -1],
    [85, -74, 1, -1],
    [85, -73, 1, -1],
    [85, -72, 1, -1],
    [85, -71, 1, -1],
    [85, -70, 1, -1],
    [85, 11, 1, -1],
    [85, 24, 1, -1],
    [85, 25, 1, -1],
    [85, 26, 1, -1],
    [85, 27, 1, -1],


## Procol ideas
    col1 85 = Treadmill
    col2 15 = speed
    col2 17 = incline



    #$# = 232423 (hex)

    550C010055C00224E15527010155040204E155B002323455C002B0C255B40C313230374D2020202020202055C002B4C255B708000000000000000055BA144455414C4B49542054524541442020202020202055C002BAC25519040000000055C00219C255C00219E1



    ## Bluetooth proyx server

    sudo setcap 'cap_net_raw,cap_net_admin+eip' `which hcitool`
    sudo setcap 'cap_net_raw,cap_net_admin+eip' `which hciconfig`
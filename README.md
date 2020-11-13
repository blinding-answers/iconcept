# iConcept pyhton driver
Interface and control iConcept pafers

##Idea
Create a workout by reacting to certain conditions.  
Like interval training by time or distance.  
Load a route profile.  (GPX)



# PROTOCOL

Data: 55170101

    START COMMAND
    DEBUG:iconcept.bluetooth.chat_service:Got command from command_q:[85, 10, 1, 1] //start
    DEBUG:iconcept.bluetooth.chat_listener:on_data_write: b'U\n\x01\x01'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_write: string 'U\n\x01\x01'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_write:HEX  550A0101

    START RESPONSE
    DEBUG:iconcept.bluetooth.chat_service:Received: b'U\xc0\x02\n\xc2U\xc0\x02\n\xc1'
    DEBUG:iconcept.bluetooth.chat_listener:on_data_read: 55C0020AC255C0020AC1

    RESET COMMAND
    DEBUG:iconcept.bluetooth.chat_service:Got command from command_q:[85, 10, 1, 2] //reset
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

551e0101 550d0a00000000000000000000


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

    550C0100 55C00224E15527010155040204E155B002323455C002B0C255B40C313230374D2020202020202055C002B4C255B708000000000000000055BA144455414C4B49542054524541442020202020202055C002BAC25519040000000055C00219C255C00219E1



## Bluetooth proyx server

    sudo apt-get install libbluetooth-dev

    <!-- dont know if this still required -->
    sudo setcap 'cap_net_raw,cap_net_admin+eip' `which hcitool`
    sudo setcap 'cap_net_raw,cap_net_admin+eip' `which hciconfig`


    add user to bluetooth group
    sudo vi /etc/systemd/system/dbus-org.bluez.service

    [Service]
    ExecStart=/usr/lib/bluetooth/bluetoothd -C
    Group=bluetooth

    <!-- then run -->
    sudo hciconfig hci0 piscan
    sudo systemctl daemon-reload
    sudo /etc/init.d/bluetooth restart



client send this to init:  

    550c01ff
    55bb01ff
    552401ff
    552501ff
    552601ff
    552701ff
    550201ff
    550301ff
    550401ff
    550601ff
    551f01ff
    55a001ff
    55b001ff
    55b201ff
    55b301ff
    55b401ff
    55b501ff
    55b601ff
    55b701ff
    55b801ff
    55b901ff
    55ba01ff
    550b01ff
    551801ff
    551901ff
    551a01ff
    
    551b01ff
    
treadmill responds with:

    550c0100
    
    55bb0102
    55c00224e1
    
    55c00225e1
    
    55c00226e1

    55270101
    55020100
    55030100
    550d0a00
    00000000
    0000000000
    55040204e1
    550602005a
    55c00206c2

    551f0416000100
    55c002a0e1
    
    55b0023234
    55c002b0c2
    55b208544d30314b322020
    55c002b2c2
    55b308544d303120202020
    55c002b3c2
    55b40c313230374d20202020202020
    55c002b4c2
    55b5080000000000000000
    55b60a00000000000000000000
    55b7080000000000000000
    55b80a00000000000000000000
    55b9144248202020202020202020202020202020202020(BH                  )
    55b9144248202020202020202020202020202020202020(BH                  )
    55c002b9c2
    55ba14 4455414c4b495420545245414420202020202020(DUALKIT TREAD       )
    55c002bac2
    550b0101
    551805000003061e
    55c00218c2
    5519040000183a
    55c00219c2
    551a0400000748
    55c0021ac2
    551b01b9
    55c0021bc2
    55c00218e1
    55c00219e1
    55c0021ae1
    
    550d0a00000000000000000000
    
client sends:
    
    55170101
    
    550a0102 //reset
    
  
treadmill send :

    55c0020ac2
    55c0020ac1
    
client:
    
    55010625014b00b400
 
    55170101 [ 85, 23, 1, 1 ]

treadmill:
    
    551e0101
    550d0a00000000000000000000
    55c00201c2
    55c00201c2
    55c00201c1
    
client:
    
    55150100

treadmill:
    
    55c00215c2
    55c00215c1
    
    551e0101
    550d0a00000000000000000000  
    
client:
    
    55170101
    550f020100

treadmill:
    
    55c0020fc2
    55c0020fc1
    
client:
    
    55110101

treadmill:
    
    551e0101
    550d0a00000000000000000000

client:
    
    55170101
    55080101
    

treadmill:
    
    55c00208c2
    55c00208c1
    
    551e0101
    550d0a00000000000000000000
    
client:
    
    550c01ff
    55bb01ff
    552401ff
    552501ff
    552601ff
    552701ff
    550201ff
    550301ff
    550401ff
    550601ff
    551f01ff
    55a001ff
    55b001ff
    55b201ff
    55b301ff
    55b401ff
    55b501ff
    55b601ff
    55b701ff
    55b801ff
    55b901ff
    55ba01ff
    550b01ff
    551801ff
    551901ff
    551a01ff
    551b01ff

treadmill:
    
    550c0100
    55bb0102
    55c00224e1
    550d0a00000000000000000000
    
    55c00225e1
    55c00226e1
    
    55270101
    55020100
    55030100
    55040204e1
    550602005a
    55c00206c2
    551f0416000100
    
    55c002a0e1
    55b0023234
    55c002b0c2
    55b208544d30314b322020
    55c002b2c2
    55b308544d303120202020
    55c002b3c2
    55b40c313230374d2020202020202055c002b4c2
    55b5080000000000000000
    55b60a00000000000000000000
    55b7080000000000000000
    55b80a00000000000000000000
    55b914 4248202020202020202020202020202020202020(BH                  )
    55b9144248202020202020202020202020202020202020
    55c002b9c2
    55ba14 4455414c4b495420545245414420202020202020(DUALKIT TREAD       )
    55c002bac2
    550b0101551805000003061e
    55c00218c25519040000183a
    55c00219c2551a0400000748
    55c0021ac2551b01b9
    55c0021bc2
    55c00218e1
    55c00219e1
    55c0021ae1
    
    550d0a00000000000000000000
    
client:
    
    55170101
    
    550a0102

treadmill:
    
    55c0020ac2
    55c0020ac1//19.357841s
    
     
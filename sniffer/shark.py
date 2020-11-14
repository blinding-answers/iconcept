import pyshark
import os
from pyshark.packet.packet import Packet
import json
import sys

path = os.path.dirname(os.path.abspath(__file__))
dumps_dir = os.path.join(path, 'packet_dumps')
btsnoop = os.path.join(dumps_dir, 'fitconsole_spp.pcap')

for filename in os.listdir(dumps_dir):
    file_path = os.path.join(dumps_dir, filename)
    cap1 = pyshark.FileCapture(file_path)

    packet: Packet
    comms = list()
    for packet in cap1:
        if 'BTSPP' in packet:
            data = dict()
            # print(packet.hci_h4.direction)
            data = {
                "number": packet.number,
                "direction": "receive" if packet.hci_h4.direction == '0x00000001' else "send",
                "source": packet.bthci_acl.src_bd_addr,
                "destination": packet.bthci_acl.dst_bd_addr,
                "data": str(packet.btspp.data).replace(':', '')
            }
            comms.append(data)

    with open(os.path.join(dumps_dir, f"{filename}.json"), 'w') as fp:
        json.dump(comms, fp, indent=4)
    print(json.dumps(comms, indent=4))

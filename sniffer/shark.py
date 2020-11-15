import pyshark
import os
from pyshark.packet.packet import Packet
import json
import sys

import fnmatch

treadmill_address = "8c:de:52:21:14:e4"

path = os.path.dirname(os.path.abspath(__file__))
dumps_dir = os.path.join(path, 'packet_dumps')

pscap_files = fnmatch.filter(os.listdir(dumps_dir), '*.pcap')

for filename in pscap_files:

    file_path = os.path.join(dumps_dir, filename)
    cap1 = pyshark.FileCapture(file_path)

    packet: Packet
    comms = list()
    for packet in cap1:
        if 'BTSPP' in packet:
            data = dict()
            # print(packet.frame_info.time)
            # sys.exit()
            if treadmill_address in packet.bthci_acl.dst_bd_addr or treadmill_address in packet.bthci_acl.src_bd_addr:
                data = {
                    "number": packet.number,
                    "time": packet.frame_info.time,
                    "direction": "receive" if packet.hci_h4.direction == '0x00000001' else "send",
                    "source": packet.bthci_acl.src_bd_addr,
                    "destination": packet.bthci_acl.dst_bd_addr,
                    "data": str(packet.btspp.data).replace(':', '')
                }
                comms.append(data)

    with open(os.path.join(dumps_dir, f"{filename}.json"), 'w') as fp:
        json.dump(comms, fp, indent=4)
    print(json.dumps(comms, indent=4))

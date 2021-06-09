from iconcept.fitness_device_message_processor import FitnessDeviceMessageProcessor
import logging
import os
import json
from sniffer.rfcomm_packet import RfcommPacket
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# json_path = os.path.join('sniffer', 'packet_dumps', 'btsnoop_hci_fitconsole_20201116.pcap.json')
# json_path = os.path.join('sniffer', 'packet_dumps', 'btsnoop_hci_fitconsole.pcap.json')
# json_path = os.path.join('sniffer', 'packet_dumps', 'btsnoop_hci_fitconsole_20201116.pcap.json')
# json_path = os.path.join('sniffer', 'packet_dumps', 'fit-console-btsnoop_hci-20201117.pcap.json')
# json_packets = json.load(open(json_path))
#
# # received_packets = [x.get('data') for x in json_packets if x.get('direction') == 'receive']
# received_packets = [RfcommPacket(
#     frame_number=x.get('number'),
#     src_address=x.get('source'),
#     dst_address=x.get('destination'),
#     data=x.get('data')
# ) for x in json_packets]
# received_packets = [x.get('data') for x in json_packets if x.get('direction') == 'receive']


def addr_to_device(addr):
    if "8c:de:52:21:14:e4" == addr.lower():
        return "treadmill"

    if "22:22:70:85:90:6f" == addr.lower():
        return "phone"


def json_pcap_to_rfcomm_packet(json_file: str) -> List[RfcommPacket]:
    pcap = json.load(open(json_file))
    output = []

    for packet in pcap:
        layers = packet.get("_source", {}).get("layers", {})
        frame = layers.get("frame", {})
        frame_number = frame.get("frame.number")
        bluetooth = layers.get("bluetooth", {})
        btspp = layers.get("btspp", {})
        data = btspp.get("btspp.data")
        src_address = bluetooth.get("bluetooth.src")
        dst_address = bluetooth.get("bluetooth.dst")

        if data is not None:
            packet = RfcommPacket(frame_number=frame_number, src_address=src_address, dst_address=dst_address,
                                  data=data)
            output.append(packet)

    return output


json_path = os.path.join('sniffer', 'packet_dumps', 'fitconsole_20210608.json')
# json_path = os.path.join('sniffer', 'packet_dumps', 'bhfitnesszwiftlink_20200608.json')
# json_path = os.path.join('sniffer', 'packet_dumps', 'bhfitnesszwiftlink_20210609.json')
# json_path = os.path.join('sniffer', 'packet_dumps', 'bhfitnesszwiftlink_20210609-1.json')

received_packets = json_pcap_to_rfcomm_packet(json_path)

processor = FitnessDeviceMessageProcessor()

for received_packet in received_packets:
    logger.debug(f"[{received_packet.frame_number}] from {addr_to_device(received_packet.src_address)} to {addr_to_device(received_packet.dst_address)}:")
    messages = processor.get_datagrams(received_packet)
    for message in messages:
        logger.debug(message)

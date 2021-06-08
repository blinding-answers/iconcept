from iconcept.fitness_device_message_processor import FitnessDeviceMessageProcessor
import logging
import os
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# json_path = os.path.join('sniffer', 'packet_dumps', 'btsnoop_hci_fitconsole_20201116.pcap.json')
# json_path = os.path.join('sniffer', 'packet_dumps', 'btsnoop_hci_fitconsole.pcap.json')
# json_path = os.path.join('sniffer', 'packet_dumps', 'btsnoop_hci_fitconsole_20201116.pcap.json')
json_path = os.path.join('sniffer', 'packet_dumps', 'fit-console-btsnoop_hci-20201117.pcap.json')
json_packets = json.load(open(json_path))

received_packets = [x.get('data') for x in json_packets if x.get('direction') == 'receive']
processor = FitnessDeviceMessageProcessor()
messages = processor.get_datagrams(''.join(received_packets).upper())
for message in messages:
    logger.debug(message)

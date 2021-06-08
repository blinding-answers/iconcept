import logging
import bluetooth
import sys
from iconcept.fitness_device_commander import FitnessDeviceCommander
from iconcept.fitness_device import FitnessDevice
from iconcept.fitness_device_message_processor import FitnessDeviceMessageProcessor
from iconcept.channel import Channel
import select
import time

logger = logging.getLogger(__name__)


def main():
    treadmill_hardware_address = "8c:de:52:21:14:e4"
    socket = connect(treadmill_hardware_address)
    channel = Channel(socket)
    commander = FitnessDeviceCommander(channel)
    commander.init()
    loop(socket=socket, commander=commander)


def loop(socket, commander):
    logger.debug(f"START LOOP.....")
    keep_alive_timer = time.time()
    start_time = time.time()
    started = False
    abort_time = 60
    while True:
        readable, writable, exceptions = select.select([socket], [socket], [socket], 5)
        if len(readable) > 0:
            socket = readable[0]
            data = socket.recv(2048)
            if data is not None:
                # logger.debug(f"Received binary: {data}")
                logger.debug(f"Received hex: {data.hex()}")
                processor = FitnessDeviceMessageProcessor()
                datagrams = processor.get_datagrams(data=str(data.hex()).upper())
                for datagram in datagrams:
                    logger.debug(datagram)
                # logger.debug(f"Received len: {len(data)}")

        if len(writable) > 0:
            if time.time() > keep_alive_timer + 1:
                keep_alive_timer = time.time()
                commander.keep_alive(True)
            if time.time() > start_time + 10 and started is False:
                commander.reset()
                time.sleep(1)
                commander.enable_start_key()
                time.sleep(1)
                commander.set_speed(5)
                time.sleep(1)
                commander.query_pulse_type()
                time.sleep(1)
                commander.start()
                started = True

        if len(exceptions) > 0:
            logger.exception(exceptions)
            sys.exit()

        if time.time() > start_time + abort_time:
            break

        time.sleep(0.5)


def connect(hardware_address):
    logger.debug(f"Connect to server on {hardware_address}")
    service_matches = bluetooth.find_service(uuid="00001101-0000-1000-8000-00805F9B34FB", address=hardware_address)
    # logger.debug(service_matches)
    if len(service_matches) == 0:
        logger.error("Couldn't find the RFCOMM service.")
        sys.exit(1)

    first_match = service_matches[0]
    port = first_match["port"]
    name = first_match["name"]
    host = first_match["host"]

    logger.info(f"Connecting to '{name}' on {host}:{port}")

    # Create the client socket
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        logger.debug(socket.connect((host, port)))
        logger.debug("CONNECTED")
    except Exception as e:
        logger.exception(e)
        raise e

    return socket


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.DEBUG)
        main()
    except KeyboardInterrupt:
        logger.debug("Bye")

#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import time

from iconcept import FitnessDevice
from iconcept import (
    FitnessDeviceSyncManager,
)
from iconcept.bluetooth import (
    ChatListener,
    ChatService,
)
from multiprocessing import Process

# FIX A BUG!!!
import multiprocessing

# Backup original AutoProxy function
backup_autoproxy = multiprocessing.managers.AutoProxy


# Defining a new AutoProxy that handles unwanted key argument 'manager_owned'
def redefined_autoproxy(
        token,
        serializer,
        manager=None,
        authkey=None,
        exposed=None,
        incref=True,
        manager_owned=True,
):
    # Calling original AutoProxy without the unwanted key argument
    return backup_autoproxy(token, serializer, manager, authkey, exposed, incref)


# Updating AutoProxy definition in multiprocessing.managers package
multiprocessing.managers.AutoProxy = redefined_autoproxy


def main():
    logger.debug("Main")
    hardware_address = "8C:DE:52:21:14:E4"
    # Setup multiprocess manager
    device_sync_manager = FitnessDeviceSyncManager()
    device_sync_manager.start()
    # this queue is used to send command to the chat_service
    command_q = device_sync_manager.Queue()
    device = device_sync_manager.fitness_device(command_q=command_q)
    chat_listener = ChatListener(device=device)
    chat_service = ChatService(command_q=command_q)
    chat_service.set_listener(listener=chat_listener)
    chat_service_process = Process(
        target=chat_service.connect, kwargs={"hardware_address": hardware_address}
    )
    chat_service_process.start()

    while True:
        logger.debug(f"Waiting for Connection : state = {device.connection_state}")
        if device.connection_state == 2:
            break
        time.sleep(1)

    # time.sleep(5)
    device.start()
    device.set_target_speed(4)


    # device.set_incline(8)

    chat_service_process.join()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.debug("Bye")

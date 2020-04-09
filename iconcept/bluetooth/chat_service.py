import logging
logger=logging.getLogger(__name__)

from iconcept.bluetooth import ChatListener
from typing import List
import bluetooth
import sys
import select
import time

class ChatService:
    uuid="00001101-0000-1000-8000-00805F9B34FB"
    CONNECTION_STATE_NONE=0
    CONNECTION_STATE_CONNECTING=1
    CONNECTION_STATE_CONNECTED=2
    def __init__(self, command_q):
        self.sock=None
        self.listerner:ChatListener=None
        self.command_q=command_q
        
    def connect(self,hardware_address):
        if self.listerner is not None:
            # Set state
            self.listerner.on_state_changed(self.CONNECTION_STATE_CONNECTING)
            logger.debug(f"Connect to server on {hardware_address}")
            service_matches = bluetooth.find_service(uuid=self.uuid, address=hardware_address)
            if len(service_matches) == 0:
                logger.error("Couldn't find the SampleServer service.")
                sys.exit(1)

            first_match = service_matches[0]
            port = first_match["port"]
            name = first_match["name"]
            host = first_match["host"]

            logger.info(f"Connecting to '{name}' on {host}:{port}")

            # Create the client socket
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            try:
                self.sock.connect((host, port))
                self.listerner.on_connect_success(param_string=name)      
                self.listerner.on_state_changed(self.CONNECTION_STATE_CONNECTED)       
            except Exception as e:
                self.listerner.on_state_changed(self.CONNECTION_STATE_NONE)
                self.listerner.on_connect_failed(e)      
            
            self.start_communication()
        else:
            logger.debug("No ChatListener attached!!")
            sys.exit(1)


    def start_communication(self):
        logger.debug(f"START COMMUNICATION....")
        while True:
            readable, writable, exceptional = select.select([self.sock], [self.sock], [self.sock])
            if len(readable) > 0:
                socket=readable[0]
                data = socket.recv(2048)
                if data is not None:               
                    received=data.hex()
                    logger.debug(f"Received: {received}")
                    self.listerner.on_data_read(message=received)
      
            if len(writable)>0:
                socket=writable[0]
                if not self.command_q.empty():
                    command=self.command_q.get()
                    logger.debug(f"Got command from command_q:{command}")
                    bin_data = ''.join(map(lambda x: chr(x % 256), command)).encode('utf-8')                    
                    socket.send(bin_data)
                    self.listerner.on_data_write(command)

            if len(exceptional)>0:
                self.listerner.on_state_changed(self.CONNECTION_STATE_NONE)
                self.listerner.on_connect_lost()
        
            time.sleep(0.5)
    
    def set_listener(self,listener:ChatListener):
        self.listerner=listener

        
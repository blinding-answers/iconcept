#!/usr/bin/env python3
"""PyBluez simple example rfcomm-server.py
Simple demonstration of a server application that uses RFCOMM sockets.
Author: Albert Huang <albert@csail.mit.edu>
$Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $
"""
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# import bluetooth
#
# server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# server_sock.bind(("", bluetooth.PORT_ANY))
# server_sock.listen(1)
#
# port = server_sock.getsockname()[1]
#
# uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
#
# bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
#                             service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
#                             profiles=[bluetooth.SERIAL_PORT_PROFILE],
#                             # protocols=[bluetooth.OBEX_UUID]
#                             )
#
# print("Waiting for connection on RFCOMM channel", port)
#
# client_sock, client_info = server_sock.accept()
# print("Accepted connection from", client_info)
#
# try:
#     while True:
#         data = client_sock.recv(1024)
#         if not data:
#             break
#         print("Received", data)
# except OSError:
#     pass
#
# print("Disconnected.")
#
# client_sock.close()
# server_sock.close()
# print("All done.")

from bluetooth import *

server_socket = BluetoothSocket(RFCOMM)

# server_socket.bind(("38:DE:AD:64:26:F6", 3))
server_socket.bind(("", 3))
server_socket.listen(1)


client_socket, address = server_socket.accept()

data = client_socket.recv(1024)

print("received [%s]" % data)

client_socket.close()
server_socket.close()

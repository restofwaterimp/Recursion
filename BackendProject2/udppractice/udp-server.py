import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/udp_socket_file'


try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

# display running socket
print('starting up on {}'.format(server_address))

# bind socket to particular address
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')

    # receive data from socket
    # max receive size is 4096 byte
    data, address = sock.recvfrom(4096)

    print('receive {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(sent, address))

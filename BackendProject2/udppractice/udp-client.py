import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# define server address
server_address = '/udp_socket_file'
# define client address
address = '/udp_client_socket_file'

message = b'Message to send to the client'

# combine client address
sock.bind(address)

try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    print('waiting to receive')
    #receive data max 4096 bytes
    data, server = sock.recvfrom(4096)

    print('received {!r}'.format(data))
finally:
    print('closing socket')
    sock.close()

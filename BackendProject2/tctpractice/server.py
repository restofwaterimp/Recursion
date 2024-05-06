# import socket and os module
import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up no {}'.format(server_address))


# connect socket with server address
sock.bind(server_address)

# wait connect require
sock.listen(1)

# waiting connection by client
while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            # read data from server
            # read 16 byte
            data = connection.recv(16)
            # modify binary to utf-8
            data_str = data.decode('utf-8')

            print('Received ' + data_str)

            # if exist data
            if data:
                response = 'Processing ' + data_str
                connection.sendall(response.encode())
            else:
                print('no data from ', client_address)
                break

    finally:
        print("Closing current connection")
        connection.close()
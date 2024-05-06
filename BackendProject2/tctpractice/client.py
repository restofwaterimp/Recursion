import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

# try connect server
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)


try:
    # you need to send byte format if you send socket connection
    message = b'Sending a message to the server side'
    sock.sendall(message)

    # wait 2 second
    sock.settimeout(2)

    try:
        while True:
            data =str(sock.recv(32))

            if data:
                print('Server response: ' + data)
            else:
                break
    
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()
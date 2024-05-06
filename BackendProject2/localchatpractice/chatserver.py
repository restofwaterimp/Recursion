# this program under linux
import socket
import os
from faker import Faker


sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
fake = Faker()

# socket server address
server_address = '/tmp/socket_link'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Stargin up no {}'.format(server_address))

# connect socket with server address
sock.bind(server_address)

sock.listen(1)

while True:
    connection , client_address = sock.accept()

    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(1024)

            data_str = data.decode('utf-8')

            # name,addressの場合は疑似名前、住所を返信
            # closing を受けたら、チャットを終了する
            if data:
                print('Received ' + data_str)

                if data_str.find("name") >= 0 or data_str.find("who are") >= 0:
                    return_message=fake.name()
                elif data_str.find("address") >= 0:
                    return_message=fake.address()
                elif data_str == "closing":
                    return_message="OK. Closing socket."
                else:
                    return_message=fake.text()

                response = 'Processing : ' + return_message
                connection.sendall(response.encode())

                # Do you finish socket?
                if data_str == "closing":
                    print('receive closing signal.')
                    break
            # else:
            #     print('no data from ' + client_address)
                

    finally:
        print('Closing current connection')
        connection.close()
        break

print("finish socket server")


import socket
import sys


sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

server_address='/tmp/socket_link'
print('connecting to {}'.format(server_address))

print("Chat Start")

try:
    sock.connect(server_address)

except socket.error as err:
    print(err)
    print("Don't connect server []".format(server_address))
    sys.exit(1)


#closing とチャットに入力するまではチャットとやり取りできる
while True:
    print('Input messege to server >>> ')
    #テキストでメッセージを入力させる
    message=input()
    # binary に変換
    bmessage=bytes(message.encode())

    sock.sendall(bmessage)

    sock.settimeout(2)

    try:
        # while True:
        # 繰り返しにすると、recvでTimeoutErrorになるため、一回のみ受信
        # 受信時のバイト数を1024にした
        data=str(sock.recv(1024))

        if data:
            print('Server response: ' + data)
        else:
            break

        if message=="closing":
            break


    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')
        sys.exit(1)

    #finally:
        ##print("Finish Received.")
        #処理を終了させる場合        
        # print('closing socket')
    # sock.shutdown(socket.SHUT_RDWR)
    # sock.close()

sock.close()
print("Close socket")



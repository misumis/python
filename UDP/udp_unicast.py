########################
#                      #
# Author: Michał Nowak #
#                      #
########################

import socket
import threading

HOST = 'localhost'


def client(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except Exception as e:
        print(e)
    while True:
        message = input("What to send:")
        try:

            print("\nYour message: " + message)
            sock.sendto(message.encode('utf-8'), (HOST, port))
            data, address = sock.recvfrom(1024)
        except Exception as e:
            print(e)
        print('Recived from server: {}'.format(data.decode("utf-8")))


def server(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('localhost', port))
    except Exception as e:
        print(e)

    while True:
        data, address = sock.recvfrom(1024)
        print(address, data.decode("utf-8"))
        sock.sendto(data, address)


def main():
    port = int(input('Enter port number:'))
    th = threading.Thread(target=server, args=(port, ))
    th.start()
    client(port)


if __name__ == '__main__':
    main()

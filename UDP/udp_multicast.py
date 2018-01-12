########################
#                      #
# Author: Michał Nowak #
#       Muklticast      #
########################
import socket
import struct
import threading


MCAST_GRP = 'localhost'
MCAST_PORT = 8080

def send_data(message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
        sock.sendto(message, (MCAST_GRP, MCAST_PORT))
    except Exception as e:
        print(e)

def receive_data():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.MCAST, 1)
        sock.bind(('', MCAST_PORT))
        mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    except Exception as e:
        print(e)

    print('Start receiving.')
    while True:
        data, address = sock.recvfrom(1024)
        print(address, data.decode("utf-8"))


def main():
    recive_thread = threading.Thread(target=receive_data)
    recive_thread.start()
    
    while True:
        message = input("Enter message:")
        send_data(message.encode())


if __name__ == '__main__':
    main()

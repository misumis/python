########################
#                      #
# Author: Michał Nowak #
#       Broadcast      #
########################

import socket
import threading
import socketserver

BUFSIZE = 65535
UDP_IP = ''

def server(interface,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)        
        sock.bind(('', port))
    except Exception as e:
        print("Error Binding")
        pass

    while True:
        data, address = sock.recvfrom(1024)
        print(address, data.decode("utf-8"))
        sock.sendto(data,('255.255.255.255',port))
        # sock.sendto('Test', ('255.255.255.255',port))

# zajęcia od 17:30 - 20:00 Niedziela, E110

def main():
    port = int(input('Enter port number:'))
    th = threading.Thread(target=server, args=(UDP_IP,port))
    th.start()


if __name__ == '__main__':
    main()


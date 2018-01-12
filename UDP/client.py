########################
#                      #
# Author: Michał Nowak #
#       Broadcast      #
########################

import socket
import threading
import socketserver

UDP_IP = ''


def client(network, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)        
        sock.bind(('', port))
    except socket.timeout:
        print("Error")
        pass

    while True:
        
        try:
            
            text = input('> ')
            sock.sendto(text.encode('utf-8'), (network, port))
            data, address = sock.recvfrom(1024)
        except Exception as e:
            pass    
        print('Server: ', data.decode('utf-8'))

def main():
    port = int(input('Enter port number:'))
    client('localhost',port)
    
if __name__ == '__main__':
    main()

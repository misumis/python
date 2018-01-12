########################
#                      #
# Author: Michał Nowak #
#       HTTP Server    #
########################

import socket
import os
from lxml import etree

def objects_sum(table):
    table = etree.HTML(table).find("body/table")
    Sum = 0
    for row in table:
        values = int([col.text for col in row][1])
        Sum += values
    return Sum

HOST, PORT = '', 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(1)
print('Serving HTTP on port %s ...' % PORT)

while True:
    client_connection, client_address = sock.accept()
    request = client_connection.recv(1024)
    print()
    if len(request.decode().split()) > 1:
        files_to_serve = request.decode().split()[1].strip("/").split("_")
    else:
        files_to_serve = []

    result = """\
    HTTP/1.1 200 OK

    <html>
    <body>
    <table border=1>
    """
    for file in [name for name in files_to_serve if os.path.isfile("{}.txt".format(name))]:    
        with open("{}.txt".format(file), "r") as file:
            result += file.read()

    Sum = objects_sum(result)
    result += """
    </table>
    <b>Sum: {}</b>
    </body>
    </html>
    """.format(Sum)

    http_response = result.encode()
    client_connection.sendall(http_response)
    client_connection.close()
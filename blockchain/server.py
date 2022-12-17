import os
import socket
import threading
import json


def handle_connection(sock, addr):
    data = sock.recv(1024)
    data = json.loads(data.decode())
    
    if data['action'] == 'info':
        sock.send(
            str(json.dumps({
                'status': 200
            })).encode()
        )

    


def server():
    HOST = 'localhost'
    PORT = 5000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen(1)
        
        while True:
            print("Waiting for connection... ")
            sock, addr = serv_sock.accept()
            print(f"{addr[0]}:{addr[1]} - connected")
            t = threading.Thread(target=handle_connection, args=(sock, addr))
            t.start()
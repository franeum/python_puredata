#!/usr/bin/env python3

import socket 

HOST = "127.0.0.1"
PORT = 8000
ADDRESS = (HOST, PORT)

#client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#client_socket.sendto() 

def init_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return client 

def send_msg(msg, client):
    return client.sendto(str.encode(msg), (HOST, PORT))

def close_client(clnt):
    return clnt.close()
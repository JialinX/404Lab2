#!/usr/bin/env python3
import socket, sys

def create_tcp_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f"Failed to create socker. Error code: {str(msg[0])}, Error message : {msg[1]}")
        sys.exit()
    print("Socket created successfully")
    return s

def get_remote_ip(host):
    print(f"Getting IP for {host}")
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()
    print(f'IP address of {host} is {remote_ip}')
    return remote_ip

def send_data(serversocket, payload):
    print("Sending payload")
    try:
        serversocket.sendall(payload.encode())
    except:
        socket.error:
        print('Send failed')
        sys.exit()
    print("Payload sent successfully")

def main():
    try:
        host = "www.google.com"
        port = 80
        payload = 
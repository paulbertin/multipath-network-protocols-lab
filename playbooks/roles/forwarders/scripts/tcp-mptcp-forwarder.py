#!/usr/bin/env python3

import socket
import argparse
import threading

# Function for forwarding data from one socket to another
def forward_data(source, destination):
    while True:
        try:
            data = source.recv(1024)
            if not data:
                break
            print(f'Forwarding {len(data)} bytes from {source.getpeername()} to {destination.getpeername()}')
            destination.sendall(data)
        except (socket.error, socket.timeout, OSError) as e:
            print(f'Error while forwarding data: {e}')
            break

# Add argument parser
parser = argparse.ArgumentParser(
    description="Forward TCP to MPTCP connection"
)

parser.add_argument('-l', '--listen', required=True,
    help='Listen address for incoming TCP connection (ip:port format)')

parser.add_argument('-d', '--destination', required=True,
    help='Destination address for forwarding (ip:port format)')

args = parser.parse_args()

tcp_socket = None
mptcp_socket = None

try:
    # Create TCP socket and bind it to listen address
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    ip, port = args.listen.split(':')
    listen_address = (ip, int(port))
    tcp_socket.bind(listen_address)
    print(f'Start listening for incoming TCP connection on {args.listen}')
    tcp_socket.listen()
    conn, addr = tcp_socket.accept()
    print(f'Accepted TCP connection from {addr}')

    # Create MPTCP socket and connect to destination address
    mptcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_MPTCP)
    ip, port = args.destination.split(':')
    destination_address = (ip, int(port))
    mptcp_socket.connect(destination_address)
    print(f'Connected to {destination_address} via MPTCP. Start forwarding data...')

    # Start forwarding data in separate threads (one for each direction)
    tcp_thread = threading.Thread(target=forward_data, args=(conn, mptcp_socket))
    mptcp_thread = threading.Thread(target=forward_data, args=(mptcp_socket, conn))
    tcp_thread.start()
    mptcp_thread.start()

    # Wait for threads to finish
    tcp_thread.join()
    mptcp_thread.join()

except (socket.error, socket.timeout, OSError) as e:
    print(f'Socket error: {e}')

finally:
    # Close sockets
    if tcp_socket:
        tcp_socket.close()
        print("TCP socket closed")
    if mptcp_socket:
        mptcp_socket.close()
        print("MPTCP socket closed")

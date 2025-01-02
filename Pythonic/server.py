import socket
import threading

# threading = multitasking

PORT = 5050

# Get the hostname of the local machine
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) #anything that connects to the address will hit  the socket



# TO // CONTINUE //
# https://www.youtube.com/watch?v=3QiPPX-KeSc
# 19:05
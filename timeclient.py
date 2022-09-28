import socket

from config import PORT,MSG_LENGTH,FORMAT

s=socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT))

while True:
    timestamp_message=s.recv(MSG_LENGTH).decode(FORMAT)
    print(timestamp_message)
    

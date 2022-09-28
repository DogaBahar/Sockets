import socket
import time
import threading

from datetime import datetime
from config import PORT, MAX_CONNECTIONS,FORMAT

def send_timestamps(connection, sender):
    print(f"New connection {sender} connected")
    connected=True
    while connected:
        timestamp = datetime.now().isoformat()
        connection.send(bytes(timestamp +'\n', FORMAT))
        print(timestamp)
        time.sleep(5)
        

def start_timeserver():
    s=socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), PORT))
    s.listen(MAX_CONNECTIONS)
    
    while True:
        connection, sender= s.accept()
        print(f'Connection to {sender} established')
        thread=threading.Thread(target=send_timestamps, args=(connection,sender))
        thread.start()
        print(f"Active connections {threading.activeCount()-1}")

    
if __name__=='__main__':      
    print('server is starting...')
    start_timeserver()


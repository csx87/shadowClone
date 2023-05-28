import socket

PORT = 6969
HOST = "0.0.0.0"
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
FORMAT = "utf-8"
HEADER = 64
DISCONNECT_MESSAGE = "DISCONNECT"

def send(msg,conn):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)
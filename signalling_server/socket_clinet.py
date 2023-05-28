import socket
import messaging as msg
import time 
import random

rand_int = random.randint(0,100)
#name = str(rand_int)

name = "Chaman"

PORT = 6969
HOST = "172.232.68.4"
ADDR = (HOST, PORT)
FORMAT = "utf-8"
HEADER = 64
DISCONNECT_MESSAGE = "DISCONNECT"
PING_MESSAGE = "PING"
SAME_NAME = "same_name"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

msg.send_message(client,name)

connected = True

while connected:
    message = msg.recv_offer(client)
    if(message == PING_MESSAGE):
        msg.send_message(client,PING_MESSAGE)
    elif(message == SAME_NAME):
        print("Alread a client with same name connected use a different name")
        client.close()
        connected = False
    else:
        offerSDP = message
        print(f"[Offer sdp recieved]: {offerSDP}")
        answerSDP = "Answer SDP"
        print(f"[Answer sdp sent]: {answerSDP}")
        msg.send_answer(client, answerSDP)

exit(1)
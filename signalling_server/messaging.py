import socket
import server_info as serv_info

HEADER = serv_info.HEADER
FORMAT = serv_info.FORMAT

def send_message(conn, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)

def recv_message(conn):
    msg = None
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
    return msg

def send_offer(conn, offerSDP):
    return send_message(conn,offerSDP)

def send_answer(client, answerSDP):
    return send_offer(client,answerSDP)

def recv_offer(conn):
    return recv_message(conn)

def recv_answer(client):
    return recv_message(client)
        
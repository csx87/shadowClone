import socket
import server_info as serv_info

MSG_LENGTH = serv_info.MSG_LENGTH
FORMAT = serv_info.FORMAT

def send_message(conn, msg):
    message = msg.encode(FORMAT)
    conn.send(message)

def recv_message(conn):
    msg = None
    msg = conn.recv(MSG_LENGTH).decode(FORMAT)
    return msg

def send_offer(conn, offerSDP):
    return send_message(conn,offerSDP)

def send_answer(client, answerSDP):
    return send_offer(client,answerSDP)

def recv_offer(conn):
    return recv_message(conn)

def recv_answer(client):
    return recv_message(client)
        

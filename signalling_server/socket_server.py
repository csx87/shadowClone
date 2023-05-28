import socket
import server_info as ser
import threading
import messaging as msg
import time
import client_database as database



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ser.ADDR)

def handle_client(conn,addr):
    clientName = msg.recv_message(conn)
    #print(f"[Socket Server][NEW CONNECTION] {clientName} {addr} connected")

    if(database.client_name_is_not_present(clientName)):
        database.add_client_to_database(clientName,conn)

    else:
        print("client with same name already present. closing connection")
        msg.send_message(conn,ser.SAME_NAME)
        conn.close()


    ''' 
    connected =True
    while connected:
        offerSDP = "OFFER SDP 12234"
        ret = "hello"
        msg.send_offer(conn,offerSDP)
        ret = msg.recv_answer(conn)
        connected = False

        if ret == ser.DISCONNECT_MESSAGE:
           connected = False
           conn.close()
           print("[connection closed]") 
           print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1 }")
        else: 
            answerSDP = answerSDP

        print(f"[Answer SDP receieved][{addr}] {answerSDP}")
    '''        

def send_offer_sdp_get_answer_sdp(clientName,offerSDP):
    conn = database.find_client_conn(clientName)
    if(conn):
        msg.send_offer(conn,offerSDP)
        ret = msg.recv_answer(conn)

        if ( ret == ser.DISCONNECT_MESSAGE or ret == None):
            print("[Socket Server]Client is disconnected or not available")
            database.del_client_from_database(clientName)
            conn.close()
            return None
        
        return ret



def start_socket_server():
    server.listen()
    print(f"[Socket Server] is listening on {ser.PORT}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target = handle_client,args = (conn,addr))
        thread.start()
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1 }")


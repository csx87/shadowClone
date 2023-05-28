import server_info as ser
import messaging as msg
clientDatabase = dict()

def add_client_to_database(name,conn):
    print(f"[Socket Server] Adding client {name} to database")
    clientDatabase[name] = conn

def del_client_from_database(name,ADDR):
    print(f"[Socket Server] Removing client {name,ADDR} from database")
    clientDatabase.pop(name)

def find_client_conn(clientName):
    if(clientName in clientDatabase):
        return clientDatabase[clientName]
    return None

def print_client_names():
    print("\nDatabase: ")
    for keys in clientDatabase:
        print(keys)
    print("\n")

def client_name_is_not_present(name):
    try:
        conn = clientDatabase[name]
    except KeyError:
        return True
    try:
        msg.send_message(conn,ser.PING_MESSAGE)
    except BrokenPipeError:
        return True
    try:
        msg.recv_message(conn)
    except BrokenPipeError:
        return True
    return False

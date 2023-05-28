from http.server import HTTPServer,BaseHTTPRequestHandler
import server_info as ser
import socket_server as socket
import messaging as msg
import json
import threading

dict = {"key" : "value"}

class webrtcServer(BaseHTTPRequestHandler):
    def do_POST(self): 
        content_length = int(self.headers['Content-Length'])
        clientName = str(self.headers['Client-Name']) #Removes the starting and ending "" from client name
        body = self.rfile.read(content_length)
        offerSDP = body.decode('utf-8', 'strict')

        print(offerSDP)

        answerSDP = socket.send_offer_sdp_get_answer_sdp(clientName,offerSDP)

        jsonToReply = None
        if(answerSDP == None):
            print("Client not available or disconnected")
            jsonToReply = {"success":False,"message":"Client not available or disconnected"}
        else:
            jsonToReply = {"success":True,"message":"","answerSDP":answerSDP}

        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()

        json_string = json.dumps(jsonToReply)
        self.wfile.write(bytes(json_string.encode(encoding='utf_8')))
    
    #def do_GET(self):

thread = threading.Thread(target = socket.start_socket_server)
thread.start()
server = HTTPServer(('172.232.68.4',8787), webrtcServer)
print(f"[HTTP server] now runnig on PORT: 8787")
server.serve_forever()
server.server_close()

package com.example.shadow_clone;

import android.util.Log;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.Socket;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

public class SocketServerHandling {
    private final String serverIP;
    private final int serverPort;
    private String clientName = null;
    private Socket clientSocket = null;

    private final int MSG_LENGTH = 532;
    private final Charset charset = StandardCharsets.UTF_8;
    private final String PING_MESSAGE = "PING";
    private final String SAME_NAME = "same_name";
    private final String DISCONNECT_MESSAGE = "DISCONNECT";

    SocketServerHandling(String IP,int PORT){
        serverIP = IP;
        serverPort = PORT;
    }

    public void setClientName(String clientName) {
        this.clientName = clientName;
    }

    public boolean connectToServer(){
        try {
            clientSocket = new Socket(serverIP,serverPort);
        } catch (IOException e) {
            e.printStackTrace();
            return  false;
        }

        if(clientSocket != null) {
            if (clientName != null) {
                    return  sendMessage(clientName);
            }
            else{
                Log.i("socket","Client Name is not present");
                return false;
            }
        }
        return false;
    }

    public boolean sendMessage(String message){


        if(message == null){
            Log.i("socket server","message is null");
            return false;
        }

        OutputStream clientSocketOut = null;
            try {
                clientSocketOut = clientSocket.getOutputStream();
            } catch (IOException e) {
                e.printStackTrace();
                return false;
            }

            if(clientSocketOut != null) {
                try {
                    byte[] msgByte = message.getBytes(charset);
                    Log.i("debug", "Sending message:" + message);
                    clientSocketOut.write(msgByte);
                    clientSocketOut.flush();


                } catch (IOException e) {
                    e.printStackTrace();
                    return false;
                }

            }
           return true;
    }

    public String recvMessage()  {


        if (clientSocket == null) {
            Log.i("socket server", "Not connected to server");
            return null;
        }
        InputStream clientSocketIn = null;
        try {
            clientSocketIn = clientSocket.getInputStream();
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (clientSocketIn != null) {
            DataInputStream dos = new DataInputStream(clientSocketIn);
            byte[] buffer = new byte[MSG_LENGTH];
            int ret;
            try {
                ret = dos.read(buffer);
            } catch (IOException e) {
                e.printStackTrace();
                return null;
            }
            String message = new String(buffer, 0, ret, charset);
            Log.i("debug","Recv message:" + message);
            return message;
        }
        return null;
    }

    public void close(){
        sendMessage(DISCONNECT_MESSAGE);
       try{
           clientSocket.close();
       } catch (IOException e) {
           e.printStackTrace();
       }
       clientName = null;
       clientSocket = null;
    }

}

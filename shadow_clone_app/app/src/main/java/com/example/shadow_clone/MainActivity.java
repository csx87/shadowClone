package com.example.shadow_clone;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import java.net.Socket;
import java.util.Objects;

public class MainActivity extends AppCompatActivity {

    private TextView tvOfferSDP;
    private EditText etAnswerSDP, etClientName;
    private Button connectToServerButton;
    private String offerSDP,answerSDP;
    private SocketServerHandling socketServer;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvOfferSDP = findViewById(R.id.offer_sdp);
        etAnswerSDP = findViewById(R.id.answer_sdp);
        etClientName = findViewById(R.id.client_name);
        connectToServerButton = findViewById(R.id.connect_to_server_button);

    }

    public void onClickConnect(View view){

        String clientName = etClientName.getText().toString();
        answerSDP = etAnswerSDP.getText().toString();
        String PING_MESSAGE = getString(R.string.PING_MESSAGE);
        String SAME_NAME = getString(R.string.SAME_NAME);

        new Thread(new Runnable() {
            @Override
            public void run() {

                String serverIP = getResources().getString(R.string.IP);
                int serverPort = getResources().getInteger(R.integer.PORT);

                boolean ret;
                socketServer = new SocketServerHandling(serverIP, serverPort);
                socketServer.setClientName(clientName);

                // Connect to server
                ret = socketServer.connectToServer();
                if (ret) {
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            connectToServerButton.setText("Connected to sever");
                            connectToServerButton.setEnabled(false);
                        }
                    });

                    boolean connected = true;
                    while(connected){
                        String message = null;
                        message = socketServer.recvMessage();

                        if(message == null){
                            Log.i("debug","message is null");
                        }
                        else if(Objects.equals(message,PING_MESSAGE )){
                            socketServer.sendMessage(PING_MESSAGE);
                        }
                        else if (Objects.equals(message,SAME_NAME)){
                            Log.i("debug","client with the same name present");
                            connected = false;
                        }

                        else {
                            offerSDP = message;
                            Log.i("offer sdp",offerSDP);
                            // TODO: Check if offer sdp is valid
                            socketServer.sendMessage(answerSDP);
                        }
                    }
                    socketServer.close();
                    socketServer = null;
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            connectToServerButton.setText("Connect to sever");
                            connectToServerButton.setEnabled(true);
                        }
                    });

                }

            }

        }).start();
    }

    @Override
    protected void onDestroy() {
        socketServer.close();
        Log.i("debug","here");
        super.onDestroy();

    }
}



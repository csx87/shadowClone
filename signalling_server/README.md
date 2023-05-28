# Signalling server

You can find these files in 
/ccshare/linux/c_files/surecha/shadow_clone/signalling_server in linux 98 machine

## 1) Deploy the server
Copy all the files in same directory and do:
``` python3 server.py ```

**Note: Do this in 98 machine** 

## 2) Connect the client
``` python3 socket_client.py```

**Note: You can do this in any device which has an access to 98 machine or in 98 machine itself**

**Note: Give client name as Chaman only** 

## 3) Flash the modified firmware

Flash the box with ```
/ccshare/linux/c_files/surecha/shadow_clone/signalling_server/shadow_clone_v1.update```

**Note: Use a box which has access to 98 machine**

In this firmware the server ip-add has been  hardcorded to 98 machine and client-name to Chaman

For later we can make our nest app provide the server address and client name

## Check the pipeline logs 

You should see 

``` 
[mpa]<5/8  3:36:13.900 -6> [webrtcsrc]<webrtcsrc.c:677>send_sdp_to_peer():response: {"success": true, "message": "", "answerSDP": "<your SDP>"}
 ```
 
 The logs will end with an SDP error. That is expected since we are giving some random answer SDP 

import socket
import time
import pandas as pd
import os
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #define the client.

client.connect(('localhost', 9080)) #connect the client.

#send a message to  start the server.
message = "Start program"
client.send(message.encode("UTF-8"))  

 
#receive a message from server to receive and decode.
response = client.recv(1024).decode("UTF-8")
print("response",response)
time.sleep(100)


response = client.recv(1024).decode("UTF-8")
print("response",response)
df_final_data = pd.read_csv(response, encoding='utf-8')
print(df_final_data)

message = "received_successfully"
client.send(message.encode("UTF-8"))

#receive data's and binary image.
image_data = b""
while True:
    data = client.recv(1024)
    if not data:
        break
    image_data += data

#save the binary data's as an image data.
with open("received_output1.png", "wb") as file:
    file.write(image_data)

client.close() #close the client's connection with server.

os.startfile("received_output1.png")

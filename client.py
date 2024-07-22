import socket
import time
import pandas as pd
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 9080))

#send message to server
message = "Start program"
client.send(message.encode("UTF-8"))  

 
#recive message from server
response = client.recv(1024).decode("UTF-8")
print("responce",response)
time.sleep(100)


response = client.recv(1024).decode("UTF-8")
print("responce",response)
df_final_data = pd.read_csv(response, encoding='utf-8')
print(df_final_data)

message = "received_successfully"
client.send(message.encode("UTF-8"))
#دریافت داده تصویر باینری 
image_data = b""
while True:
    data = client.recv(1024)
    if not data:
        break
    image_data += data

# ذخیره داده‌های باینری به عنوان فایل تصویری
with open("received_output1.png", "wb") as file:
    file.write(image_data)



client.close()

os.startfile("received_output1.png")
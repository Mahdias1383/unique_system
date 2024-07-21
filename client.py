import socket
import time
import pandas as pd

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 9080))

# تا زمانی که خودم نگفتم پیام بفرست
# while True:
#    #send message to server
#    message = input("Enter a message:")
#    client.send(message.encode("UTF-8"))
#    if message == "quit":
#       break
   
#    #recive message from server
#    response = client.recv(1024).decode("UTF-8")
#    print("responce",response)

# client.close()


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


client.close()
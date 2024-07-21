import socket
import pandas as pd
import time
from digikala_crawler import scrape_digikala_product_details
from amazon_crawler import scrape_amazon_product_details
from olfa_crawler import scrape_olfa_product_details
from urls import urls
from menu_urls import menu_urls
from lists import list_digikala,list_olfa,list_amazon
from create_crawler_queue import crawler_queue
from merge_data import create_data_frames,combine_data_frames
from scrape_threads import crawler_threads
import final_df

#amazon
#queue_amazon = crawler_queue("amazon")
#crawler_threads(scrape_amazon_product_details,queue_amazon,list_amazon)
#print(list_amazon)
#df_amazon = create_data_frames(list_amazon, "amazon.csv")
#time.sleep(45)

#digikala 
#queue_digikala = crawler_queue("digikala")
#crawler_threads(scrape_digikala_product_details,queue_digikala,list_digikala)
#print(list_digikala)
#df_digikala = create_data_frames(list_digikala, "digikala.csv")
#time.sleep(20)

#olfa
#queue_olfa = crawler_queue("olfa")
#crawler_threads(scrape_olfa_product_details,queue_olfa,list_olfa)
#print(list_olfa)
#df_olfa = create_data_frames(list_olfa, "olfa.csv")
#time.sleep(5)




# df_amazon = pd.read_csv('digikala.csv', encoding='utf-8')
# df_digikala = pd.read_csv('olfa.csv', encoding='utf-8')
# df_olfa = pd.read_csv('amazon.csv', encoding='utf-8')
#df_combined = combine_data_frames(df_amazon,df_digikala,df_olfa)
#print(df_combined)


# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("localhost", 9080))

# server.listen(1)
# print('Server is listening on port 9080')

# #handle message
# while True:
#     conn, addr = server.accept()
#     print('Connected by', addr)
#     while True:
#         # get data from client
#         #1024 سایز بافر خواندن 
#         # سایز پیام خواندن که پیام چند بیت بیت بخواند
#         #utf-8 یک استاندارد برای decode and encode
#         data=conn.recv(1024).decode("UTF-8")
#         if not data:
#             break
#         print(data)
    
#         # by this connection that is conn/ send message to client
#         message = input("Enter a message:")
#         conn.send(message.encode("UTF-8"))   
    
#     conn.close()  
# server.close()
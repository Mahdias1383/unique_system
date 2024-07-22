import threading
from queue import Queue
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
from menu_urls import menu_urls
from lists import list_amazon
from create_crawler_queue import crawler_queue

def scrape_amazon_product_details(queue, result_list):
   "Scrape products details from amazon's urls."
   while not queue.empty():
        url = queue.get() #get urls by a queue.
        time.sleep(1)
        HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")
        price = soup.find("p", class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice") #scrape product's price.
        if price:
           price1 = price.text.strip() #return price element as a text.
        else:
            price = soup.find("span", class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice") #another details to find price element.
           
        
        title = soup.find("span",{"id":"productTitle","class":"a-size-large product-title-word-break"}) #scrape title's element.
        title1 = title.text.strip() #return title's element as a text.
        
        index = title1.find(',')
        if index != -1:
           result = title1[:index]
        else:
           result = title1  
        
        #append the results to the final scrape details of amazon's list.
        price2 =float(price1[1:]) * 60000 #convert prices from dollar to Toman .
        result_list.append({"name_product": result, "price_product": price2})
        queue.task_done()

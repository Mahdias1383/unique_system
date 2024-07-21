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
    while not queue.empty():
        url = queue.get()
        time.sleep(1)
        HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")
        price = soup.find("p", class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice")
        if price:
           price1 = price.text.strip()
        else:
            price = soup.find("span", class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice")
           
        
        title = soup.find("span",{"id":"productTitle","class":"a-size-large product-title-word-break"})
        title1 = title.text.strip()
        
        index = title1.find(',')
        if index != -1:
           result = title1[:index]
        else:
           result = title1  # اگر | پیدا نشد، کل متن را برگرداند
        #print(result)
        # اضافه کردن نتیجه به لیست
        price2 =float(price1[1:]) * 60000
        result_list.append({"name_product": result, "price_product": price2})
        queue.task_done()

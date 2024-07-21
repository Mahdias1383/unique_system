import threading
from queue import Queue
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from menu_urls import menu_urls
from lists import list_olfa
from create_crawler_queue import crawler_queue
#------------

def scrape_olfa_product_details(queue, result_list):
    while not queue.empty():
        url = queue.get()
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(3)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        title_element = soup.find("h1", class_="product_title entry-title wd-entities-title")
        title = title_element.text.strip() if title_element else "عنوان محصول یافت نشد"
        index = title.find('|')
        if index != -1:
           result = title[:index]
        else:
           result = title

        price_element = soup.find("p", class_="price")
        price = price_element.text.strip() if price_element else "قیمت یافت نشد"
        price1 = price.replace("تومان", "")
        price1 = price1.split('–')[0].strip().replace(',', '')

        # Convert to integer
        price1 = float(price1)
        
        result_list.append({"name_product": result, "price_product": price1})

        driver.quit()
        queue.task_done()





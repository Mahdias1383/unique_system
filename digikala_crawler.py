import threading
from queue import Queue
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from menu_urls import menu_urls
from lists import list_digikala
from create_crawler_queue import crawler_queue

def scrape_digikala_product_details(queue, result_list):
    "Scrape products details from digikala's urls."
    while not queue.empty():
        url = queue.get() #get urls by a queue.
        driver = webdriver.Chrome() #define a driver by selenium lib.
        driver.get(url)
        time.sleep(10)
        page_source = driver.page_source

        #use beautiful soap to export data.
        soup = BeautifulSoup(page_source, 'html.parser')

        #find the title of product.
        title_element = soup.find("h1", class_="text-h4 text-neutral-900 mb-2 pointer-events-none")
        title = title_element.text.strip() if title_element else "عنوان محصول یافت نشد"

        #find the price of the product.
        price_element = soup.find("span", class_="text-h4 ml-1 text-neutral-800")
        price = price_element.text.strip() if price_element else "قیمت یافت نشد"
        price = price.replace(",", "")
        price =float(price)
        
        #append the results to the final scrape details of digikala's list.
        result_list.append({"name_product": title, "price_product": price})

        driver.quit()
        queue.task_done()
        















import threading
from queue import Queue
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
#import urls_dict
#import menu_urls
#import digikala_list
#import crawler_queue
#----------------------


# تنظیمات صف و لیست
#queue_digikala = Queue(100)





# for k, v in menu_urls["digikala"].items():
#     print(v)
#     queue_digikala.put(v)

def scrape_digikala_product_details(queue, result_list):
    while not queue.empty():
        url = queue.get()
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(5)
        page_source = driver.page_source

        # استفاده از BeautifulSoup برای تجزیه HTML
        soup = BeautifulSoup(page_source, 'html.parser')

        # پیدا کردن عنوان محصول
        title_element = soup.find("h1", class_="text-h4 text-neutral-900 mb-2 pointer-events-none")
        title = title_element.text.strip() if title_element else "عنوان محصول یافت نشد"

        # پیدا کردن قیمت محصول
        price_element = soup.find("span", class_="text-h4 ml-1 text-neutral-800")
        price = price_element.text.strip() if price_element else "قیمت یافت نشد"

        # اضافه کردن نتیجه به لیست
        result_list.append({"name_product": title, "price_product": price})

        driver.quit()
        queue.task_done()















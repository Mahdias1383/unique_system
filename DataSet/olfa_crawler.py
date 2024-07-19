import threading
from queue import Queue
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
#------------
urls = {
    "digikala" : {
        "url1" :"https://www.digikala.com/product/dkp-14664702/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%DA%AF%D9%88%D8%B3%D9%88%D9%86%DB%8C%DA%A9-%D9%85%D8%AF%D9%84-gem-873/",
        "url2" : "https://www.digikala.com/product/dkp-1901244/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88%D8%B3%D8%A7%D8%B2-%D9%86%D9%88%D8%A7-%D9%85%D8%AF%D9%84-nova-ncm-128exps/",
        "url3" : "https://www.digikala.com/product/dkp-4836058/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D9%86%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D9%85%D8%AF%D9%84-pixie-en124s",
        "url4" : "https://www.digikala.com/product/dkp-4889296/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D8%AF%D9%88%D9%84%DA%86%D9%87-%DA%AF%D9%88%D8%B3%D8%AA%D9%88-%D9%85%D8%AF%D9%84-mini-me/",
        "url5" : "https://www.digikala.com/product/dkp-2356208/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88%D8%B3%D8%A7%D8%B2-%D8%B2%DB%8C%DA%AF%D9%85%D8%A7-%D9%85%D8%AF%D9%84-rl-222/",
        "url6":"https://www.digikala.com/product/dkp-9870703/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D9%85%D8%A8%D8%A7%D8%B4%DB%8C-%D9%85%D8%AF%D9%84-me-ecm-2034/",
        "url7":"https://www.digikala.com/product/dkp-1929346/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D9%85%D8%A8%D8%A7%D8%B4%DB%8C-%D9%85%D8%AF%D9%84-ecm2010/",
        "url8":  "https://www.digikala.com/product/dkp-2181548/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88%D8%B3%D8%A7%D8%B2-%D9%85%D8%A8%D8%A7%D8%B4%DB%8C-%D9%85%D8%AF%D9%84-ecm2013/",
        "url9":"https://www.digikala.com/product/dkp-14998371/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D9%81%DB%8C%D9%84%DB%8C%D9%BE%D8%B3-%D9%85%D8%AF%D9%84-ep3246/",
        "url10": "https://www.digikala.com/product/dkp-4354974/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D8%AF%D9%84%D9%88%D9%86%DA%AF%DB%8C-%D9%85%D8%AF%D9%84-ec685/",
    },  
    "olfa" : {
        "url1" : "https://www.olfacoffee.com/product/philips-ep5443-70/",
        "url2" : "https://www.olfacoffee.com/product/%d8%a7%d8%b3%d9%be%d8%b1%d8%b3%d9%88-%d8%b3%d8%a7%d8%b2-%d9%86%d9%88%d8%a7-128/",
        "url3" : "https://www.olfacoffee.com/product/bosch-tis30129rw/",
        "url4" : "https://www.olfacoffee.com/product/delonghi-ec-235/",
        "url5" : "https://www.olfacoffee.com/product/delonghi-ec7-espresso-machine/",
        "url6" :"https://www.olfacoffee.com/product/%d8%a7%d8%b3%d9%be%d8%b1%d8%b3%d9%88-%d8%b3%d8%a7%d8%b2-%d9%85%d8%a8%d8%a7%d8%b4%db%8c-2034-ecm/",
        "url7" :"https://www.olfacoffee.com/product/mebashi-ecm2010/",
        "url8" :"https://www.olfacoffee.com/product/philips-ep3246/",
        "url9" :"https://www.olfacoffee.com/product/sprso-mchin-me-ecm2013/",
        "url10": "https://www.olfacoffee.com/product/delonghi-685/"
    },
    "amazon" : {
        "url1" : "https://www.amazon.com/Breville-BES840XL-Infuser-Espresso-Machine/dp/B0089SSOR6/ref=sr_1_24?crid=3PGDS82IRP7ON&dib=eyJ2IjoiMSJ9.-kzrHI0becQBDvbaGQoPjc5KfeJOjc6Eqv2VlU1YegLGfI7wWCHawuB9yUiH5aj6z2_hImk4bhTBgCUe7XLGbtEbEPL9id28V1Ef1cjqMwtbq88tq3McXNJqkdPiua2wNUjuF5qwvo8eM4DYN43Zh0awsIPpk9PjSRdxKBHhjhDkoA2z7gKhQsihIktjx1c3JXrCQN1HwML7Ojb1bmBrS5ovFhu4igINOAhASeLYpbeq7weryOWnYLmceU44jMlMRpYMnFYUF5C3-GtdOC_Qw1ECweUmmexcxwp0V5EPhc0.0DieYFUEm06MY9KVzpgbx2QP6MGVNGrcOuyPp_U42do&dib_tag=se&keywords=espresso+machine&qid=1721126361&sprefix=spress%2Caps%2C824&sr=8-24",
        "url2" : "https://www.amazon.com/Breville-Barista-Express-Espresso-BES876DBL/dp/B0CGJZW53Q/ref=sr_1_1?crid=39UKAK5LFPY5S&dib=eyJ2IjoiMSJ9.XWw11yiSLkL6CrmPf3YcMjjcYUDV-9tHSC8b_tpuFSZmvYrfTDrUaJW1XYUrqPzOof3w1cpU1Jg5MJCutAxgjRaV39d0Ex5m0qJmzh72nM18OfUwgIZiuZgTxVYSPpM5D2-EAC3-NLI-W5DLPmH_gPJmS7vgXGCgSaln98rEK0M.up61Yfg0EVR82Ddwp_cSR799WTfzw9AUIROBwajaYQI&dib_tag=se&keywords=Breville+Barista+Express+Impress+Espresso+Machine+BES876DBL%2C+Damson+Blue&qid=1721127380&sprefix=breville+barista+express+impress+espresso+machine+bes876dbl%2C+damson+blue%2Caps%2C552&sr=8-1",
        "url3" : "https://www.amazon.com/Hamilton-Beach-Espresso-Machine-Steamer/dp/B003D66TXA/ref=sr_1_27?crid=3PGDS82IRP7ON&dib=eyJ2IjoiMSJ9.-kzrHI0becQBDvbaGQoPjc5KfeJOjc6Eqv2VlU1YegLGfI7wWCHawuB9yUiH5aj6z2_hImk4bhTBgCUe7XLGbtEbEPL9id28V1Ef1cjqMwtbq88tq3McXNJqkdPiua2wNUjuF5qwvo8eM4DYN43Zh0awsIPpk9PjSRdxKBHhjhDkoA2z7gKhQsihIktjx1c3JXrCQN1HwML7Ojb1bmBrS5ovFhu4igINOAhASeLYpbeq7weryOWnYLmceU44jMlMRpYMnFYUF5C3-GtdOC_Qw1ECweUmmexcxwp0V5EPhc0.0DieYFUEm06MY9KVzpgbx2QP6MGVNGrcOuyPp_U42do&dib_tag=se&keywords=espresso+machine&qid=1721126361&sprefix=spress%2Caps%2C824&sr=8-27",
        "url4" : "https://www.amazon.com/Yabano-Espresso-Machine-Cappuccino-Frother/dp/B0BTRWQFZJ/ref=sr_1_32?crid=3PGDS82IRP7ON&dib=eyJ2IjoiMSJ9.-kzrHI0becQBDvbaGQoPjc5KfeJOjc6Eqv2VlU1YegLGfI7wWCHawuB9yUiH5aj6z2_hImk4bhTBgCUe7XLGbtEbEPL9id28V1Ef1cjqMwtbq88tq3McXNJqkdPiua2wNUjuF5qwvo8eM4DYN43Zh0awsIPpk9PjSRdxKBHhjhDkoA2z7gKhQsihIktjx1c3JXrCQN1HwML7Ojb1bmBrS5ovFhu4igINOAhASeLYpbeq7weryOWnYLmceU44jMlMRpYMnFYUF5C3-GtdOC_Qw1ECweUmmexcxwp0V5EPhc0.0DieYFUEm06MY9KVzpgbx2QP6MGVNGrcOuyPp_U42do&dib_tag=se&keywords=espresso+machine&qid=1721126361&sprefix=spress%2Caps%2C824&sr=8-32",
        "url5" :"https://www.amazon.com/Lavazza-Classy-Single-Espresso-Machine/dp/B07RVDJW56/ref=sr_1_22?crid=3PGDS82IRP7ON&dib=eyJ2IjoiMSJ9.-kzrHI0becQBDvbaGQoPjc5KfeJOjc6Eqv2VlU1YegLGfI7wWCHawuB9yUiH5aj6z2_hImk4bhTBgCUe7XLGbtEbEPL9id28V1Ef1cjqMwtbq88tq3McXNJqkdPiua2wNUjuF5qwvo8eM4DYN43Zh0awsIPpk9PjSRdxKBHhjhDkoA2z7gKhQsihIktjx1c3JXrCQN1HwML7Ojb1bmBrS5ovFhu4igINOAhASeLYpbeq7weryOWnYLmceU44jMlMRpYMnFYUF5C3-GtdOC_Qw1ECweUmmexcxwp0V5EPhc0.0DieYFUEm06MY9KVzpgbx2QP6MGVNGrcOuyPp_U42do&dib_tag=se&keywords=espresso+machine&qid=1721126361&sprefix=spress%2Caps%2C824&sr=8-22",
    }
}
urls = {
    "digikala" : {
        "url1" :"https://www.digikala.com/product/dkp-14664702/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%DA%AF%D9%88%D8%B3%D9%88%D9%86%DB%8C%DA%A9-%D9%85%D8%AF%D9%84-gem-873/",
        "url2" : "https://www.digikala.com/product/dkp-1901244/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88%D8%B3%D8%A7%D8%B2-%D9%86%D9%88%D8%A7-%D9%85%D8%AF%D9%84-nova-ncm-128exps/",
        "url3" : "https://www.digikala.com/product/dkp-4836058/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D9%86%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D9%85%D8%AF%D9%84-pixie-en124s",
        "url4" : "https://www.digikala.com/product/dkp-4889296/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D8%AF%D9%88%D9%84%DA%86%D9%87-%DA%AF%D9%88%D8%B3%D8%AA%D9%88-%D9%85%D8%AF%D9%84-mini-me/",
        "url5" : "https://www.digikala.com/product/dkp-2356208/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88%D8%B3%D8%A7%D8%B2-%D8%B2%DB%8C%DA%AF%D9%85%D8%A7-%D9%85%D8%AF%D9%84-rl-222/",
        "url6":"https://www.digikala.com/product/dkp-9870703/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D9%85%D8%A8%D8%A7%D8%B4%DB%8C-%D9%85%D8%AF%D9%84-me-ecm-2034/",
        "url7":"https://www.digikala.com/product/dkp-1929346/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D9%85%D8%A8%D8%A7%D8%B4%DB%8C-%D9%85%D8%AF%D9%84-ecm2010/",
        "url8":  "https://www.digikala.com/product/dkp-2181548/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88%D8%B3%D8%A7%D8%B2-%D9%85%D8%A8%D8%A7%D8%B4%DB%8C-%D9%85%D8%AF%D9%84-ecm2013/",
        "url9":"https://www.digikala.com/product/dkp-14998371/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D9%81%DB%8C%D9%84%DB%8C%D9%BE%D8%B3-%D9%85%D8%AF%D9%84-ep3246/",
        "url10": "https://www.digikala.com/product/dkp-4354974/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B3%D9%88-%D8%B3%D8%A7%D8%B2-%D8%AF%D9%84%D9%88%D9%86%DA%AF%DB%8C-%D9%85%D8%AF%D9%84-ec685/",
    },  
    "olfa" : {
        "url1" : "https://www.olfacoffee.com/product/philips-ep5443-70/",
        "url2" : "https://www.olfacoffee.com/product/%d8%a7%d8%b3%d9%be%d8%b1%d8%b3%d9%88-%d8%b3%d8%a7%d8%b2-%d9%86%d9%88%d8%a7-128/",
        "url3" : "https://www.olfacoffee.com/product/bosch-tis30129rw/",
        "url4" : "https://www.olfacoffee.com/product/delonghi-ec-235/",
        "url5" : "https://www.olfacoffee.com/product/delonghi-ec7-espresso-machine/",
        "url6" :"https://www.olfacoffee.com/product/%d8%a7%d8%b3%d9%be%d8%b1%d8%b3%d9%88-%d8%b3%d8%a7%d8%b2-%d9%85%d8%a8%d8%a7%d8%b4%db%8c-2034-ecm/",
        "url7" :"https://www.olfacoffee.com/product/mebashi-ecm2010/",
        "url8" :"https://www.olfacoffee.com/product/philips-ep3246/",
        "url9" :"https://www.olfacoffee.com/product/sprso-mchin-me-ecm2013/",
        "url510": "https://www.olfacoffee.com/product/delonghi-685/"
    },
    "amazon" : {
        "url1" : "https://www.amazon.com/Breville-BES840XL-Infuser-Espresso-Machine/dp/B0089SSOR6/ref=sr_1_24?crid=3PGDS82IRP7ON&dib=eyJ2IjoiMSJ9.-kzrHI0becQBDvbaGQoPjc5KfeJOjc6Eqv2VlU1YegLGfI7wWCHawuB9yUiH5aj6z2_hImk4bhTBgCUe7XLGbtEbEPL9id28V1Ef1cjqMwtbq88tq3McXNJqkdPiua2wNUjuF5qwvo8eM4DYN43Zh0awsIPpk9PjSRdxKBHhjhDkoA2z7gKhQsihIktjx1c3JXrCQN1HwML7Ojb1bmBrS5ovFhu4igINOAhASeLYpbeq7weryOWnYLmceU44jMlMRpYMnFYUF5C3-GtdOC_Qw1ECweUmmexcxwp0V5EPhc0.0DieYFUEm06MY9KVzpgbx2QP6MGVNGrcOuyPp_U42do&dib_tag=se&keywords=espresso+machine&qid=1721126361&sprefix=spress%2Caps%2C824&sr=8-24",
        "url2" : "https://www.amazon.com/Breville-Barista-Express-Espresso-BES876DBL/dp/B0CGJZW53Q/ref=sr_1_1?crid=39UKAK5LFPY5S&dib=eyJ2IjoiMSJ9.XWw11yiSLkL6CrmPf3YcMjjcYUDV-9tHSC8b_tpuFSZmvYrfTDrUaJW1XYUrqPzOof3w1cpU1Jg5MJCutAxgjRaV39d0Ex5m0qJmzh72nM18OfUwgIZiuZgTxVYSPpM5D2-EAC3-NLI-W5DLPmH_gPJmS7vgXGCgSaln98rEK0M.up61Yfg0EVR82Ddwp_cSR799WTfzw9AUIROBwajaYQI&dib_tag=se&keywords=Breville+Barista+Express+Impress+Espresso+Machine+BES876DBL%2C+Damson+Blue&qid=1721127380&sprefix=breville+barista+express+impress+espresso+machine+bes876dbl%2C+damson+blue%2Caps%2C552&sr=8-1",
        "url3" : "https://www.amazon.com/Hamilton-Beach-Espresso-Machine-Steamer/dp/B003D66TXA/ref=sr_1_27?crid=3PGDS82IRP7ON&dib=eyJ2IjoiMSJ9.-kzrHI0becQBDvbaGQoPjc5KfeJOjc6Eqv2VlU1YegLGfI7wWCHawuB9yUiH5aj6z2_hImk4bhTBgCUe7XLGbtEbEPL9id28V1Ef1cjqMwtbq88tq3McXNJqkdPiua2wNUjuF5qwvo8eM4DYN43Zh0awsIPpk9PjSRdxKBHhjhDkoA2z7gKhQsihIktjx1c3JXrCQN1HwML7Ojb1bmBrS5ovFhu4igINOAhASeLYpbeq7weryOWnYLmceU44jMlMRpYMnFYUF5C3-GtdOC_Qw1ECweUmmexcxwp0V5EPhc0.0DieYFUEm06MY9KVzpgbx2QP6MGVNGrcOuyPp_U42do&dib_tag=se&keywords=espresso+machine&qid=1721126361&sprefix=spress%2Caps%2C824&sr=8-27",
        "url4" : "https://www.amazon.com/Yabano-Espresso-Machine-Cappuccino-Frother/dp/B0BTRWQFZJ/ref=sr_1_32?crid=3PGDS82IRP7ON&dib=eyJ2IjoiMSJ9.-kzrHI0becQBDvbaGQoPjc5KfeJOjc6Eqv2VlU1YegLGfI7wWCHawuB9yUiH5aj6z2_hImk4bhTBgCUe7XLGbtEbEPL9id28V1Ef1cjqMwtbq88tq3McXNJqkdPiua2wNUjuF5qwvo8eM4DYN43Zh0awsIPpk9PjSRdxKBHhjhDkoA2z7gKhQsihIktjx1c3JXrCQN1HwML7Ojb1bmBrS5ovFhu4igINOAhASeLYpbeq7weryOWnYLmceU44jMlMRpYMnFYUF5C3-GtdOC_Qw1ECweUmmexcxwp0V5EPhc0.0DieYFUEm06MY9KVzpgbx2QP6MGVNGrcOuyPp_U42do&dib_tag=se&keywords=espresso+machine&qid=1721126361&sprefix=spress%2Caps%2C824&sr=8-32",
        "url5" :"https://www.amazon.com/Lavazza-Classy-Single-Espresso-Machine/dp/B07RVDJW56/ref=sr_1_22?crid=3PGDS82IRP7ON&dib=eyJ2IjoiMSJ9.-kzrHI0becQBDvbaGQoPjc5KfeJOjc6Eqv2VlU1YegLGfI7wWCHawuB9yUiH5aj6z2_hImk4bhTBgCUe7XLGbtEbEPL9id28V1Ef1cjqMwtbq88tq3McXNJqkdPiua2wNUjuF5qwvo8eM4DYN43Zh0awsIPpk9PjSRdxKBHhjhDkoA2z7gKhQsihIktjx1c3JXrCQN1HwML7Ojb1bmBrS5ovFhu4igINOAhASeLYpbeq7weryOWnYLmceU44jMlMRpYMnFYUF5C3-GtdOC_Qw1ECweUmmexcxwp0V5EPhc0.0DieYFUEm06MY9KVzpgbx2QP6MGVNGrcOuyPp_U42do&dib_tag=se&keywords=espresso+machine&qid=1721126361&sprefix=spress%2Caps%2C824&sr=8-22",
    }
}
#--------------
# تنظیمات صف و لیست
queue_olfa = Queue(100)
list_olfa = []

# اضافه کردن URLها به صف
menu_urls ={
    "digikala": urls["digikala"],
    "olfa": urls["olfa"],
    "amazon": urls["amazon"]
}

for k, v in menu_urls["olfa"].items():
    print(v)
    queue_olfa.put(v)

def scrape_olfa_product_details(queue, result_list):
    while not queue.empty():
        url = queue.get()
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(5)
        page_source = driver.page_source

        # استفاده از BeautifulSoup برای تجزیه HTML
        soup = BeautifulSoup(page_source, 'html.parser')

        # پیدا کردن عنوان محصول
        title_element = soup.find("h1", class_="product_title entry-title wd-entities-title")

        title = title_element.text.strip() if title_element else "عنوان محصول یافت نشد"

        index = title.find('|')
        if index != -1:
           result = title[:index]
        else:
           result = title  # اگر | پیدا نشد، کل متن را برگرداند
        #print(result)

        # پیدا کردن قیمت محصول
        price_element = soup.find("p", class_="price")
        #elementor-widget-container
        price = price_element.text.strip() if price_element else "قیمت یافت نشد"

        # اضافه کردن نتیجه به لیست
        result_list.append({"name_product": result, "price_product": price})

        driver.quit()
        queue.task_done()

# ایجاد و اجرای دو نخ
threads = []
for _ in range(2):
    t = threading.Thread(target=scrape_olfa_product_details, args=(queue_olfa, list_olfa))
    t.start()
    threads.append(t)

# منتظر ماندن تا تمامی نخ‌ها به پایان برسند
for t in threads:
    t.join()

print(list_olfa)



# تبدیل لیست به DataFrame
df_list_olfa = pd.DataFrame(list_olfa, columns=["name_product", "price_product"])
# چاپ DataFrame


df_list_olfa.to_csv('df_list_olfa.csv', index=False)
print(df_list_olfa)




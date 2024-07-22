from queue import Queue
from menu_urls import menu_urls

def crawler_queue(name):
    "This function defines a queue for the crawlers."
    queue = Queue(len(menu_urls[name])) 
    for k, v in menu_urls[name].items():
        print(v)
        queue.put(v)
    return queue

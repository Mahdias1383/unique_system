from queue import Queue
from menu_urls import menu_urls


# def crawler_queue(name,queue):
def crawler_queue(name):
    # queue = Queue(100)
    queue = Queue(len(menu_urls[name]))
    for k, v in menu_urls[name].items():
        print(v)
        queue.put(v)
    return queue
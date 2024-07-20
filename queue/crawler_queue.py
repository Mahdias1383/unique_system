from queue import Queue
#import menuurls


def crawler_queue(name,queue):
    queue = Queue(100)
    for k, v in menu_urls[name].items():
        print(v)
        queue.put(v)
    return queue
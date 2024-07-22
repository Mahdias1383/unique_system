from threading import Thread

def crawler_threads(func,queue,listt):
    "This function create threads for crawlers."
    threads = []
    for _ in range(2):
        t =Thread(target=func, args=(queue,listt))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        
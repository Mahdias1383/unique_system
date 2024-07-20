from threading import Thread


def crawler_threads(func,queue,listt):
    threads = []
    for _ in range(2):
        t =Thread(target=func, args=(queue,listt))
        t.start()
        threads.append(t)

    # منتظر ماندن تا تمامی نخ‌ها به پایان برسند
    for t in threads:
        t.join()
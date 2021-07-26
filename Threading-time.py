import time
import threading

def thread_run():
    print('=====',time.ctime,'=====')
    for i in range(1,50001):
        print('Thread running - ', i)

    threading.Timer(2.5,thread_run).start()

thread_run()
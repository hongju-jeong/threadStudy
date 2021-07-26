import threading

tot = 0

def add_total(amount):
    global tot
    tot += amount
    print(threading.currentThread().getName()+' Not Synchronized :', tot)

if __name__ =='__main__':
    for i in range(10000):
        my_thread = threading.Thread(target=add_total, args=(1,))
        my_thread.start()
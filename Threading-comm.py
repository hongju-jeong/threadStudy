import threading

from queue import Queue

def creator(data, q):

    print('Creating data and putting it on the queue')
    print('\n')
    for item in data:
        evt = threading.Event()
        q.put((item, evt))
        print('Waiting for data to be doubled')
        evt.wait()
    

def consumer(q):

    while True:
        data, evt = q.get()
        print(f'Receive Original Data : {data}')
        processed = data * 5
        print(f'Receive Processed Data : {processed}')
        print('\n')
        evt.set()
        q.task_done()

if __name__ == '__main__':
    q = Queue()
    data = [7,14,39,59,77,1,109,99,167,920,1035]
    thread_one = threading.Thread(target=creator, args=(data, q))
    thread_two = threading.Thread(target=consumer, args=(q,))
    thread_one.start()
    thread_two.start()

    q.join()
    
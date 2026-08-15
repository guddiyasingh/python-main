### Multithrading
## When to use Multi Thrading
###I/O-bound tasks: Tasks That spend more time waiting for I/O operations(e.g., file operation)
### Concurrent execution:When you want to improve the throughput of your applications by python

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter:{letter}")     

##Create 2 threades
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t = time.time()
## Start the thread
t1.start()
t1.start()
## Wait for the threads to complete

t1.join()
t2.join()

finished_time = time.time()-t
print(finished_time)

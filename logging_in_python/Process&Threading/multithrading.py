### Multithrading
## When to use Multi Thrading
###I/O-bound tasks: Tasks That spend more time waiting for I/O operations(e.g., file operation)
### Concurrent execution:When you want to improve the throughput of your applications by python

import threading
import time

def print_numbers():

    for i in range(5):
        print(f"Number: {i}")

def print_letter():
    for letter in "abcde":
        print(f"letter:{letter}")        



t = time.now()
print_numbers()
print_letter

finished_time = time.now()-t







import threading
import requests
from bs4 import BeautifulSoup

urls=[

'https://docs.langchain.com/oss/python/integrations/providers/overview',
'https://docs.langchain.com/oss/python/integrations/providers/overview'
] 

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched{len(soup.text)} characters from {url}')

threads=[]   

for url in urls:

  thread = threading.Thread(target=fetch_content,args=(url,))
  threads.append(thread)
  thread.start()


  for thread in threads:
    thread.join()


print("All web pages fetched")


import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits

## function to compute factorials of a given number

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)

if __name__==" __main__":    
    number=[5000,6000,700,8000]

    start_time=time.time()

## create a pool of worker processes

with multiprocessing.Pool() as pool:
     
     results = pool.map(computor_factorial,numbers)

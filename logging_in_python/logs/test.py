
from logger import logging

def add(a,b):
    logging.debug("The addition operation is takingg place")
    return a+b

logging.debug("The addition functionis called")

add(10,11)
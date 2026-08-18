





import threading
import requests
from bs4 import BeautifulSoup

urls=[

'https://docs.langchain.com/oss/python/integrations/providers/overview'
] 

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched{(len(soup.text))}')
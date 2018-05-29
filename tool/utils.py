from bs4 import BeautifulSoup
import xml
import requests

def aExtract(html):
    soup = BeautifulSoup(html,'xml')
    listlinks = []
    for link in soup.find_all('a'):
        listlinks.append(link.get('href'))
    listlinks2= list(set(listlinks))
    return(listlinks2)

def gethtml(url):
    r = requests.get(url)
    if r.status_code == 200:
       return(aExtract(r.text))


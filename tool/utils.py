from bs4 import BeautifulSoup
import xml, html5lib
import requests

def aExtract(html):
    soup = BeautifulSoup(html,'html5lib')
    listlinks = []
    for link in soup.find_all('a'):
        listlinks.append(link.get('href'))
    listlinks2= list(set(listlinks))
    len1= len(listlinks)
    lenunique = len(listlinks2)
    return(listlinks2,len1,lenunique)

def gethtml(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    r = requests.get(url,headers=headers)

    if r.status_code == 200:
       return(aExtract(r.text))
    else:
        print(r.status_code)
        return('Brak linków',0,0)

def httpresponse(url):
    r = requests.get(url)
    # print(r.headers)
    if r.status_code == 200:
       return(aExtract(r.text))




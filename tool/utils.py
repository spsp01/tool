from bs4 import BeautifulSoup
import xml, html5lib
import requests
from requests.auth import HTTPBasicAuth

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
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
       return(r.headers)
    else:
        return('Błedny kod odpowiedzi: '+ r.status_code)


def senutourl(url):
    r = requests.get(
        'http://dolphin.senuto.com/slowa.php?domain=' + url + '&domain_min=1&domain_max=50&keyword=&type=simple&url='+url+'&searches_min=0&searches_max=&cpc_min=0&cpc_max=&seasonality=0&brand=0&city=0&names=0&ecommerce=0&export=&limit=50000',
        auth=HTTPBasicAuth('senuto', 'SenutO'))
    keywordspair=[]
    position =[]
    for index,i in enumerate(r.text.splitlines()):
        if index > 0:
            kp ={}
            kp['keyword'] = i.split(',')[0].replace('"', '')
            kp['position'] = i.split(',')[1]
            keywordspair.append(kp)
    return(keywords,position)


senutourl('axa.pl/')
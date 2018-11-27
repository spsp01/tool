from bs4 import BeautifulSoup
from random import choice
import csv
import requests
from requests_html import HTMLSession
from requests_html import HTML
from lxml import etree



from requests.auth import HTTPBasicAuth

desktop_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'
]

def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


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

    r = requests.get(url,random_headers())

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

        string=  'Błedny kod odpowiedzi: '+ str(r.status_code)
        header = {'Błąd': string}
        return(header)


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
            kp['llow'] = i.split(',')[3]
            keywordspair.append(kp)
    return(keywordspair)

def getgooglelinks(fraza):

    url_fraza = 'https://www.google.pl/search?q='+fraza+'&num=100&ie=UTF-8&gbv=1'
    r = requests.get(url_fraza,headers=random_headers())
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        h3s= soup.find_all('h3', class_='r')
        urls=[]
        for index,a in enumerate(h3s):
            urls.append(a.find('a').get('href').replace('/url?q=', '').split('&')[0])
        return(urls)
    else:
        return (['Błąd', str(r.status_code)])


def getsitelinks(domain):
    url_site = 'https://www.google.pl/search?q=site%3A'+domain+'&num=100&ie=UTF-8&gbv=1'
    r = requests.get(url_site,headers=random_headers())
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        h3s= soup.find_all('h3', class_='r')
        urls=[]
        for index,a in enumerate(h3s):
            if index > 0:
                urls.append(a.find('a').get('href').replace('/url?q=', '').split('&')[0])
        return(urls)
    else:
        return(['Błąd',str(r.status_code)])


def senutoposition(domain,phrase):
    files= {'file':phrase}
    payload = {'domain':domain}
    r = requests.post('http://dolphin.senuto.com/positions_batch.php', auth=HTTPBasicAuth('senuto', 'SenutO'),files=files, data=payload)
    #print(r.text.encode('UTF-8').split('\n'))
    csv_reader = csv.reader(r.text.splitlines())
    keywords = []

    for i in csv_reader:
        print(i)
        keyword={}
        keyword['keyword']= i[0].replace('Å¼','ż')
        keyword['llow'] = i[1]
        keyword['position'] = i[2]
        keyword['url'] = i[3]
        keywords.append(keyword)
    return keywords


def senutopositioncsv(domain,phrase):
    files= {'file':phrase}
    payload = {'domain':domain}
    r = requests.post('http://dolphin.senuto.com/positions_batch.php', auth=HTTPBasicAuth('senuto', 'SenutO'),files=files, data=payload)

    return r.text.replace('Å¼','ż').encode('UTF-8')

def getlinks(url):
    session = HTMLSession()
    try:
        r = session.get(url)
        links = r.html.absolute_links
        listlinks2 = list(set(r.html.absolute_links))
        len1 = len(r.html.absolute_links)
        lenunique = len(listlinks2)

        return links,len1,lenunique
    except:
        return 'no links'


def linksfromsitemap(sitemap):
    session = HTMLSession()
    r = session.get(sitemap)
    soup = BeautifulSoup(r.text,'lxml')
    result =[]
    for loc in soup.find_all('loc'):
        result.append(loc.text)
    #print(result)
    #print(len(result))
    return result
#linksfromsitemap('https://axa.pl/sitemap.xml')

def geturl(url):
    session = HTMLSession()
    r = session.get(sitemap)
    if r.status_code == 200:
       return(aExtract(r.text))
    else:
        print(r.status_code)
        return('Brak linków',0,0)

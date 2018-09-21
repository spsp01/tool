import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote
from random import choice

desktop_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

def geturlsgoogle(phrase):
    print(phrase)
    r = requests.get('https://www.google.pl/search?num=50&q='+ str(phrase),headers=random_headers())
    soup = BeautifulSoup(r.text, 'lxml')
    print(r.status_code)
    b= soup.find_all('h3',class_='r')
    urls= []
    domains =[]
    for index,a in enumerate(b):
       c= a.find('a')
       print(c)
       urlgoogle =c.get('href').replace('/url?q=','').split('&')[0]
       urls.append(unquote(urlgoogle))
       domains.append(urlparse(urlgoogle).hostname.replace("www.", ""))

    return(urls,domains)


def getposition(phrase,domain):
        urls, domains = geturlsgoogle(phrase)
        if domain in domains:
            response = phrase+','+str(domains.index(domain) + 1) +',' + str(urls[domains.index(domain)])
            return response
        else:
            return '>100, N/A'

#print(getposition('odkurzacze workowe','tefal.pl'))


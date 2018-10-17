import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote
from random import choice
from tool.utils.selposition import selhtml
import time

desktop_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', }

# def cookie():
#     a = {
#
#         'NID': '141=JebGgzpCsVhu-KXo9OrdynKiccH4DL0kd8MQ6NxAyKSPXwGlMDZUw4ZM0T-UZyydwFLSO0TTIqbCmBfTsyebGxXJMXkOxMReKM5wVVEH439DoBKBzzH_hbKQJTD0s8iFcazdGXXV0BORxqoJpNvhffa0h50ZJTIOOV8DJ5vJO23DGYdxJZP-5rgEK8NrWd1X0s9ll3n0StOVdcBCELfqAumlTljPVwXfka4',
#         'SID': 'PwUtHtQnSg-y4UCUx9Hs7iAklslOgaPDAmEvXnV30q6X_ATY_gKWFUlOxurTQOT7B-6Mvw.',
#         'HSID': 'A0-svrqsRt3dCxBhs',
#         'SSID': 'AIpCmc8ZS7XCB_zsB; APISID=q2y0jSsn6IvxaueT/AOD2vvMhzF_etQq-p',
#         'SAPISID': 'mMvRdRLwI3knq1ZT/Aa0XPjfxEME61jQWV',
#         'SIDCC': 'AGIhQKR3Rb58V12XGysbUUQI3mbkZSV118KmV7EhJRX-JU99eE4HSc3ncLXILH9eQX-_c27k3jcIMZaKYgOvvQ',
#         'aixefrbalt': '1529656836',
#         '1P_JAR': '2018-10-16-08',
#         'OGP': '-5061451:',
#         'DV': 'U2FHBnfbBO1dYM2vjpxIRaWvkc7AZ1b59w-9auHsKgEAADBLuKqlTTtk8gAAAMTbFnEOG9rMTgAAAOj7wmvlvcZsFAAAAA',
#     }
#     return a
def geturlsgoogle(phrase):

    r = requests.get('https://www.google.pl/search?num=50&q='+ str(phrase)+'&gbv=1',headers=random_headers())
    soup = BeautifulSoup(r.text, 'lxml')
    b= soup.find_all('h3',class_='r')
    print(r.status_code)
    print(r.cookies)
    if r.status_code == 200:
        urls= []
        domains =[]
        for index,a in enumerate(b):
           c = a.find('a')
           if c.get('href').find('/search?q='):
               urlgoogle =c.get('href').replace('/url?q=','').split('&')[0]
               urls.append(unquote(urlgoogle))
               domains.append(urlparse(urlgoogle).hostname.replace("www.", ""))

        return(urls,domains)
    else:
        urls, domains= selhtml(phrase)
        return (urls, domains)


def getposition(phrase,domain):
        phrase_plus= phrase.replace(' ','+')
        print(phrase_plus)

        urls, domains = geturlsgoogle(phrase)

        if domain in domains:
            response = phrase+','+str(domains.index(domain) + 1) +',' + str(urls[domains.index(domain)])
            return response
        else:
            return str(phrase)+ ', >100, N/A'

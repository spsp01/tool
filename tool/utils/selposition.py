from selenium import webdriver
from urllib.parse import urlparse, unquote
import time

def selpoz(phrase,driver):
    dchrome= driver
    url_phrase = 'https://www.google.pl/search?q='+phrase
    base_url = dchrome.get(url_phrase)
    urlssel = dchrome.find_elements_by_css_selector('div.r a')
    urls = []
    domains =[]
    for index, i in enumerate(urlssel):
        url = i.get_property('href')
        if i.get_attribute('class') == '':
             urls.append(url)
             domains.append(urlparse(url).hostname.replace("www.", ""))
    return urls,domains


def startchrome(lista,domain):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    dchrome = webdriver.Chrome(chrome_options=options)
    results =[]
    for i in lista:
        urls, domains = selpoz(i,dchrome)
        if domain in domains:
            response = i + ',' + str(domains.index(domain) + 1) + ',' + str(urls[domains.index(domain)])
            results.append(response)
        else:
            results.append(str(i) + ', >100, N/A')
        time.sleep(1)

    dchrome.close()
    return(results)


lista= ['ubezpieczenia','ubezpieczenie ac','axa']
print(startchrome(lista,'axa.pl'))

def generatelist(arr, size):
    arrs = []
    while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
    arrs.append(arr)
    return arrs

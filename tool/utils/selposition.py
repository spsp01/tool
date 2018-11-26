from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse, unquote
import time

def selpoz(phrase,driver):
    dchrome= driver
    url_phrase = 'https://www.google.pl/search?q='+phrase+'&oq='+phrase+'&num=50&sourceid=chrome&ie=UTF-8'
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



def selhtml(phrase):

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    dchrome = webdriver.Chrome()

    url_phrase = 'https://www.google.pl/search?q='+phrase+'&num=50'
    base_url = dchrome.get(url_phrase)
    urlssel = dchrome.find_elements_by_css_selector('div.r a')
    urls = []
    domains =[]
    for index, i in enumerate(urlssel):
        url = i.get_property('href')
        if i.get_attribute('class') == '':
             urls.append(url)
             domains.append(urlparse(url).hostname.replace("www.", ""))
    dchrome.close()
    return urls,domains

def generatelist(arr, size):
    arrs = []
    while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
    arrs.append(arr)
    return arrs

def seltest():
       dchrome = webdriver.Firefox()
       dchrome.add_cookie({})

def selgoogle(phrase):
    #using next function
    dchrome = webdriver.Firefox()

    url_phrase = 'https://www.google.pl/search?q='+phrase
    base_url = dchrome.get(url_phrase)
    print(dchrome.page_source)
    urls= []
    for x in range(0, 4):
       urls.extend(divr(dchrome))
       time.sleep(2)
       dchrome.find_element_by_id('pnnext').click()
    urls.extend(divr(dchrome))
    return urls

def divr(driver):
    urlssel = driver.find_elements_by_css_selector('div.r a')
    urls = []
    for index, i in enumerate(urlssel):
        url = i.get_property('href')
        if i.get_attribute('class') == '':
            urls.append(url)
    return urls

# for index, i in enumerate(selgoogle('ubezpieczenia ac')):
#     print(index,' ',i)
# for index, i in enumerate(selhtml('ubezpieczenia ac')):
#     print(index,' ',i)
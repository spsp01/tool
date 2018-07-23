from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import requests


#Headless Chrome
def top50g(keyword):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    d = webdriver.Chrome(chrome_options=chrome_options)
    url_keyword = 'https://www.google.pl/search?q='+keyword+'&num=50'
    base_url = d.get(url_keyword)
    a = d.find_elements_by_css_selector('h3.r a')
    urls = []
    for i in a:
        urls.append(i.get_attribute('href'))
    return(urls)

#Requests
def geturltext(keyword):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    url= 'https://www.google.pl/search?q=' + keyword + '&num=50'
    r = requests.get(url,headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,'lxml')
        a = soup.select("h3.r a['href']")
        urls =[]
        for i in a:
            urls.append(i['href'])
    print(urls)
    return(urls)


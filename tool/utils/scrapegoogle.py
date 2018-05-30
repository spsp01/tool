from selenium import webdriver
from bs4 import BeautifulSoup

def top50g():
    d = webdriver.Chrome()
    url_fraza = 'https://www.google.pl/search?q=mleko modyfikowane&num=50'
    base_url = d.get(url_fraza)
    a = d.find_elements_by_css_selector('h3.r a')
    urls = []
    for i in a:
        urls.append(i.get_attribute('href'))
    print(urls)
    return(urls)


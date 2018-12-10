from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pickle
import random
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import time




def getcookie(folder,user,password):

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=E:\\chromeusers\\"+folder)
    dchrome = webdriver.Chrome(chrome_options=options)
    url_phrase = 'https://google.com/'
    base_url = dchrome.get(url_phrase)
    dchrome.find_element_by_id('gb_70').click()
    time.sleep(1)
    dchrome.find_element_by_xpath('//*[@id="identifierId"]').click()
    login= user
    dchrome.find_element_by_id('identifierId').send_keys(login)
    dchrome.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span').click()
    time.sleep(1)
    passwd = password
    dchrome.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(passwd)
    dchrome.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span').click()
    pickle.dump(dchrome.get_cookies(), open("cookies_google.pkl", "wb"))
    time.sleep(3)
    print(dchrome.get_cookies())



def opengoogle():

    # cookies = pickle.load(open("cookies_google.pkl", "rb"))

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=E:\\chromeusers\\marcelina")
    dchrome = webdriver.Chrome(chrome_options=options)
    dchrome.get('https://onet.pl')
    time.sleep(2)
    dchrome.get('https://google.com/')
    # for i in cookies:
    #      dchrome.add_cookie(i)
    #
    # dchrome.get('https://google.com/')

#opengoogle()

def openfirefox():
    binary = "C:\\Users\\Jarek\\Anaconda3\\Scripts\\geckodriver.exe"
    profile= webdriver.FirefoxProfile(profile_directory='C:\\Users\\Jarek\\Desktop\\temp')
    driver = webdriver.Firefox(firefox_profile=profile,firefox_binary=binary)
    driver.get('https://google.com')
    #driver.quit()

#openfirefox()

def readcookie():
    cookies = pickle.load(open("cookies_google.pkl", "rb"))
    for i in cookies:
        print(i)

        # cookies = pickle.load(open("cookies_google.pkl", "rb"))

        # dchrome.get('https://onet.pl')
        # time.sleep(2)
        # dchrome.get('https://google.com/')
        # for i in cookies:
        #      dchrome.add_cookie(i)
        #
        # dchrome.get('https://google.com/')




class Opengoogle():
    def __init__(self,user):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=E:\\chromeusers\\"+user)
        options.add_experimental_option("detach", True)
        self.dchrome = webdriver.Chrome(chrome_options=options)

    def getadress(self, url):
        self.dchrome.get(url)

    def gettext(self):
        return self.dchrome.page_source

    def getlinks(self):
        urlssel = self.dchrome.find_elements_by_css_selector('div.r a')
        urls = []
        domains = []
        for index, i in enumerate(urlssel):
            url = i.get_property('href')
            if i.get_attribute('class') == '':
                urls.append(url)
                domains.append(urlparse(url).hostname.replace("www.", ""))
        return(urls,domains)
        #print(domains,urls)
    def get_position(self,domain,phrase):
        domain = domain
        results = []
        urls, domains = self.getlinks()
        if domain in domains:
            response = phrase + ',' + str(domains.index(domain) + 1) + ',' + str(urls[domains.index(domain)])
            results.append(response)
        else:
            results.append(str(phrase) + ', >100, N/A')
        return results


def scrapeadress(lista,domain):
    profiles = ['temp', 'hanna','marcelina']

    dividedlist = dividelist(lista,40)
    response = []
    print(dividedlist)
    for divl in dividedlist:
        if profiles == []:
            profiles = ['temp', 'hanna','marcelina']
        randomprof = random.choice(profiles)
        profiles.remove(randomprof)
        a = Opengoogle(randomprof)
        a.getadress('https://www.google.pl/search?q='+divl[0])
        time.sleep(2)
        for index,phrase in enumerate(divl):
            print(index)
            if index % 5 == 0 and index % 10 != 0:
                a.getadress('https://www.google.com/search?q='+phrase)
            if index % 10 == 0 and index !=0:
                a.getadress('https://www.google.pl/search?q='+phrase)
            search = a.dchrome.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[1]/input')
            search.clear()
            search.send_keys(phrase)
            search.send_keys(Keys.ENTER)
            response.append(a.get_position(domain,phrase))
            time.sleep(random.random()*31)
            if index % 10 == 0:
                time.sleep(random.random() * 100)
                print('sleep')
        a.dchrome.quit()
    return response

def dividelist(lista,n):
    return [lista[i:i + n] for i in range(0, len(lista), n)]



#print(scrapeadress(['ford', 'focus silniki', 'ford focus colorado red', 'ford focus promocje', 'focus części', 'ford focus zdjęcia', 'ford focus katalog', 'ford focus abs', 'ford focus silniki', 'ford focus wnętrze', 'dealerzy forda', 'części samochodowe ford focus', 'focus chill', 'ford focus bagażnik', 'ford focus frozen white', 'ford focus st cena', 'isofix', 'salony forda', 'samochody ford', 'focus abs', 'fordpower', 'ford dealerzy', 'ford key free', 'reflektory ksenonowe', 'części do forda focusa', 'czujniki ciśnienia w oponach', 'focus galeria', 'focus rs cena', 'focus gps', 'focus econetic', 'ford focus individual', 'ford focus silnik', 'ford focus gps', 'bluetooth ford', 'samochody ford focus', 'dealer forda', 'abs ford focus', 'układ wspomagania kierownicy', 'nowy ford focus', 'ford focus kombi', 'czujnik ciśnienia w oponach', 'ford focus rs cena', 'salon forda', 'nowy focus', 'ford focus części', 'focus dane techniczne', 'podgrzewane fotele', 'części samochodowe ford', 'filtr przeciwpyłkowy', 'ford kinetic design', 'focus duratec', 'ford focus chill', 'czujniki parkowania', 'ford focus bluetooth', 'ford easy fuel', 'ford focus econetic', 'ford powershift', 'ford focus dane techniczne', 'czujnik parkowania', 'samochody osobowe', 'ford focus', 'focus', 'focus titanium', 'ford focus turbo', 'focus ambiente', 'focus esp', 'ford focus esp', 'bezpieczne samochody', 'focus trend', 'ford focus titanium', 'focus ghia', 'ford focus trend', 'wspomaganie parkowania', 'parkowanie równoległe tyłem', 'dane techniczne ford focus', 'ford focus cena', 'c max', 'samochód rodzinny', 'auta 7 osobowe', 'samochody 7 osobowe', 'transit', 'tourneo', 's-max', 'ranger', 'mondeo', 'kuga', 'ka', 'galaxy', 'ford transit', 'ford tourneo', 'ford s-max', 'ford ranger', 'ford porady', 'ford mondeo', 'ford kuga', 'ford ka', 'ford galaxy', 'ford fiesta', 'ford c-max', 'focus sedan', 'focus rs', 'fiesta', 'nowy ford fiesta cena ', 'fiesta mk8', 'ford fiesta 2012', 'fiesta 2012', 'nowy ford fiesta', 'nowa fiesta', 'b max', 'ford b max', 'b max silniki', 'b max dane techniczne', 'b max 2012', 'b max bez słupka', 'ford focus 2012', 'focus st 2012', 'focus st dane techniczne', 'ecoboost', 'ford focus st', 'focus st', 'nowy ford focus st', 'ford kuga wymiary', 'ford kuga cena', 'ford transit wymiary', 'b-max', 'ford transit opinie', 'ford kuga opinie', 'nowa kuga', 'bmax', 'ford bmax', 'ford b-max cena', 'ford kuga spalanie', 'nowy ford kuga', 'ford transit spalanie', 'ford transit dane techniczne', 'ford b-max', 'mondeo mk5', 'nowe mondeo', 'nowe mondeo 2013', 'nowy mondeo', 'nowe mondeo 2012', 'ford mondeo mk5', 'nowy ford mondeo 2012', 'nowy ford mondeo 2013', 'mondeo 2013', 'mondeo 2012', 'ford mondeo 2012', 'nowy ford mondeo', 'ford ka wymiary', 'c-max dane techniczne', 'porady motoryzacyjne', 'targi motoryzacyjne frankfurt', 'targi samochodowe frankfurt', 'oszczędne samochody', 'ford ranger wildtrak', 'fiesta dane techniczne', 'najlepszy silnik benzynowy', 's max spalanie', 'ekonomiczne auta', 'samochody z gwarancją', 'ford samochody używane', 'c max spalanie', 'nowy ford mustang', 'ford focus iii', 'auto 7 osobowe', 'asystent parkowania', 'ford mondeo titanium', 'nowy mustang', 'ford focus 3', 'ford focus kombi wymiary', 'ford kuga dane techniczne', 'kredyt na samochód używany', 'mustang 2015', 'ford mustang 2015', 'ekonomiczne samochody', 'ford fiesta wymiary', 'ford c-max dane techniczne', 'ford c max spalanie', 'focus c max', 'samochód używany', 'auta dostawcze', 'auta osobowe', 'ford c max wymiary', 'ford focus 2013', 'ford fiesta dane techniczne', 'ford courier', 'ford focus wymiary', 'auta nowe', 'ford fiesta 2013', 'nowe auta', 'ford k', 'ford mondeo kombi', 'samochody używane z gwarancją', 'samochody nowe', 'ford focus c max', 'connect', 'leasing samochodu', 'leasing samochodowy', 'nowe samochody', 'samochody dostawcze', 'ford mustang', 'mustang', 'samochody'],'ford.pl'))
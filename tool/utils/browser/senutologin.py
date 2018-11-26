from selenium import webdriver
import pickle
import requests

def getcookie():
    dchrome = webdriver.Chrome()
    url_phrase = 'https://app.senuto.com/users/login'
    base_url = dchrome.get(url_phrase)
    login= 'bazaz@performance-media.pl'
    passwd ='201818!@#gPMedia%$#'
    dchrome.find_element_by_id('hs-eu-confirmation-button').click()
    dchrome.find_element_by_name('email').send_keys(login)
    dchrome.find_element_by_name('password').send_keys(passwd)
    dchrome.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/form/div[3]/div/button').click()
    pickle.dump(dchrome.get_cookies() , open("cookies.pkl","wb"))



def getinfo():
    dchrome = webdriver.Chrome()
    url_phrase = 'https://app.senuto.com/'
    base_url = dchrome.get(url_phrase)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        dchrome.add_cookie(cookie)
    ready_url = dchrome.get(url_phrase)


def readinfo(domain,url):

    s = requests.Session()
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        #print(cookie)
        s.cookies.set(cookie['name'], cookie['value'])
    r= s.get('https://app.senuto.com/')
    #payload ='module=Explorer&grid=Top50Keywords&params%5Burl%5D='+domain+'&params%5Bformat%5D=1&params%5Bdisplay%5D=w&params%5Blanguage%5D=pl&draw=2&columns%5B0%5D%5Bdata%5D=keyword&columns%5B0%5D%5Bname%5D=keyword&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=position&columns%5B1%5D%5Bname%5D=position&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=cpc&columns%5B2%5D%5Bname%5D=cpc&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=words_count&columns%5B3%5D%5Bname%5D=words_count&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=trends&columns%5B4%5D%5Bname%5D=trends&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=searches&columns%5B5%5D%5Bname%5D=searches&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=updated&columns%5B6%5D%5Bname%5D=updated&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=difficulty&columns%5B7%5D%5Bname%5D=difficulty&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=domain&columns%5B8%5D%5Bname%5D=domain&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=5&order%5B0%5D%5Bdir%5D=desc&start=0&length=100&search%5Bvalue%5D=&search%5Bregex%5D=false'
    payload ='module=Explorer&grid=PositionsHistory&params%5Burl%5D='+domain+'&params%5Bformat%5D=1&params%5Bdisplay%5D=w&params%5Blanguage%5D=pl&params%5Bfilters%5D%5B0%5D%5Bcomplement%5D=true&params%5Bfilters%5D%5B0%5D%5Bkey%5D=domain&params%5Bfilters%5D%5B0%5D%5Bmatch%5D=equals&params%5Bfilters%5D%5B0%5D%5BmatchType%5D=url&params%5Bfilters%5D%5B0%5D%5Bvalue%5D='+url+'&draw=1&columns%5B0%5D%5Bdata%5D=keyword&columns%5B0%5D%5Bname%5D=keyword&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=searches&columns%5B1%5D%5Bname%5D=searches&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=position&columns%5B2%5D%5Bname%5D=position&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=positionsChange&columns%5B3%5D%5Bname%5D=positionsChange&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=positionsMonthlyHistory&columns%5B4%5D%5Bname%5D=positionsMonthlyHistory&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=positionsHistory&columns%5B5%5D%5Bname%5D=positionsHistory&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=cpc&columns%5B6%5D%5Bname%5D=cpc&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=difficulty&columns%5B7%5D%5Bname%5D=difficulty&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=domain&columns%5B8%5D%5Bname%5D=domain&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false'
    headers = {
        'Host': "app.senuto.com",
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Accept': "application/json, text/plain, */*",
        'Origin': "https://app.senuto.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded",
        'Referer': "https://app.senuto.com/keywords-base",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "pl,en-US;q=0.9,en;q=0.8,de;q=0.7",
    }
    u = s.post('https://app.senuto.com/grids', data=payload,headers=headers)


    for i in u.json()['data']:
        print(i['keyword']+' '+i['domain'])

    a = open("slowa.json","w")
    a.write(u.text)
    a.close()
readinfo('axa.pl','axa.pl/')






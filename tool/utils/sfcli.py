from urllib.parse import urlparse
import os
from pathlib import Path
import datetime

def getdomain(url):
    # Returns domain from url
    domain = urlparse(url).hostname.replace("www.", "")
    return domain

def pathwindows(domain):
    x = datetime.datetime.now()
    today = str(x.day) + '-' + str(x.month) + '-' + str(x.year)
    path = Path('E:', '/', 'screaming','crawl', domain,today)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def startsf(url):
    string = 'ScreamingFrogSEOSpiderCli -crawl ' + url +' --headless --overwrite --save-crawl --export-tabs "Internal:All" '+isconfigin(getdomain(url)) +' --output-folder ' + str(pathwindows(getdomain(url)))
    print(string)
    os.system(string)
    return 'OK'

def getfile():
    b = os.walk('E:/screaming/crawl')
    c = list(b)
    files = []
    for index,i in enumerate(c):
        if index>0 and index%2==0:
            try:
                a= i[0].split("\\")[1]
                b=i[0].split("\\")[2]
                c= str(a)+', '+ str(b)+', '+ str(i[-1][0])
                d =str(a)+', '+ str(b)+', '+ str(i[-1][1])
                files.append(c)
                files.append(d)
            except:
                files.append('>NA')

    return files

def getconfig():
    files = os.listdir('E:/screaming/config')
    configs = []
    for i in files:
        configs.append(i.replace('.seospiderconfig','').replace('_','.'))

    return configs


def isconfigin(domain):
    if domain in getconfig():
        return '--config E:/screaming/config/' + domain.replace('.','_')+'.seospiderconfig'
    return ''
from urllib.parse import urlparse
import os
from pathlib import Path
import datetime
import subprocess

def getdomain(url):
    # Returns domain from url
    print(url)
    if 'www' in url:
        domain = urlparse(url).hostname.replace("www.", "")
    else:
        domain = urlparse(url).hostname
    print(domain)
    return domain

def pathwindows(domain,folder,subfolder):
    x = datetime.datetime.now()
    today = str(x.day) + '-' + str(x.month) + '-' + str(x.year)

    if subfolder != '':
         path = Path('E:', '/', folder,subfolder, domain,today)
    else:
         path = Path('E:', '/', folder, domain, today)

    if not os.path.exists(path):
        os.makedirs(path)
    return path


# def startsf(url):
#     string = 'ScreamingFrogSEOSpiderCli -crawl ' + url +' --headless --overwrite --save-crawl --export-tabs "Internal:All" '+isconfigin(getdomain(url)) +' --output-folder ' + str(pathwindows(getdomain(url),'screaming','crawl'))
#     print(string)
#     subprocess.run(string,shell=True, check=True)
#     return 'OK'

def getfile():
    b = os.walk('E:/screaming/crawl')
    c = list(b)

    files = []
    for index,i in enumerate(c):
        if index>0:
            try:
                if i[-1] != []:
                    a= i[0].split("\\")[1]
                    b=i[0].split("\\")[2]
                    c= str(a)+', '+ str(b)+', '+ str(i[-1][0])
                    d =str(a)+', '+ str(b)+', '+ str(i[-1][1])
                    try:
                        e = str(a) + ', ' + str(b) + ', ' + str(i[-1][2])
                    except:
                        e=('N/A')
                    files.append(c)
                    files.append(d)
                    files.append(e)
            except:
                files.append('>NA')
    #print(files)
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

def startsf(url):
    print(url)
    string = 'ScreamingFrogSEOSpiderCli -crawl ' + url +' --headless --overwrite --save-crawl --save-report "Crawl Overview" --export-tabs "Internal:All" '+isconfigin(getdomain(url)) +' --output-folder ' + str(pathwindows(getdomain(url),'screaming','crawl'))
    print(string)
    subprocess.run(string,shell=True, check=True)
    return 'OK'


def geturl(url):
    # Returns domain from url
    if not 'http' in url:
        return url


    path = urlparse(url).netloc.replace("www.", "") +urlparse(url).path
    if path.endswith('/'):
        path = path[:-1]
    pathdash = path.replace('/','-')

    return pathdash


def cleanurl(url):
    if '?' in url:
        urlclean= url.split('?')[0]
        return urlclean
    return url

def startlighthouse(url):
    string = 'lighthouse '+cleanurl(url)+' --chrome-flags="--headless" --output=json --output-path='+str(pathwindows(getdomain(url),'lighthouse',''))+'\\' + geturl(url)+'.json'
    print(string)
    subprocess.run(string,shell=True, check=True)
    return 'OK'


def startlighthousebatch(url):
    string = 'lighthouse '+cleanurl(url)+' --chrome-flags="--headless" --output=json --output-path='+str(Path('E:', '/','batch',geturl(url)+'.json'))
    print(string)
    subprocess.run(string,shell=True, check=True)
    return 'OK'

# listurl= ['https://axa.pl','https://axa.pl/ubezpieczenie-zycie-i-zdrowie/','https://kobieceinspiracje.pl/kulinaria/119506,podudzia-faszerowane-miesem-mielonym-w-sosie-orientalnym-z-papryka-z-jednej-patelni.html']
#
# for i in listurl:
#     startlighthousebatch(i)
# def readoutput():
#     p= subprocess.Popen('dir',shell=True,  stdout=subprocess.PIPE)



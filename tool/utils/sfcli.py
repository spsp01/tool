from urllib.parse import urlparse
import os
from pathlib import Path
import datetime

def getdomain(url):
    domain = urlparse(url).hostname.replace("www.", "").replace('.','_')
    return domain

def pathwindows(domain):
    x = datetime.datetime.now()
    today = str(x.day) + '-' + str(x.month) + '-' + str(x.year)
    path = Path('E:', '/', 'crawl', domain,today)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def startsf(url):
    string = 'ScreamingFrogSEOSpiderCli -crawl ' + url +' --headless --overwrite --save-crawl --export-tabs "Internal:All" --output-folder ' + str(pathwindows(getdomain(url)))
    os.system(string)
    return 'OK'








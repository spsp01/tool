import requests
KEY = 'AIzaSyB2XIGtpjln8Og61TDFv9AiYfvHFLAHTzQ'

def createurljson(url,type):
    urljson='https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url='+url+'&strategy='+type + '&key='+KEY
    return urljson

def download(url):
    urljson = createurljson(url,'desktop')
    req = requests.get(urljson, timeout=15).json()
    string = url+';'+str(req['ruleGroups']['SPEED']['score'])+';'+str(req['pageStats']['numberHosts'])+';'+str(req['pageStats']['numberJsResources'])+';'+str(req['pageStats']['numberCssResources'])+';'+str(req['pageStats']['numberResources'])+';'+str(req['pageStats']['imageResponseBytes'])
    print(string)
    return string
    # print('Page Speed Result: '+ str(req['ruleGroups']['SPEED']['score']))
    # print('Number of host: '+str(req['pageStats']['numberHosts']))
    # print('JS Resources: '+str(req['pageStats']['numberJsResources']))
    # print('CSS Resources: '+str(req['pageStats']['numberCssResources']))
    # print('Total Resources: '+str(req['pageStats']['numberResources']))
    # print('Total Image Size (in kb): '+str(req['pageStats']['imageResponseBytes']))

#download('https://www.dyson.pl/suszarki-do-rak/airblade-v.aspx')
with open('urls.txt','r',encoding='UTF-8') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    with open('csvfile.csv', 'a', encoding='UTF-8') as file:
        for i in content:
            file.write(download(i))
            file.write('\n')
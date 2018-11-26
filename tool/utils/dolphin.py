import requests
import json

def getapi(domain,param,action):
    if action == 0:
        url= 'http://dolphin.senuto.com/api.php?key=pm_c05f6c233521207f6fe311afef550c3c&domain='+str(domain)+'&type='+str(param)
    else:
        url = 'http://dolphin.senuto.com/api.php?key=pm_c05f6c233521207f6fe311afef550c3c&domain=' + str(domain) + '&type=' + str(param)+'&action='+str(action)
    r = requests.get(url)
    data = json.loads(r.text)
    return(data)

def phrases_from_end(json,rangetop,number):
    last = list(json[str(rangetop)].values())[number]
    return last

def phrases_difference(json,rangetop):
    #returns substraction from last 2 values
    diff = phrases_from_end(json,rangetop,-1) - phrases_from_end(json,rangetop,-2)
    return diff

def test():
    keywords_stats=getapi('axa.pl','weekly','domain_keywords_stats')
    keywords_characteristic = getapi('axa.pl','weekly','domain_keywords_characteristic')
    domain_seasonality = getapi('axa.pl','weekly','domain_seasonality')
    domain_keywords_cloud = getapi('axa.pl','weekly','domain_keywords_cloud')
    domain_competitors = getapi('axa.pl','weekly','domain_competitors')
    print(keywords_stats)
    print(keywords_characteristic)
    print(domain_seasonality)
    print(domain_keywords_cloud)
    print(domain_competitors)


    # print(phrases_from_end(jsonfile,'top3',-1))
    # print(phrases_from_end(jsonfile, 'top3', -2))
    # print(phrases_difference(jsonfile,'top3'))

#test()


#all - wszystkie możliwe dane w jednym zapytaniu.
# domain_keywords_history - historia statystyk słów kluczowych top3/top10/top50
# domain_keywords_stats - aktualne statystyki top3/top10/top50
#
# domain_seasonality - sezonowość domeny (miesiąc po miesiącu [1-12])
#
# domain_keywords_characteristic - charakterystyka słów domeny (liczba słów z imionami, miastami lub brandem)
#
# domain_keywords_cloud - 500 najczęściej występujących słów we frazach na które domena występuje w top50
#
# domain_competitors - lista najczęściej występujących domen w top10 na słowa kluczowe podanej domeny w top50
#
# domain_keywords_top - po 200 fraz z pozycji 1-3, 4-10 i 11-50
#
# domain_ads_stats - wyciąga informację na temat reklam AdWords w ramach widoczności danej domeny



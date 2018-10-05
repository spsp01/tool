import json

filejson ='E:\lighthouse\\axa.pl\\5-10-2018\\axa.pl.json'

with open(filejson,'r',encoding='UTF-8') as read_file:
    data = json.load(read_file)

    for b in data['audits'].keys():
      print(b)

    first_contentful_paint = data['audits']['first-contentful-paint']
    speedindex = data['audits']['speed-index']['displayValue']
    mobile_friendly = data['audits']['mobile-friendly']['title']
    https = data['audits']['is-on-https']['title']
    robots_txt =data['audits']['robots-txt']
    crawlable = data['audits']['is-crawlable']['title']
    canonical = data['audits']['canonical']['title']
    meta_description = data['audits']['meta-description']['title']
    metrics = data['audits']['metrics']
    structured_data = data['audits']['structured-data']
    plugins = data['audits']['plugins']
    hreflang = data['audits']['hreflang']
    link_text = data['audits']['link-text']
    font_size = data['audits']['font-size']
    http_status_code = data['audits']['http-status-code']

    print(first_contentful_paint)


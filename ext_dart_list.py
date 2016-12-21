import json
import urllib2

url_quote = 'http://dart.fss.or.kr/api/search.json?auth=0163d3df4b40f223395ed5e93c38e947b42b9414&page_set=100'

def CollectPrices(url):
    f = urllib2.urlopen(url)
    page = f.read()
    f.close()
    js = json.loads(page)
    return js

DARTInfo = CollectPrices(url_quote)

i = 0

for el in DARTInfo['list']:
    if DARTInfo['list'][i]['crp_cls'] == "K" or DARTInfo['list'][i]['crp_cls'] == "Y":
        print i+1, \
              DARTInfo['list'][i]['crp_cls'], \
              DARTInfo['list'][i]['crp_nm'], \
              DARTInfo['list'][i]['crp_cd'], \
              DARTInfo['list'][i]['rpt_nm']
    i = i + 1

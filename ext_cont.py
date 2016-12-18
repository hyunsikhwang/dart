import requests
import lxml
from lxml import html

r = requests.get('http://dart.fss.or.kr/report/viewer.do?rcpNo=20160809800398&dcmNo=5249424&eleId=0&offset=0&length=0&dtd=HTML')
tree = lxml.html.fromstring(r.content)
elements = tree.xpath('//span')

count = 0

for el in elements:
    count = count + 1
    if el.text_content() == u'매출액' or \
    el.text_content() == u'영업이익' or \
    el.text_content() == u'법인세비용차감전계속사업이익' or \
    el.text_content() == u'당기순이익':
        print count, el.text_content()

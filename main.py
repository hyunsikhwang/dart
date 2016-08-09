import lxml.html

url = 'http://finance.daum.net/quote/all.daum?type=S&stype=P'
url2 = 'http://dart.fss.or.kr/report/viewer.do?rcpNo=20160809800398&dcmNo=5249424&eleId=0&offset=0&length=0&dtd=HTML'

html = lxml.html.parse(url2)
# packages = html.xpath('//tr/td/a/text()') # get the text inside all "<tr><td><a ...>text</a></td></tr>"
# packages = html.xpath('//table[@class="gTable clr"]/tr/td/span/text()') # get the text inside all "<tr><td><a ...>text</a></td></tr>"
# print packages

packages = html.xpath('//table/tbody/tr/td/span[@class="xforms_input"]/text()')
# test = html.xpath("//tr/td/a/@href")

A = {}
i = 0

for stname in packages:
    A[i] = stname
    # A[i] = stname[-6:]
    print A[i]
    i=i+1

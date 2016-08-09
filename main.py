import lxml.html

url='http://finance.daum.net/quote/all.daum?type=S&stype=P'

html = lxml.html.parse(url)
# packages = html.xpath('//tr/td/a/text()') # get the text inside all "<tr><td><a ...>text</a></td></tr>"
packages = html.xpath('//table[@class="gTable clr"]/tr/td/span/text()') # get the text inside all "<tr><td><a ...>text</a></td></tr>"
# print packages
test=html.xpath("//tr/td/a/@href")

A = {}
i = 0

for stname in packages:
    A[i] = stname
    # A[i] = stname[-6:]
    print A[i]
    i=i+1

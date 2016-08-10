import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html 

class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()
    
url = 'http://www.kofiabond.or.kr/websquare/websquare.html?w2xPath=/xml/bondint/lastrop/BISLastAskPrcDay.xml&amp;divisionId=MBIS01010010000000&amp;divisionNm=%25EC%259D%25BC%25EC%259E%2590%25EB%25B3%2584&amp;tabIdx=1&amp;w2xHome=/xml/&amp;w2xDocumentRoot='  
#This does the magic.Loads everything
r = Render(url)  
#result is a QString.
result = r.frame.toHtml()

#QString should be converted to string before processed by lxml
formatted_result = str(result.toAscii())

#Next build lxml tree from formatted_result
tree = html.fromstring(formatted_result)

#Now using correct Xpath we are fetching URL of archives
archive_links = tree.xpath('//table/tbody/tr/td/nobr/text()')
print archive_links
#print formatted_result

"""
네이버 증권 사이트에서 오른쪽 마우스 클릭 후 inspect (검사) 클릭 이후, 오른쪽 위 마우스 버튼 클릭 후 원하는 사이트 상 정보에 마우스를 위치한 후 클릭 이후 오른쪽
코드에서 오른쪽 마우스 클릭 후 copy -> copy selector 클릭 후 복붙
=> #exchangeList > li.on > a.head.usd > div > span.value
""" 
from bs4 import BeautifulSoup
import urllib.request as req
import datetime

url = "https://finance.naver.com/marketindex/"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")
currency = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")

print("Date: " + now + " USD: " + currency.string)


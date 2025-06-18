'''
아래 주석 코드는 Shebang (샤뱅)을 의미 해당 주석이 위치한 파일을 어떠한 인터프리터로 실행할지 결정
'''
#!/usr/bin/env python
import sys
import urllib.request as req
import urllib.parse as parse

if (len(sys.argv) <= 1): # 외부에서 파이썬으로 넘어오는 파라미터의 개수가 1개뿐이라면
    print("region number paramater must require")
    sys.exit()

regionNumber = sys.argv[1] # 외부에서 파이썬으로 넘어오는 파라미터 (regionNumber: 지역번호)

api_addr = "https://www.weather.go.kr/w/weather/forecast/mid-term.do"
values = {
    'stnId1' : regionNumber
}
params = parse.urlencode(values) # String 타입을 Binary 타입으로 인코딩
url = api_addr + "?" + params # ?는 url에서 쿼리스트링을 의미
print("url =", url)

data = req.urlopen(url).read()
text = data.decode("utf-8") # Binary 타입을 String 타입으로 인코딩
print(text)
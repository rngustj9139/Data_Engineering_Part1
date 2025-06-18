"""
하기 코드는 VS Code에서는 글자가 깨지고 파워쉘에서는 정상 작동
"""
#!/usr/bin/env python

import requests 
from bs4 import BeautifulSoup

def main():
    url = "https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId1=109"
    res = requests.get(url)

    soup = BeautifulSoup(res.text)
    table = soup.find("table", class_="table-col cmp-sticky-type1") # table 태그이며, table-col cmp-sticky-type1이라는 Class 명을 갖는 태그를 가져옮 (테이블 형식)
    tbody = table.find("tbody")
    trs = tbody.find_all("tr") # find_all은 리스트를 반환 (iteration 가능)

    for index_tr, tr in enumerate(trs): # tbody는 리스트가 아닌 태그 객체이며 iteration 불가
        tds = tr.find_all("td")
        for index_td, td in enumerate(tds):
            if (index_td == 1):
                td = tr.find("td", class_="midterm-city")
                city = td.find("span", class_="sticky").text.strip() # strip()을 통해 양쪽 공백 제거
            elif (index_td >= 2): 
                min_temperature = td.find("span", class_="tmn").text.strip() # strip()을 통해 양쪽 공백 제거
                max_temperature = td.find("span", class_="tmx").text.strip() # strip()을 통해 양쪽 공백 제거
            if (index_td != 0 and index_td != 1):
                print(f"[{city}] → min_temp: {min_temperature} max_temp: {max_temperature}")

if __name__ == "__main__":
    main()
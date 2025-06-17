import urllib.request

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url) # 응답값을 res (response) 변수에 저장
data = res.read()

text = data.decode("utf-8") # Binary 값이 디코딩을 통해 String 값으로 변환됨
print(text)
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\\2023_BIGDATA\\chromedriver-win64\\chromedriver.exe" # 백슬래시 (\)를 두번 붙이거나 문자열 앞에 r을 붙이기 (r"D:\2023_BIGDATA\chromedriver-win64\chromedriver.exe")

# 옵션 설정 (필요시)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # 예시: 창 최대화

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.google.com/") # Chrome 브라우저 로딩
time.sleep(10) # 10초 동안 브라우저 유지

driver.quit() # 브라우저 종료


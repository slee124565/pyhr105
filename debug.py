from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


if __name__ == '__main__':
    url = 'https://bsignin.104.com.tw/login'
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # 開啟目標網站
    driver.get(url)

    pass


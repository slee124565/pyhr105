import os
import time
import dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

dotenv.load_dotenv()

if __name__ == '__main__':
    url = 'https://bsignin.104.com.tw/login'
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    username = os.getenv('USERNAME', '')
    password = os.getenv('PASSWORD', '')

    # 開啟目標網站
    driver.get(url)

    # 等待頁面加載
    time.sleep(1.5)

    # 定位電子信箱（用戶名）輸入框
    username_input = driver.find_element(By.CSS_SELECTOR, 'input[data-qa-id="loginUserName"]')
    username_input.send_keys(username)  # 輸入用戶名

    # 定位密碼輸入框
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-qa-id="loginPassword"]')
    password_input.send_keys(password)  # 輸入密碼

    # 定位並點擊 "立即登入" 按鈕
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[data-qa-id="loginButton"]')

    # 模擬用戶滑鼠操作
    actions = ActionChains(driver)
    actions.move_to_element(login_button).click().perform()

    # 顯示訊息並等待用戶按下 Enter
    input("Check browser UI and press <Enter> to continue...")

    pass

    # 下載履歷
    # 'https://vip.104.com.tw/search/SearchResumeMaster?idno=30000002614244&ec=12&c=130000000049773'

    # 執行登出
    # 'https://vip.104.com.tw/oidc/logout'

    driver.quit()

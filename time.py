from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:8080/ruiqinbus//page/index.html")

login_ele = (By.CLASS_NAME,"login-submit")

try:
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located(login_ele))
    print("资源加载成功")
except:
    print("资源加载失败")

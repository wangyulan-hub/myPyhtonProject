from selenium import webdriver


#获取driver
driver = webdriver.Chrome()
#打开网页
driver.get("https://www.baidu.com/")
print(driver.title)

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


#获取driver
driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐性等待，最长等待10秒
#打开网址
driver.get("http://localhost:8080/ruiqinbus/login.jsp")
#最大化浏览器
driver.maximize_window()
print(driver.title)

#获取用户名输入框
username_ele = driver.find_element_by_id("j_username").send_keys("zhuzhichao")
#获取密码输入框
password_ele = driver.find_element_by_id("j_password").send_keys("123456")
#获取验证码输入框
auth_code_ele = driver.find_element_by_id("jym_val").send_keys("aaaa")
#获取登录按钮
login_ele = driver.find_element_by_css_selector("#loginForm > input.login-submit")

#触发点击事件
ActionChains(driver).click(login_ele).perform()

#验证登录成功
#获取鼠标上移的元素
user_name_ele = driver.find_element_by_class_name("zui-btn.head-bar-user")
print(user_name_ele.text)

name = user_name_ele.text

if name == u"您好！ 朱智超":
    print("login ok")
else:
    print("账号或密码错误")


print("========over======")
driver.close()

# sleep(1)
#
# #hover触发
# ActionChains(driver).move_to_element(user_name_ele).perform()
#
# sleep(1)
#
# #获取鼠标上移的元素
# myData_ele = driver.find_element_by_id("updateMyData")
# sleep(1)
# #hover触发
# ActionChains(driver).click(myData_ele).perform()
# sleep(1)
#
# #获取用户名称元素
# real_name_ele = driver.find_element_by_id("real_Name")
# print("--------------------")
# print(real_name_ele.text)






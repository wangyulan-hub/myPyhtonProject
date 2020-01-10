from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


#获取driver
driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐性等待，最长等待10秒
#打开网址
driver.get("http://localhost:8080/ruiqinbus/login.jsp")
#最大化浏览器
driver.maximize_window()
print(driver.title)

#获取用户名输入框
username_ele = driver.find_element_by_id("j_username").send_keys("superadmin")
#获取密码输入框
password_ele = driver.find_element_by_id("j_password").send_keys("123456")
#获取验证码输入框
auth_code_ele = driver.find_element_by_id("jym_val").send_keys("aaaa")
#获取登录按钮
login_ele = driver.find_element_by_css_selector("#loginForm > input.login-submit")

#触发点击事件
ActionChains(driver).click(login_ele).perform()

#点击锁定导航栏
navLock = driver.find_element_by_class_name("zui-icon-you.z-nav-arrow")
navLock_ele = driver.find_element_by_class_name("z-nav-switch")
ActionChains(driver).move_to_element(navLock).perform()
navLock_ele.click()

#点击用户管理
dictInfoList = driver.find_element_by_xpath('//*[@id="leftNav"]/div[2]/a[5]')
ActionChains(driver).move_to_element(dictInfoList).perform()
userList = driver.find_element_by_xpath('//*[@id="leftNav"]/ul/li[5]/a[7]')
userList.click()

#选中重置密码
resetPass = driver.find_element_by_class_name("zui-btn.resetPass")
resetPass.click()
alert_ele = driver.switch_to.alert
alert_ele.dismiss()
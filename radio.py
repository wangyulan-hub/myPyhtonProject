from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

#获取driver
driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐性等待，最长等待10秒
#打开网址
driver.get("http://localhost:8080/ruiqinbus/login.jsp")
#最大化浏览器
driver.maximize_window()
print(driver.title)

#获取用户名输入框
username_ele = driver.find_element_by_id("j_username").send_keys("daipuhui")
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
ActionChains(driver).move_to_element(navLock).click(navLock_ele).perform()

#点击贷前管理-进件管理
loanBefore = driver.find_element_by_xpath("//*[@id='leftNav']/div[2]/a[2]")
busCaseManageList = driver.find_element_by_xpath('//*[@id="leftNav"]/ul/li[2]/a[1]')
ActionChains(driver).move_to_element(loanBefore).move_to_element(busCaseManageList).click().perform()

# main_wrap_ele = driver.find_element_by_class_name("z-main-wrap")
# ActionChains(driver).move_to_element(main_wrap_ele).perform()

#获取新增按钮
# busBinterviewAdd_ele = driver.find_element_by_class_name('zui-btn')
# ActionChains(driver).click(busBinterviewAdd_ele).perform()

customerInfoEdit_ele = driver.find_element_by_xpath('//*[@id="mycontent"]/tr[6]/td[14]/button[2]')
customerInfoEdit_ele.click()
print(1)

#获取当前窗口的handle name
current_window = driver.current_window_handle
#返回当前会话中所有窗口的句柄
all_windows = driver.window_handles
print("all_windows:",all_windows)
#通过遍历判断要切换的窗口
for window in all_windows:
    print("window:",window)
    if window != current_window:
        #将定位焦点切换到指定的窗口，包含所有可切换焦点的选项
        driver.switch_to.window(window)
#获取当前窗口的handle name
# current_window = driver.current_window_handle

sex_ele = driver.find_element_by_xpath('//*[@id="busBondsmanEditorContent"]/div[2]/div[10]/div[2]/div[6]/div/div/label[2]/i')
ActionChains(driver).move_to_element(sex_ele).click().perform()

submit_ele = driver.find_element_by_id("saveOrupdate")
submit_ele.click()

popover_okay_ele = driver.find_element_by_class_name("zui-btn.zui-popover-okay")
popover_okay_ele.click()

#定位到下拉框
bUS_RCR_BOR_ISMARRY = driver.find_element_by_id("bUS_RCR_BOR_ISMARRY")
ActionChains(driver).move_to_element(bUS_RCR_BOR_ISMARRY).click().perform()
#通过xpth定位到第3个标签
# MS_YH = driver.find_element_by_xpath('//*[@id="busBondsmanEditorContent"]/div[2]/div[10]/div[2]/div[8]/div/div/div/dl/dd[3]')
# MS_YH.click()

select = driver.find_element_by_class_name("zui-option-list")
#找到所有的option
all_options = select.find_elements_by_tag_name("dd")
print(len(all_options))
#遍历所有的选项
for option in all_options:
    print("选项:",option.text)
    # option.click()









# driver.quit()
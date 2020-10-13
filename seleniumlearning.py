from selenium import webdriver
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)
# WebPath = "https://www.google.com"
# WebPath = "https://www.baidu.com/"
WebPath = "https://www.agoda.com/zh-tw/"
browser.get(WebPath)

# 透過Element方式抓取元素
# by id
# browser.find_element_by_id('s-top-left').click() # 百度

# by name
# browser.find_element_by_name('wd').send_keys("hello world") # 百度

# 輸入框並填入Hello world, 並用\n的方式仿造Enter
# browser.find_element_by_name('q').send_keys('hello world\n') # Google
# time.sleep(2) # 暫停2秒
# browser.quit() # 關閉瀏覽器

# by link text and partial link text
# browser.find_element_by_link_text('Gmail').click()
# time.sleep(2)
# browser.back() # 返回上一頁
# browser.find_element_by_partial_link_text('mail').click()
# time.sleep(2)
# browser.quit()

# by Tag # 百度
# elements = browser.find_elements_by_tag_name('a')

# for ele in elements:
#     # print(ele.text)

#     if ele.text == '新闻':
#         ele.click()
#         time.sleep(5)
#         pass
#     pass

# browser.quit()

# by xpath # Agoda
browser.maximize_window() # 螢幕最大化
time.sleep(2)
browser.find_element_by_xpath("//div[@id='SearchBoxContainer']/div[2]/button/div/div/span").click()

# by css
# time.sleep(2)
# browser.find_element_by_css_selector('.gkBteU').click()

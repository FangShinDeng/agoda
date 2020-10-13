from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)
WebPath = "https://baidu.com"
browser.get(WebPath)

# Maximize the browser # 視窗最大化
browser.maximize_window()

# Get Title # 索取標題
browser_title = browser.title
print(browser_title)

# Get CurrentURL # 索取目前連結
CurrentURL = browser.current_url
print(CurrentURL)

# Open another URL
browser.get("https://www.google.com")

# Broswer back # 回上一頁
time.sleep(2)
browser.back()

# Broswer Forward # 下一頁
time.sleep(2)
browser.forward()

# Get Page Source # 索取當前頁面原始碼
Page_source = browser.page_source
print(Page_source)

# Broswer Refresh 重新整理
browser.refresh()

# Close or quit browser, Close關閉單一頁面, quit關閉整個瀏覽器
browser.close() 
# browser.quit()

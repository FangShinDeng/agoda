from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)
WebPath = "https://www.agoda.com/zh-tw/search?city=4951&checkIn=2020-11-01&los=1&rooms=1&adults=2&children=0&gclid=Cj0KCQjw2or8BRCNARIsAC_ppybm78O0Bj2B8BxqCWh89WSVBbKQ92tHwkfRmItkOZ2tG8XXENUtkqgaAiWHEALw_wcB&languageId=20&userId=5a482a2d-74d5-4cff-be26-d3dfd132e91d&sessionId=4zuobjjdcii30pjringprbrg&pageTypeId=1&origin=TW&locale=zh-TW&cid=-1&aid=130243&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=5a482a2d-74d5-4cff-be26-d3dfd132e91d&prid=0&checkOut=2020-11-02&priceCur=TWD&textToSearch=%E5%8F%B0%E5%8C%97%E5%B8%82&travellerType=1&familyMode=off&productType=-1"
browser.get(WebPath)
browser.maximize_window()
time.sleep(2)   

# 一開始移動視窗
browser.execute_script('window.scrollTo(0,224)')
browser.execute_script('window.scrollTo(0,1828)')
browser.execute_script('window.scrollTo(0,3182)')
browser.execute_script('window.scrollTo(0,4606)')
browser.execute_script('window.scrollTo(0,6099)')
time.sleep(2)
browser.execute_script('window.scrollTo(0,7249)')
browser.execute_script('window.scrollTo(0,8967)')
browser.execute_script('window.scrollTo(0,10645)')
browser.execute_script('window.scrollTo(0,12208)')
browser.execute_script('window.scrollTo(0,13985)')
browser.execute_script('window.scrollTo(0,16714)')
time.sleep(2)
browser.execute_script('window.scrollTo(0,17963)')
browser.execute_script('window.scrollTo(0,20214)')
browser.execute_script('window.scrollTo(0,22014)')
browser.execute_script('window.scrollTo(0,23851)')
browser.execute_script('window.scrollTo(0,25714)')
browser.execute_script('window.scrollTo(0,28194)')
time.sleep(2)

# 抓取第一頁的頁數資料，並將目前頁面跟最後一頁的數字給抓出來
PagesNumber = format(browser.find_element_by_id('paginationPageCount').text)
PagesNumberlist = PagesNumber.split('/ ')
CurrentPage = int(PagesNumberlist[0].strip('第').strip('頁'))
LastPage = int(PagesNumberlist[1].strip('共').strip('頁'))

# 第一次不重新滾動的設定值
firsttime = 1

while LastPage > CurrentPage:
    # 第一次已經移動過視窗，直接執行下方代碼，並將firsttime改為0
    if firsttime == 1:
        firsttime = 0
    # 非第一次的都重新滾動
    else: 
        browser.execute_script('window.scrollTo(0,224)')
        browser.execute_script('window.scrollTo(0,1828)')
        browser.execute_script('window.scrollTo(0,3182)')
        browser.execute_script('window.scrollTo(0,4606)')
        browser.execute_script('window.scrollTo(0,6099)')
        time.sleep(2)
        browser.execute_script('window.scrollTo(0,7249)')
        browser.execute_script('window.scrollTo(0,8967)')
        browser.execute_script('window.scrollTo(0,10645)')
        browser.execute_script('window.scrollTo(0,12208)')
        browser.execute_script('window.scrollTo(0,13985)')
        browser.execute_script('window.scrollTo(0,16714)')
        time.sleep(2)
        browser.execute_script('window.scrollTo(0,17963)')
        browser.execute_script('window.scrollTo(0,20214)')
        browser.execute_script('window.scrollTo(0,22014)')
        browser.execute_script('window.scrollTo(0,23851)')
        browser.execute_script('window.scrollTo(0,25714)')
        browser.execute_script('window.scrollTo(0,30000)')
        time.sleep(2)

    # 打印整個頁面的所有旅館名稱
    hotelnames = browser.find_elements_by_class_name('PropertyCard__HotelName')
    for name in hotelnames: 
        print(name.text)
        pass

    # 抓取每頁的頁數，並將目前頁面跟最後一頁的數字給抓出來
    PagesNumber = format(browser.find_element_by_id('paginationPageCount').text)
    PagesNumberlist = PagesNumber.split('/ ')
    CurrentPage = int(PagesNumberlist[0].strip('第').strip('頁'))
    LastPage = int(PagesNumberlist[1].strip('共').strip('頁'))

    # 當如果頁數已為最後一頁時，直接跳出
    # 避免NextButton找不到報錯
    if CurrentPage == LastPage:
        time.sleep(3)
        browser.quit()
    else:
        NextButton = browser.find_element_by_id('paginationNext')
        NextButton.click()
        pass
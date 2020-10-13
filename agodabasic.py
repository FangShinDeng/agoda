from selenium import webdriver
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)
WebPath = "https://www.agoda.com/zh-tw/search?city=4951&checkIn=2020-11-01&los=1&rooms=1&adults=2&children=0&gclid=Cj0KCQjw2or8BRCNARIsAC_ppybm78O0Bj2B8BxqCWh89WSVBbKQ92tHwkfRmItkOZ2tG8XXENUtkqgaAiWHEALw_wcB&languageId=20&userId=5a482a2d-74d5-4cff-be26-d3dfd132e91d&sessionId=4zuobjjdcii30pjringprbrg&pageTypeId=1&origin=TW&locale=zh-TW&cid=-1&aid=130243&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=5a482a2d-74d5-4cff-be26-d3dfd132e91d&prid=0&checkOut=2020-11-02&priceCur=TWD&textToSearch=%E5%8F%B0%E5%8C%97%E5%B8%82&travellerType=1&familyMode=off&productType=-1"
browser.get(WebPath)
browser.maximize_window()

# click button
time.sleep(2)   
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

hotelnames = browser.find_elements_by_class_name('PropertyCard__HotelName')

print(hotelnames[0].text)
time.sleep(0.5)

browser.find_element_by_id('paginationNext').click()
# browser.quit()  
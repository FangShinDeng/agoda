# 來爬蟲超大旅行網站 agoda 的資料吧！
    教學影片: https://www.youtube.com/watch?v=MQH4Rau_F_A&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF&index=10
    影片中的教學透過NextButton來直接印出所有Title名稱，但最後會報錯誤，因為最後一頁找不到NextButton了
    在本篇練習中，我們將抓取頁數總和及當前頁數來作為判斷式！並在最後已頁數作為最後判斷，避免報錯哦！

    尚未摸過Selenium套件的初學者，建議先看下面的Selenium最基本使用及影片學習來源，並將IDE的使用方法給搞懂後實作一次
    實作完畢後，再來從0挑戰Agoda的爬蟲專案哦！

## 使用 Selenium 套件！最基本使用!!!
    基本使用教學影片:https://www.youtube.com/watch?v=Xjv1sY630Uc

## Selenium 學習影片來源
    參考學習影片: https://www.youtube.com/watch?v=o6yzNaRAzW8&list=PLRxMjOjh7Y5fi4ID2YCkcA2vLlD-JNC9i
    seleniumlearning.py 練習基本的selenium操作
    seleniumextra.py 練習與瀏覽器互動的一些操作
## Selenium IDE Chrome 插件
    下載連結: https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd

## Selenium筆記
    透過以下方式抓取Element
    by id
    by name
    by class name
    by link text and partial link text
    by tag
    by xpath
    by css

    其中xpath的原理請參考w3c上的內容: https://www.w3schools.com/xml/xpath_intro.asp
## 開始來寫基本的Agoda爬蟲吧！
    因為Agoda的網頁目前在一開始沒顯出現下一頁的按鈕，因此我們先用IDE進行Window.scroll，然後改成execute script的方式來執行，執行完畢後，打印第一頁的所有飯店名稱，具體請參考agodabasic.py
    
## 學會一頁!接著來打印全部頁數吧
    再來我們將用while迴圈來打印全部頁數! 在使用while迴圈時，我們需要先抓出當前頁數/總頁數的資料，我們用by id即可處理
    抓取總頁數資料後，我們要將這個字串切分開來，並將當前頁數及總頁數分別存到兩個變數裡面，若不熟悉變數操作的，請參考demo.py
    
    再來我們用 while 當總頁數>當前頁數時，就重複執行打印，讀取當前頁數及按下一頁的動作，即可完成90%，但最後你會發現印完了會報錯，那是因為最後一頁找不到下一頁的按鈕，為了避免這個錯誤，我們在讀取新頁面時，執行一次當前頁面是否等於最後一頁的判斷，如果是的話，就直接關閉瀏覽器！具體請參考agoda.py
    
    這樣就大功告成拉！
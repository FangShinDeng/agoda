# 測試如何分割及擷取字串中的數字
x = "第3頁/ 共14頁"
y = x.split('/ ')
print(y)
FrontNumber = y[0].strip('第').strip('頁')
print(FrontNumber)
print(type(FrontNumber))

z = int(FrontNumber)
print(z)
print(type(z))
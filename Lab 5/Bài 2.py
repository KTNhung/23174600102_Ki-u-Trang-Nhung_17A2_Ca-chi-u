str1 = input("Nhập chuỗi kí tự 1: ")
str2 = input("Nhập chuỗi kí tự 2: ")

c=''
for i in str1:
    for j in str2:
        if i==j and c.count(i)==0:
            c+=i
print('chuỗi con chung của 2 chuỗi là:', c)
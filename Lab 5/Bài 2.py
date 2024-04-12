str1 = input("Nhập chuỗi kí tự 1: ")
str2 = input("Nhập chuỗi kí tự 2: ")

str = ""
for i in range(len(str1 + 1)):
    for j in range(len(str2 + 1)):
        if str1[i] == str2[j]:
            str += str + 1
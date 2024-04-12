str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
str = ""
if (str1.isdigit() and str2.isdigit()) or (str1.isalpha() and str2.isalpha()):
    for i in str1:
        for j in str2:
            if i == j:
                str += i 
    print("2 chuỗi có thể biến đổi cho nhau.")
else:
    print("2 chuỗi không thể biến đổi cho nhau.")
n = input("Nhập chuỗi ký tự: ")
str = ""
for i in n:
    if i.isdigit():
        str += i


if int(str) < 0:
    print(str, "khong phải số nguyên tố.")
elif int(str) == 2:
    print(str, "là số nguyên tố.")
else:
    flag = 0 
    for j in range(2, int(str)):
        if int(str) % j == 0:
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        print(str, "là số nguyên tố.")
    else:
        print(str, "không phải số nguyên tố.")
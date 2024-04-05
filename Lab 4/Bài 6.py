#Viết chương trình nhập một số từ bàn phím và in ra màn hình bằng chữ tiếng anh
m = int(input("Nhập vào 1 số: "))
n = 0
doc = ""
while m != 0:
    n = m % 10
    m = m //10
    if n == 1:
        doc = " one" + doc 
    elif n == 2:
        doc = " two" + doc 
    elif n == 3:
        doc = " three" + doc 
    elif n == 4: 
        doc = " four" + doc 
    elif n == 5:
        doc = " five" + doc 
    elif n == 6:
        doc = " six" + doc 
    elif n == 7:
        doc = " seven" + doc 
    elif n == 8:
        doc = " eight" + doc  
    elif n == 9:
        doc = " nine" + doc 

print(doc)


        
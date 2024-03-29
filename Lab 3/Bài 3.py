#a. In ra các số nguyên tố từ 100 - 1000
flag = 1
print("Các số nguyên tố từ 100 -1000 là: ", end = " ")
for i in range(100, 1000):
    for j in range(2, i):
        if i % j == 0:
            flag = 0 
            break
        else:
            flag = 1
    if flag == 1:
        print( i, end = " ")
print()
#b. In ra các số  chính phương từ 1 - 1000
print("Các số chính phương từ 1 - 1000 là: ", end = "")
flag = 0
for i in range(1, 1000):
    for j  in range(1, i):
        if j**2 == i:
            flag = 1
            break
        else:
            flag = 0
    if flag == 1:
        print(i, end = " ")
print()
#c. In ra chuỗi Fibonacci sao cho số cuối cùng trong chuỗi nhỏ hơn 100
a = 0 
b = 0
c = 1 
print("Chuỗi Fibonacci mà số cuối trong chuỗi nhỏ hơn 100 là: ", end = " ")
for i in range(0, 100):
    b = a + b
    a = c 
    c = b 
    if c < 100: 
        print(c, end = " ")
print()


#d. In ra các số hoàn hảo bé hơn 500
print("Các số hoàn hảo bé hơn 500 là: ")
for i in range(1, 500):
    S = 0 
    for j in range(1, i):
        if i % j == 0:
            S += j
    if S == i:
        print(i, end = " ")
print()

#e. In ra tổng của các số ngũ giác trong đoạn từ 1 - 200 ( kể cả 200)
print("Các số ngũ giác trong đoạn từ 1 - 200 là: ")
S = 0 
for i in range(1, 200):
    for n in range(0, i + 1):
        if i == (n*(3*n - 1))/2:
            print(i, end = " ")
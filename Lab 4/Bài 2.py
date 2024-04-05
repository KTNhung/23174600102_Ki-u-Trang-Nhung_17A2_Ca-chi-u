print("Các số nguyên tố nhỏ hơn 100 là:", end = " ")
i = 1
while i < 100:
    if i < 2:
        pass
        i += 1
    else: 
        j = 2
        flag = 1 
        while j < i:
            if i % j == 0:
                flag = 0 
                break
            j += 1
        if flag == 1:
            print(i, end = " ")
        i += 1

print()
#In ra các số chính phương nhỏ hơn 100
print("Các số chính phương nhỏ hơn 100 là:", end = " ")
i = 1
while i < 100:
    j = 1
    flag = 1 
    while j < i: 
        if j ** 2 == i:
            flag = 0
            break
        j += 1 
    if flag == 0:
        print(i, end = " ")
    i += 1 

print()

#In ra tất cả số Fiboncci nhỏ hơn 1000
print("Dãy Fibonacci nhỏ hơn 100 là:", end = " ")
a = 0
b = 0
c = 1
while c < 100:
    b = a + b 
    a = c
    c = b 
    print(b, end = " ")

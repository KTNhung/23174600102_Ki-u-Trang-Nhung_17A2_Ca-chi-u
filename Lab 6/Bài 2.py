a = []
while True:
    n = int(input("Nhập số: "))
    if n <= 0:
        break
    else:
        a.append(n)

b = []
flag = 1 
for j in a:
    if j <= 1:
        flag = 0
    
    elif j == 2:
            b.append(j)
    else: 
        for i in range(2, j):
            if j % i == 0:
                flag = 0 
                break
            else:
                flag = 1
    if flag == 1:
        b.append(j)
print("Các số nguyên tố có trong mảng là:", b )

c = []
for j in a:
    S = 0 
    for i in range(1, j):
        if j % i == 0:
            S += i 
    if S == j:
        c.append(j)

print("Các số hoàn hảo có trong mảng là:", c) 


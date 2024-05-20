def kiem_tra_snt(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

b = []
for i in range(1000):
    if i % 2 != 0:
        if kiem_tra_snt(i) and kiem_tra_snt(i+2):
            b.append([i,i+2])
print(b)
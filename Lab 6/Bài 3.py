a = []
while True:
    n = float(input("Nhập số: "))
    if n < 0:
        break
    else:
        a.append(n)


print("Số lớn nhất có trong dãy là:",max(a))
print("Số nhỏ nhất có trong dãy là:", min(a))

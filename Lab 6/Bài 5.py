a = []
b = int(input("Nhập số lượng số muốn nhập: "))
i = 0 
while i < b:
    n = float(input("Nhập số: "))
    a.append(n)
    i += 1 
c = a[1] - a[0]
for j in range(1, len(a)):
    flag = 1 
    d = a[j] - a[j-1] 
    if d != c: 
        flag = 0
        break
    else:
        flag = 1

if flag == 1:
    print("Đây là dãy cấp số cộng.", a)
else:
    print("Đây không phải dãy cấp số cộng. ")



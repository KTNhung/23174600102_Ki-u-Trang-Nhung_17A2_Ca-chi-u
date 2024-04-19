a = []
while True:
    n = int(input("Nhập số: "))
    if n <= 0:
        print("Số không hợp lệ.")
        break
    else:
        a.append(n)

S1 = 0
S2 = 0 
for i in a:
    if i % 2 == 0:
        S1 += i
    else:
        S2 += i
print("Tổng của tât cả các số chẵn trong mảng:", S1)
print("Tổng của tất cả các số lẻ trong mảng:", S2)

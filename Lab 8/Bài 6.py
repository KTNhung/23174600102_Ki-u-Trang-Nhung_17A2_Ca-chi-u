a = []
while True:
    n = int(input("Nhập số: "))
    if n < 0:
        break
    else:
        a.append(n)

b = list(filter(lambda i: i%2 != 0, a))
print("Các số lẻ trong danh sách:", b)

c = list(filter(lambda i: i % 2 == 0, a))
print("Các số chẵn có trong danh sách:", c)

d =list(map(lambda i: i**3, a))
print("Các số sau khi lập phương:", d)

e1 = list(filter(lambda i: i % 2 == 0, a))
e2 = list(map(lambda i: i**3, e1))
print("Các số chẵn sau khi lập phương:", e2)

g1 = list(filter(lambda i: i%2 != 0, a))
g2 = list(map(lambda i: i**2, g1))
print("Các số lẻ sau khi bình phương:", g2)

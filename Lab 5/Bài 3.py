n = input("Nhập chuỗi: ")

m = input("Nhập từ cần tìm kiếm: ")

print("Vị trí của từ cần tìm trong chuỗi là:", n.find(m))
s = 0
x = 0 
j = 0
for i in n:
    s = n.count(i)
    if s > x:
        x = s
        j = i

print("Từ xuất hiện nhiều nhất trong chuỗi là:", j)
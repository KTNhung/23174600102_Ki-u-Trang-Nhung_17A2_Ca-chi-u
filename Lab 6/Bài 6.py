m = int(input("Nhập chiều cao ma trận a: "))
n = int(input("Nhập chiều dài ma trận a: "))
a = []
for i in range(m):
    a.append([])
    for j in range(n):
        print("Nhập phần tử a[",i,"] [",j,"]: ",end="")
        x = int(input())
        a[i].append(x)
    print()
print("Ma trận a: ")
for i in range(m):
    for j in range(n):
        print(a[i][j]," ",end="")
    print()

SUM = 0
for i in range(m):
    for j in range(n):
        SUM = SUM + a[i][j]
print("Tổng là:",SUM)
c = int(input("Nhập chiều cao ma trận b: "))
d = int(input("Nhập độ dài ma trận b: "))
b = []
for i in range(c):
    b.append([])
    for j in range(d):
        print("Nhập phần tử b[",i,"] [",j,"]: ",end="")
        x = int(input())
        b[i].append(x)
    print()
print("Ma trận b: ")
for i in range(c):
    for j in range(d):
        print(b[i][j]," ",end="")
    print()

if m != d or n != c:
    print("Không thể tính tích.")
else:
    mul = []
    for i in range(m):
        mul.append([])
        for j in range(d):
            mul[i].append(0)
            for x in range(n):
                mul[i][j]= mul[i][j] + a[i][x]*b[x][j]
    print("Tích 2 ma trận là")
    for i in range(m):
        for j in range(d):
            print(mul[i][j]," ",end="")
        print()

        
Chuyen_vi = []
for i in range(n):
    Chuyen_vi.append([])
    for j in range(m):
        Chuyen_vi[i].append(a[j][i])
print("Ma trận chuyển vị là: ")
for i in range(n):
    for j in range(m):
        print(Chuyen_vi[i][j]," ",end="")
    print()
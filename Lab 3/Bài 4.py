#hình 1
for i in range(1, 6):
    for j in range(6 - i + 1):
         print(" ", end = "")
    for j in range(i):
        print(" *", end = "")
    print()
for i in range(5 , -1, -1):
    for j in range( 6 - i + 1):
         print(" ", end = "")
    for j in range(i):
        print(" *", end = "")
    print()


#hình 2
n = 7
m = 3
d = 0
for i in range(0,n*2,2):
    for j in range(0,n-i-1+d):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
    d = d + 1
for i in range(0,3*3,3):
    for j in range(0,n-m+1):
        print(" ",end="")
    for j in range(m):
        print("*",end="")
    print()
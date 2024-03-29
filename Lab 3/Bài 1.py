n = int(input("Nhập số nguyên dương: "))
if n <= 0:
    print("Yêu cầu nhập lại.")
else:
    #a
    S1 = 0
    for i in range(n+1):
        S1 += i
    print("S1 =", S1)

    #b.
    S2 = 1
    for i in range(1, n+1):
        S2 += 1/i
    print("S2 =", S2)

    #c. 
    S3 = 1
    for i in range(1, n+1):
        S3 += 1/((i)**1/2)
    print("S3 =", S3)

    #d.
    S4 = 1
    for i in range(1, n+1):
        S4 += ((-1)**n+1)/n
    print("S4 =", S4)


a, b, c = map(int, input("Nhập 3 số nguyên: ").split())
if a > 0 and b > 0 and c > 0: 
    if a > b and a > c:
        if b > c:
            print(b)
        else: 
            print(c)
    elif b > a and b > c:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        if a > b:
            print(a)
        else:
            print(b)
else:
    print("Số không hợp lệ.")
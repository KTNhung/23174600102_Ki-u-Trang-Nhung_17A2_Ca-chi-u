a = int(input("Nhập vào 1 số nguyên: "))
b = a // 1000
if b == 0:
    print("0")
elif b > 0 and b <= 9:
    print("Chữ số hàng nghìn của số này là:", b)
else:
    c = b % 10
    if c == 0:
        print("Chữ số hàng nghìn của số này là 0.")
    else:
        print("Chữ số hàng nghìn của số này:", c)
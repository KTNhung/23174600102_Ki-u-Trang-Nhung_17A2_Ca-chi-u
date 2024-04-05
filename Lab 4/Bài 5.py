while True:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print(f"Tổng {a} + {b} = {a+b}")
    print(f"Hiệu {a} + {b} = {a-b}")
    print(f"Tích {a} + {b} = {a*b}")
    print(f"Thương {a} + {b} = {a/b}")
    print(f"Căn bậc 2 của {a} và {b} là {a**1/2} và {b**1/2}")
    n = input("Bạn muốn tiếp tục nhập không ? (Y/N) ")
    if n == "N" or n == "n":
        break
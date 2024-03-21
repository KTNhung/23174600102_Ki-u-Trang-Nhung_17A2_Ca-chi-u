a = int(input("Nhập vào một số nguyên có ba chữ số: "))
if 100 <= a <= 999:
    tram = a // 100
    chuc = (a % 100) // 10
    don_vi = a % 10
    b = ""
    c = ''
    d = ''

    if tram > 0:
        if tram == 1:
            b = "One hundred"
        elif tram == 2:
            b = "Two hundred"
        elif tram == 3:
            b = "Three hundred"
        elif tram == 4:
            b = "Four hundred"
        elif tram == 5:
            b = "Five hundred"
        elif tram == 6:
            b = "Six hundred"
        elif tram == 7:
            b = "Seven hundred"
        elif tram == 8:
            b = "Eight hundred"
        elif tram == 9:
            b = "Nine hundred"
    if chuc == 1:
        if don_vi == 0:
            c = "ten"
        elif don_vi == 1:
            c = "eleven"
        elif don_vi == 2:
            c = "twelve"
        elif don_vi == 3:
            c = "thirteen"
        elif don_vi == 4:
            c = "fourteen"
        elif don_vi == 5:
            c = "fifteen"
        elif don_vi == 6:
            c = "sixteen"
        elif don_vi == 7:
            c = "seventeen"
        elif don_vi == 8:
            c = "eighteen"
        elif don_vi == 9:
            c = "nineteen"
    elif chuc == 2:
        c = "twenty"
    elif chuc == 3:
        c = "thirty"
    elif chuc == 4:
        c = "fourty"
    elif chuc == 5:
        c = "fifty"
    elif chuc == 6:
        c = "sixty"
    elif chuc == 7:
        c = "seventy"
    elif chuc == 8:
        c = "eighty"
    elif chuc == 9:
        c = "ninety"

    if don_vi != 0 and chuc != 1:
        if don_vi == 1:
            d = "one"
        elif don_vi == 2:
            d = 'two'
        elif don_vi == 3:
            d = 'three'
        elif don_vi == 4:
            d = 'four'
        elif don_vi == 5:
            d = 'five'
        elif don_vi == 6:
            d = 'six'
        elif don_vi == 7:
            d = 'seven'
        elif don_vi == 8:
            d = 'eight'
        elif don_vi == 9:
            d = 'nine'
    print(f"Số {a} đọc là: {b} and {c} {d}.")

else:
    print("Số không hợp lệ.")



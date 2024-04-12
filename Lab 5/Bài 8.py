n = input("Nhập chuỗi ký tự: ")
a = len(n)
if a < 10:
    print("Nhập lại chuỗi dài hơn 10 ký tự.")
else: 
    #a. Từ 2 - 8 
    print("Chuỗi ký tự con từ trị trí thứ 2 - 8:", n[2:9])
    print("Chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5:", n[5:10])
    print("Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", n[-1:-4:-1])
    chu_thuong = n.lower()
    print("Chuyển đổi các ký tự trong chuỗi thành chữ thường:", chu_thuong)
    chu_hoa = n.upper()
    print("Chuyển đổi các ký tự trong chuỗi thành chữ hoa:", chu_hoa)
    c = n[::-1]
    print("Chuỗi ký tự sau khi đảo ngược:", c)
#Nhập vào số nguyên dương ( số thập phân ), chuyển đổi nó sang số nhị phân.
n = int(input("Nhập vào số nguyên: "))
if n < 0:
    print("Số không hợp lệ.")
else:
    chuoi_nhi_phan = ""
    while n > 0:
        phan_du = n % 2 
        chuoi_nhi_phan = str(phan_du) + chuoi_nhi_phan
        n = n//2
    print("Chuỗi chuyển từ hệ thập phân sang hệ nhị phân là:", chuoi_nhi_phan)
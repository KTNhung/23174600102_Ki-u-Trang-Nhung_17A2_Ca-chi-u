S = 0 
da_nhap = " "
le = ""
chan = ""
dem = 0
while S < 1000: 
    n = int(input("Nhập số nguyên dương: "))
    if n <= 0:
        print("Số không hợp lệ.")
    else: 
        S += n 
    da_nhap = da_nhap + " " + str(n)

    #In ra số chẵn
    if n % 2 == 0: 
        chan = chan + " " + str(n)
    else:
        le = le + " " + str(n)
    dem += 1 
print("Các số đã nhập từ bàn phím là:", da_nhap)
print("Các số chẵn đã nhập:", chan)
print("Các số lẻ đã nhập:", le)
print("Số lượng các số nguyên đãư nhập:", dem)
        
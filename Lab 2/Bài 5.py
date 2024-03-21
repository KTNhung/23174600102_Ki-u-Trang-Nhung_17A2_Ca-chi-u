n = int(input("Nhập số người mau vé xem phim: "))
v = 120000
if n == 1:
    print("Giá vé cho 1 người là 120.000 đồng.")
elif 2 <= n <= 4:
    print("Giá vé cho 2 đến 4 người là:", v*n - v*0.05*n)
elif 4 < n <= 10:
    print("Giá vé cho từ 4 đến 10 người là:", v*n - v*n*0.1)
elif n > 10:
    print("Giá vé cho số người từ 10 trở lên là:", v*n - v*n*0.2)
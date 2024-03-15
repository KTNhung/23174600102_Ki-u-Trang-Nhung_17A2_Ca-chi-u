a = int(input("Nhập độ dài cạnh đáy: "))
b = int(input("Nhập chiều cao của hình chóp: "))
c = 1/2*(a**1/2)
Sxq = a*2*c #nửa chu vi nhân trung đoạn ( 1/2 đường chéo đáy )
Stp = Sxq + a**2
Vtg = 1/3*a**2*b   
print("Diện tích xung quanh: {:.2f}".format(Sxq))
print("Diện tích toàn phần: {:.2f}".format(Stp))
print("Thể tích hình chóp tứ giác đều: {:.2f}".format(Vtg))
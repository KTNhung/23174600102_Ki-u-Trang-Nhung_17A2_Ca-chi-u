import math
x = int(input("Nhập vào số thực x: "))
z = int(input("Nhập vào số thực z: "))
f = ((((x**2)*math.sin(z)) + (math.sqrt(abs(x))))/(math.log(z) + math.exp(x - 1))) + math.atan(x*z)
print("Giá trị của biểu thức là: {:.2f}".format(f))
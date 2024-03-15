a1 = int(input("Nhập tọa độ vecto a1: "))
a2 = int(input("Nhập tọa độ vecto a2: "))
b1 = int(input("Nhập tọa độ vecto b1: "))
b2 = int(input("Nhập tọa độ vecto b2: "))
#1. Phép cộng, trừ vecto
x1 = a1 + b1
x2 = a2 + b2
print(f"Phép cộng 2 vecto {a1,a2} và {b1,b2} là {x1,x2}")
y1 = a1 + (-b1)
y2 = a2 + (-b2)
print(f"Phép trừ 2 vecto {a1,a2} và {b1,b2} là {y1,y2}.")

#2. Độ dài của vecto a, vecto b
import math
a = math.sqrt(a1**2 + a2**2)
b = math.sqrt(b1**2 + b2**2)
print(f"Độ dài vecto a là: {a}")
print(f"Độ dài vecto b là: {b}. ")

#3.Cosin góc hợp giữa 2 vecto a và b
cos = ((a1*b1) + (a2*b2))/((math.sqrt(a1**2 + a2**2))*(math.sqrt(b1**2+ b2**2)))
print("Cosin góc giữa 2 vecto a và b là {:.2f}".format(cos))

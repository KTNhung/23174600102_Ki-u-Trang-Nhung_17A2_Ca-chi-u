import math
a, b, c = map(float, input("Nhập hệ số đường thẳng: ").split())
x, y, R = map(float, input("Nhập tọa độ đường tròn (tâm và bán kính R): ").split())
d = abs(a*x + b*y + c )/math.sqrt(a**2 + b**2)
if d > R: 
    print("Đường tròn không cắt đường thẳng.")
elif d == R:
    print("Đường tròn tiếp xúc với đường thẳng tại 1 điểm.")
elif d < R:
    print("Đường tròn và đường thẳng cắt nhau tại 2 điểm.")

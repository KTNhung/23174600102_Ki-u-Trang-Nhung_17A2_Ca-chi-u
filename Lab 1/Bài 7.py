a1, a2, b1, b2, c1, c2 = map(float, input("Nhập các giá trị a1, a2, b1, b2, c1, c2: ").split())
x = (b2 * c1 - c2 * b1) / (a1 * b2 - a2 * b1)
y = (c2 - a2 * x) / b2
print(f"Nghiệm của hệ phương trình là {x,y}")

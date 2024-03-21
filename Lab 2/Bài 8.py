a1, a2, b1, b2 = map(float, input("Nhập hệ số góc của 2 đường thẳng: ").split())
c1, c2 = map(float, input("Nhập hệ số tự do của 2 đường thẳng: ").split())
if a1/a2 == b1/b2 == c1/c2:
    print("Hai đường thẳng trùng nhau.")
elif a1/a2 == b1/b2 != c1/c2:
    print("Hai đường thẳng song song.")
elif a1/a2 != b1/b2:
    print("Hai đường thẳng cắt nhau.")
elif a1*b1 - a2*b2 == 0:
    print("Hai đường thẳng vuông góc.")
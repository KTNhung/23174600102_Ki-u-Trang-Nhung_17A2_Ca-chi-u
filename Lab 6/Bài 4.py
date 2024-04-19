#a. Dãy Fibonacci:
n = int(input("Nhập số lượng số Fibonacci: "))
if n <= 0:
    a = []
elif n == 1:
    a = [0]
elif n == 2:
    a = [0, 1]
else: 
    a = [0, 1]
    [a.append(a[-2] + a[-1]) for i in range(2, n)]
print(f"Dãy số Fibonacci có {n} số đầu tiên là {a}")


#b. Danh sách số nguyên tố nhỏ hơn 100

b = [i for i in range(2, 100) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]

print("Danh sách các số nguyên tố nhỏ hơn 100 là:", b)

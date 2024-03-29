#a. 
S1 = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        S1 += i
print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng [200;4000] là:", S1)

#b.
S2 = 0
for j in range(500, 1001):
    if j % 4 == 0 and j % 6 != 0:
        S2 += j 
print("Tổng các số chia hết cho 4 nhưng khong chia hết cho 6 trong khoảng từ [500; 1000] là:", S2)
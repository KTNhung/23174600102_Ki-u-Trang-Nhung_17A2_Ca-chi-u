#Nhập 1 số nguyên và in ra số chữ số của số nguyên đó
n = int(input("Nhập vào 1 số: "))
dem = 0
while True:
    n = n // 10 
    dem += 1 
    if n == 0:
        break
    
print(dem)
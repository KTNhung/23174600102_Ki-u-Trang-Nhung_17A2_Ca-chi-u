n = input("Nhập chuỗi ký tự: ")

chu_thuong = 0 
chu_hoa = 0 
chu_so = 0
ky_tu_dac_biet = 0 

for i in n: 
    if i.isupper():
        chu_hoa += 1
    else:
        chu_thuong += 1

    if i.isdigit():
        chu_so += 1 
    
    if not i.isalnum():
        ky_tu_dac_biet += 1 

print(f"Số lượng chữ thường: {chu_thuong}")
print(f"Số lượng chữ hoa: {chu_hoa}")
print(f"Số lượng chữ số: {chu_so}")
print("Số lượng ký tự đặc biệt:", ky_tu_dac_biet)
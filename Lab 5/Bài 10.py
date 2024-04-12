n = input("Nhập ký tự: ").strip()

str = ""
for i in n:
    if i != " ":
        str += i 
    else:
        continue
        

print("Chuỗi ký tự sau khi đã xóa tất cả khoảng trắng:", str)
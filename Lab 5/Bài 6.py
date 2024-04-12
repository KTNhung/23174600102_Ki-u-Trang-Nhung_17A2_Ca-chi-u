n = input("Nhập chuỗi ký tự: ")
for i in n:
    if i.isalnum():
        continue
    else:
        print("Chuỗi đã nhập chứa các ký tự đặc biệt.")
        break
        

str = ""
for i in n:
    if i.isalnum():
        continue
    else:
        str += i

for j in str: 
    a = str.count(j)
    print(f"Số lần xuất hiện của ký tự {j} là {a}")

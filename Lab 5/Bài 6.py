n = input("Nhập chuỗi ký tự: ")
for i in n:
    if i.isalnum():
        continue
    else:
        print("Chuỗi đã nhập chứa các ký tự đặc biệt.")
        break
        

str = 0
for i in n:
    if i.isalnum():
        continue
    else:
        str += 1
ty_le = (str/(len(n)))*100
print(f"Số ký tự đặc biệt xuất hiện trong chuỗi là {str} với tỷ lệ xuất hiện {ty_le:.2f}%")



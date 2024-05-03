kho = {
 "banana": 6,
 "apple": 5,
 "orange": 32,
 "pear": 15
}
gia_tien = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}

hoa_don = []
so_luong_trong_kho = 0
while True: 
    
    mat_hang = input("Nhập mặt hàng bạn muốn mua: ").strip()
    if mat_hang != "banana" and mat_hang != "apple" and mat_hang != "organe" and mat_hang != "pear":
        print("Không tồn tại mặt hàng này.")    
        break
    so_luong = int(input('Nhập số lượng: '))
    if mat_hang == "banana":
        so_luong_trong_kho = kho['banana']
    elif mat_hang == "apple":
        so_luong_trong_kho = kho['apple']
    elif mat_hang == "organe":
        so_luong_trong_kho = kho['organe']
    elif mat_hang == "pear":
        so_luong_trong_kho = kho['pear']

    if mat_hang == "banana" and so_luong > so_luong_trong_kho:
        print("Vượt quá số lượng.")
    elif mat_hang == "apple" and so_luong > so_luong_trong_kho:
        print("Vượt quá số lượng.")
    elif mat_hang == "orange" and so_luong >  so_luong_trong_kho:
        print("Vượt quá số lượng.")
    elif mat_hang == "pear" and so_luong > so_luong_trong_kho:
        print("Vượt quá số lượng.")
    

    else:
        don_gia = ' '
        hoa_don.append({
            'mat_hang_da_mua': mat_hang,
            'so_luong_da_mua': so_luong,
            'don_gia': don_gia
            })
    
        if mat_hang == "banana":
            kho['banana'] = so_luong_trong_kho - so_luong 
        elif mat_hang == "apple":
            kho['apple'] = so_luong_trong_kho - so_luong 
        elif mat_hang == "organe":
            kho['organe'] = so_luong_trong_kho - so_luong 
        elif mat_hang == "pear":
            kho['pear'] = so_luong_trong_kho - so_luong 

    choose = input("Bạn có muốn mua tiếp không ? (Y/N)").strip().upper()
    if choose == "N":
        break

for i in range(len(hoa_don)):
    if hoa_don[i]['mat_hang_da_mua'] == "banana": 
        hoa_don[i]["don_gia"] = hoa_don[i]['so_luong_da_mua'] * gia_tien["banana"]
    elif hoa_don[i]['mat_hang_da_mua'] == "apple": 
        hoa_don[i]["don_gia"] = hoa_don[i]['so_luong_da_mua'] * gia_tien["apple"]
    elif hoa_don[i]['mat_hang_da_mua'] == "organe": 
        hoa_don[i]["don_gia"] = hoa_don[i]['so_luong_da_mua'] * gia_tien["organe"]
    elif hoa_don[i]['mat_hang_da_mua'] == "pear": 
        hoa_don[i]["don_gia"] = hoa_don[i]['so_luong_da_mua'] * gia_tien["pear"]

for i in hoa_don:
    print(i)



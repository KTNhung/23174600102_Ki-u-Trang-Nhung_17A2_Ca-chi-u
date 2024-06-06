import random
import csv
import os

du_lieu = []
luu_tru_du_lieu = {}

danh_sach_mau = ['pink', 'blue', 'purple', 'cyan', 'green', 'black', 'white', 'brown', 'red', 'gray']
ds_mau_da_rut = set()
so_luong_bong = dict()
ds_so_mau_da_rut = dict()
xac_suat_rut_duoc_bong_cua_1_mau = ''



def rolls(a):
    for i in danh_sach_mau:
        so_luong_bong[i] = 1 
    roll = random.choice(danh_sach_mau)
    so_luong_bong[roll] -= 1
    ds_mau_da_rut.add(roll)
    return roll, so_luong_bong

for i in danh_sach_mau:
    ds_so_mau_da_rut[i] = 0 

X = 0 
for i in danh_sach_mau:
    so_luong_bong[i] = 1 
for i in so_luong_bong:
    X += so_luong_bong[i]
xac_suat_rut_duoc_bong_cua_1_mau = (so_luong_bong[i])/X
print("Xác xuất rút được bóng của 1 màu là:", xac_suat_rut_duoc_bong_cua_1_mau)

flag = 0   
i = 0
while i < 5:
    a, b = rolls(danh_sach_mau)
    ds_so_mau_da_rut[a] += 1
    print("Màu rút được là:",a,)

    S = 0 
    for c in b:
        S += b[c]
    print("Số lượng bóng còn lại là:",S)
    print()
    du_lieu.append({
    "Mau_bong_rut": a,
    "Xac_suat_rut_duoc_bong_cua_1_mau": xac_suat_rut_duoc_bong_cua_1_mau,
    "So_luong_bong_con_lai": S
    })
    i += 1 

    if ds_so_mau_da_rut[a] == 3:
        flag = 1
if flag == 1:
    print("You win.")
else:
    print("You lose.")


path_hien_tai = os.getcwd()
csv_path = path_hien_tai + "\\De_9.csv"
file = open(csv_path, 'w', newline = '')
a = ["Mau_bong_rut", "Xac_suat_rut_duoc_bong_cua_1_mau", "So_luong_bong_con_lai"]
write = csv.DictWriter(file, fieldnames= a)
write.writeheader()
for i in du_lieu:
    write.writerow(i)


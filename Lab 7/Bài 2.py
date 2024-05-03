list = []
while True: 
    ten = input("Nhập tên sinh viên: ").strip()
    diem_thi = float(input("Nhập điểm thi: "))
    hoc_luc = ""
    if not ten.isalpha:
        break
    elif diem_thi < 0 or diem_thi > 10:
        break
    list.append({
        'ten': ten,
        'diem_thi': diem_thi,
        'hoc_luc': hoc_luc
        })
    
for i in range(len(list)+ 1):
    for j in range(i):
        if list[j]["diem_thi"] < 4:
            list[j]['hoc_luc'] == "F"
        elif 4 <= list[j]["diem_thi"] <= 5.4:
            list[j]['hoc_luc'] = "D"
        elif 5.5 <= list[j]["diem_thi"] <= 6.9:
            list[j]['hoc_luc'] = "C"
        elif 7.0 <= list[j]["diem_thi"] <= 8.4:
            list[j]['hoc_luc'] = "B"
        elif 8.5 <= list[j]["diem_thi"] <= 10.0:
            list[j]['hoc_luc'] = "A"
A = 0
B = 0 
C = 0
D = 0
F = 0
for j in range(len(list)):
    if list[j]['hoc_luc'] == "F":
        F += 1 
    elif list[j]['hoc_luc'] == "D":
        D += 1
    elif list[j]['hoc_luc'] == "C":
        C += 1
    elif list[j]['hoc_luc'] == "B":
        B += 1
    elif list[j]['hoc_luc'] == "A":
        A += 1
        

for i in list: 
    print(i)
    
print(f"Số học sinh đạt điểm F là {F}")
print(f"Số học sinh đạt điểm D là {D}")
print(f"Số học sinh đạt điểm C là {C}")
print(f"Số học sinh đạt điểm B là {B}")
print(f"Số học sinh đạt điểm A là {A}")
    


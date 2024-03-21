print("Các thể loại phim: Hành động, Kinh dị, Tình cảm, Hài hước và Hoạt hình.")
a = input("Vui lòng lựa chọn thể loại phim: ")
b = input("Vui lòng lựa thời gian chiếu phim: ").lower()
if a == "Hành động":
    print(f"Phim {a} có suất chiếu vào buổi {b}")
elif a == "Kinh dị":
    if b == "sáng" or b == "trưa" or b == "chiều":
        print("Không có suất chiếu.")
    elif b == "tối":
        print(f"Phim {a} có suất chiếu vào buổi {b}.")
elif a == "Hài hước":
    print(f"Phim {a} có suất chiếu vào buổi {b}.")
elif a == "Tình cảm":
    if b == "sáng" or b == "trưa" or b == "chiều":
        print("Không có suất chiếu.")
    elif b == "tối":
        print(f"Phim {a} có suất chiếu vào buổi {b}.")
elif a == "Hoạt hình":
    if b == "sáng" or b == "trưa":
        print(f"Phim {a} có suất chiếu vào buổi {b}.")
    elif b == "chiều" or b == "tối":
        print("Không có suất chiếu.")   
else:
    print("Nhập không hợp lệ. Vui lòng nhập lại.")   
s = float(input("Nhập điểm số của một bài kiểm tra: "))
if 0 <= s < 5:
    print("Điểm kém.")
elif 5 <= s < 7:
    print("Điểm trung bình.")
elif 7 <= s < 8.5:
    print("Điểm khá.")
elif 8.5 <= 10:
    print("Điểm tốt.")
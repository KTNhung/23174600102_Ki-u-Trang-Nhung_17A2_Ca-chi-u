h = int(input("Nhập chiều cao: "))
w = int(input("Nhập cân nặng: "))
BMI = w/(h**2)
if BMI < 18.5:
    print("Gầy.")
elif 18.5 <= BMI <= 24.9:
    print("Bình thường.")
elif 25 <= BMI <= 29.9:
    print("Hơi béo.")
elif BMI >= 30:
    print("Béo.")

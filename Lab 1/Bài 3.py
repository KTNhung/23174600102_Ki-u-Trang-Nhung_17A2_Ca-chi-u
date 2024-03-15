x = 100000
#Tính toán số tiền có trong 5 năm 
S1 = x*(1.06**5)
amount_after_5_years = S1
print("Số tiền sẽ có sau 5 năm: {:.2f}".format(S1))

#Tính toán số tiền sẽ có sau 10 năm        
S2 = x*(1.06**10)
amount_after_10_years = S2
print("Số tiền sẽ có sau 10 năm là: {:.2f}".format(S2))

#Tính toán tỷ lệ tăng trưởng của số tiền bạn sẽ có au 10 năm so với số tiền bạn sẽ có sau 5 năm
S3 = (amount_after_10_years - amount_after_5_years )/amount_after_5_years
print("Tỷ lệ tăng trưởng của số tiền sau 10 năm so với 5 năm là: {:.2f}".format(S3))
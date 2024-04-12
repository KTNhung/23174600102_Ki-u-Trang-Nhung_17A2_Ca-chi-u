a=input('nhập chuỗi:')
b=True
c=''
for i in a:
    d=ord(i)
    if 48<=d<=57 or 65<=d<=98 or 97<=d<=122:
        continue
    else:
        b=False
        if c.count(i)==0:
            print(f'kí tự {i} có {a.count(i)} lần xuất hiện trong chuỗi và có tỉ lệ {(a.count(i)/len(a))*100:.2f}% trên toàn chuỗi')
            c+=i
if b==True:
    print('chuỗi không có kí tự đặc biệt nào')
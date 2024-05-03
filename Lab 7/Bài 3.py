''' Simile: A simile is a figure of speech that compares two different 
things using the words "like" or "as." It creates vivid imagery by drawing
parallels between unrelated objects or ideas. Example: "Her smile was as
bright as the sun. '''

text = '''Simile: A simile is a figure of speech that compares two different 
things using the words 'like' or 'as.'' It creates vivid imagery by drawing
parallels between unrelated objects or ideas. Example: 'Her smile was as
bright as the sun.'''
s = ''
a = []
text = text.lower()
for i in text:
    if i.isdigit() or i.isalpha():
        s += i
    elif s != '':
        a.append(s)
        s = ''
print(a) 
dic = {}  
for i in a:
    dic[i] = 0
for i in a:
    dic[i] += 1

dem = 0
for i in dic:
    if dem == 0:
        max = dic[i]
        key = i
        dem += 1
    else:
        if dic[i] > max:
            max = dic[i]
            key = i          
print(f"Từ xuất hiện nhiều nhất là {key} với tần suất {max}")
dem = 0
for i in dic:
    if dem == 0:
        min = dic[i]
        key = i
        dem += 1
    else:
        if dic[i] < min:
            min = dic[i]
            key = i   
print(f"Từ xuất hiện ít nhất là {key} với tần suất {min}")

'''print(f'Tỉ lệ từ {max(dic, key = dic.get)} nhiều nhất với tần suất {max(dic.values())}')
print(f'Tỉ lệ từ {min(dic, key = dic.get)} nhiều nhất với tần suất {min(dic.values())}')'''

string1 = "Hello"
string2 = "World"
str = ""
for i in range(len(string1)):
    str += string1[i] + "-" + string2[i] + "-"
print(str)
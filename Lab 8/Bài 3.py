#1
def cubesum(n:str):
    a = 0
    for i in n:
        a += int(i)**3
    return a


#2
#(a)
def PrintArmstrong():
    if isArmstrong(n):
        print(n)

#(b)
def isArmstrong(n):
    if cubesum(n) == int(n):
        return True
    return False
    
n = input('nhập n: ')
PrintArmstrong()
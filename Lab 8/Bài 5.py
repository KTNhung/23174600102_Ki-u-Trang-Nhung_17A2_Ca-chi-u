def isamicable(a,b):
    def sumPdivisors(n):
        return sum([i for i in range(1,n) if n % i == 0])

    if sumPdivisors(a) == b and sumPdivisors(b) == a:
        return True
    else:
        return False

a = int(input('nhập số a: '))
b = int(input('nhập số b: '))

if isamicable(a,b):
    print(f'{a} và {b} là một cặp số amicable')
else:
    print(f'{a} và {b} không là một cặp số amicable')
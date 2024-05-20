def tinh_hoanvi_tohop(n,r):
    from math import comb, perm
    return comb(n, r), perm(n, r)
n = int(input('nhập n:'))
r = int(input('nhập r:'))
hoan_vi,to_hop = tinh_hoanvi_tohop(n,r)
print(f'Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần: {hoan_vi}')
print(f'Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần: {to_hop}')
# https://atcoder.jp/contests/abc127/tasks/abc127_b

r, d, x = map(int, input().split())
algae = []
x_n = x
for i in range(10):
    z = r * x_n - d
    algae.append(z)
    x_n = z
for i in algae:
    print(i)
    

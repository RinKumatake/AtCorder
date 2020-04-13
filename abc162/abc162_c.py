# https://atcoder.jp/contests/abc162/tasks/abc162_c
import math
k = int(input())
a = []
for i in range(1, k+1):
    for j in range(1, k+1):
        x = math.gcd(i, j)
        for l in range(1, k+1):
            y = math.gcd(l, x)
            a.append(y)
print(sum(a))
        


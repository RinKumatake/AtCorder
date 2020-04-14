# https://atcoder.jp/contests/abc134/tasks/abc134_b
import math
n, d = map(int, input().split())
x = d * 2 + 1
print(math.ceil(n/x))


# https://atcoder.jp/contests/abc137/tasks/abc137_a

a, b = map(int, input().split())
x = a + b
y = a - b
z = a * b
print(max(x, y, z))
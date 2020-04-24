# https://atcoder.jp/contests/abc103/tasks/abc103_a

a = list(map(int, input().split()))
b = sorted(a, reverse=True)
x = b[0] - b[1]
y = b[1] - b[2]
print(x + y)
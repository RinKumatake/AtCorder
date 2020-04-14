# https://atcoder.jp/contests/abc136/tasks/abc136_a

a, b, c = map(int, input().split())
x = a - b
y = c - x
print(max(y, 0))
    
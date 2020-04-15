# https://atcoder.jp/contests/abc131/tasks/abc131_b
n, l = map(int, input().split())
apple = 0
if l >= 0:
    for i in range(2, n+1):
        taste = l + i -1
        apple += taste
elif l < 0 and n > abs(l):
    for i in range(1, n+1):
        taste = l + i -1
        apple += taste
else:
    for i in range(1, n):
        taste = l + i -1
        apple += taste

print(apple)


# https://atcoder.jp/contests/abc120/tasks/abc120_b

a, b, k = map(int, input().split())
x = min(a, b)
num = []
for i in range(1, x+1):
    if a % i == 0 and b % i == 0:
        num.append(i)
print(num[len(num)-k])


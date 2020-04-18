# https://atcoder.jp/contests/abc121/tasks/abc121_b
n, m, c = map(int, input().split())
b = list(map(int, input().split()))
cord = []
accept = 0
for i in range(n):
    a = list(map(int, input().split()))
    cord.append(a)
for i in cord:
    a = 0
    for j in range(m):
        x = i[j] * b[j]
        a += x
    if a + c > 0:
        accept += 1
print(accept)


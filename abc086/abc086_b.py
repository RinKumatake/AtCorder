# https://atcoder.jp/contests/abc086/tasks/abc086_b
a, b = input().split()
c = int(a + b)
ans = 0
for i in range(400):
    if i ** 2 == c:
        ans+=1

if ans >= 1:
    print("Yes")
else: 
    print("No")
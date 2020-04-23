# https://atcoder.jp/contests/abc105/tasks/abc105_b
n = int(input())
x = n // 4
y = n // 7
ans = 0
for i in range(x+1):
    for j in range(y+1):
        if i*4 + j*7 ==n:
            ans += 1
if ans >=1:
    print("Yes")
else:
    print("No")

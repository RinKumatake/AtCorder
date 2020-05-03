#https://atcoder.jp/contests/abc165/tasks/abc165_a
k = int(input())
a,b = map(int, input().split())
ans = 0
for i in range(a, b+1):
    if i % k == 0:
        ans +=1
        break
if ans > 0:
    print("OK")
else:
    print("NG")
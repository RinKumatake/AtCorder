# https://atcoder.jp/contests/abc135/tasks/abc135_b

n = int(input())
p = list(map(int, input().split()))
o = [i for i in range(1,n+1)]
k = 0
for i in range(n):
    if p[i] != o[i]:
        k += 1

if k == 0 or k == 2:
    print("YES")
else:
    print("NO")
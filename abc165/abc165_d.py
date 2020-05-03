# https://atcoder.jp/contests/abc165/tasks/abc165_d
a,b,n = map(int, input().split())
if b > n:
    ans = (a*n-(a%b))/b - a*((n-(n%b))/b)
else:
    x = b - 1
    ans = (a*x-(a%b))/b - a*((x-(x%b))/b)

print(int(ans))
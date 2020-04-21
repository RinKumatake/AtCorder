# https://atcoder.jp/contests/abc154/tasks/abc154_c
n = int(input())
a = list(map(int, input().split()))
a_2 = set(a)
if len(a) == len(a_2):
    print("YES")
else:
    print("NO")

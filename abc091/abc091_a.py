# https://atcoder.jp/contests/abc091/tasks/abc091_a
a,b,c = map(int, input().split())
d = a + b
if d >= c:
    print("Yes")
else:
    print("No")

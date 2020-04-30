# https://atcoder.jp/contests/abc096/tasks/abc096_a
a, b = map(int, input().split())
if b < a:
    print(a-1)
else:
    print(a)
# https://atcoder.jp/contests/abc164/tasks/abc164_a
s, w = map(int, input().split())
if w >= s:
    print("unsafe")
else:
    print("safe")
# https://atcoder.jp/contests/abc112/tasks/abc112_b
n, T = map(int, input().split())
root = []
for i in range(n):
    c,t = map(int, input().split())
    if T >= t:
        root.append(c)
if root == []:
    print("TLE")
else:
    sort_root = sorted(root)
    print(sort_root[0])
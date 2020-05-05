# https://atcoder.jp/contests/abc166/tasks/abc166_c
n, m = map(int, input().split())
h = list(map(int, input().split()))
view = [True] * n
for j in range(m):
    a, b = map(int, input().split())
    a -=1
    b -=1
    if h[a] < h[b]:
        view[a] = False
    elif h[a] > h[b]:
        view[b] = False
    elif h[a] == h[b]:
        view[a] = False
        view[b] = False

print(view.count(True))
    


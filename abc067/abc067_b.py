# https://atcoder.jp/contests/abc067/tasks/abc067_b
n, k = map(int, input().split())
l = list(map(int, input().split()))
sort_l = sorted(l, reverse=True)
snake = 0
for i in range(k):
    snake += sort_l[i]
print(snake)